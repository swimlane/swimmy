import re
from slack_bolt import App
from slack_sdk.web import WebClient
from .instance import SwimlaneInstance
from .formatter import Formatter
from .config import Config


config = Config


try:
    # Initialize a Bolt for Python app
    app = App(
        token=config.slack['bot_token'],
        signing_secret=config.slack['bot_signing_secret']
    )
    client = WebClient(token=config.slack['bot_token'])
except:
    raise Exception('Please make sure you have provided your Slack Token and Signing Secret')

try:
    # Connecting to the desired Swimlane instance
    swimlane = SwimlaneInstance(**config.swimlane)
except:
    raise Exception('Please make sure you have the correct authentication credentials to your Swimlane instance.')


@app.command("/swimmy")
def swimmy(ack, respond, body):
    """This is the main slash command for swimmy.

    When using the /swimmy command you can pass the following values/structures:
        * workspaces
        * assets
        * applications
        * plugins
        * packages
        * users
        * health
        * help
        * search __some_search_string__
        * get record __tracking_id__
        * get __application_acronym__ tasks
        * create __application_acronym__ record
    """
    ack()
    blocks = []
    if body.get('text'):
        request_string = body['text'].split()
        formatter = Formatter(swimlane.swimlane.host)
        if len(request_string) == 1:
            if request_string[0] == 'workspaces':
                results = swimlane.get_swimlane_workspaces()
                if results:
                    blocks = formatter.workspace_names(results)
                    if not blocks:
                        blocks = formatter.error(endpoint='workspaces', unknown=True)
                else:
                    blocks = formatter.error(endpoint='workspaces')
            elif request_string[0] == 'assets':
                results = swimlane.get_swimlane_assets()
                if results:
                    blocks = formatter.asset_names(results)
                    if not blocks:
                        blocks = formatter.error(endpoint='assets', unknown=True)
                else:
                    blocks = formatter.error(endpoint='assets')
            elif request_string[0] == 'applications':
                results = swimlane.get_swimlane_applications_light()
                if results:
                    blocks = formatter.application_names(results)
                    if not blocks:
                        blocks = formatter.error(endpoint='applications', unknown=True)
                else:
                    blocks = formatter.error(endpoint='applications')
            elif request_string[0] == 'plugins':
                results = swimlane.get_swimlane_plugins()
                if results:
                    blocks = formatter.plugin_names(results)
                    if not blocks:
                        blocks = formatter.error(endpoint='plugins', unknown=True)
                else:
                    blocks = formatter.error(endpoint='plugins')
            elif request_string[0] == 'packages':
                results = swimlane.get_pip_packages()
                if results:
                    blocks = formatter.pip_packages(results)
                    if not blocks:
                        blocks = formatter.error(endpoint='packages', unknown=True)
                else:
                    blocks = formatter.error(endpoint='packages')
            elif request_string[0] == 'users':
                results = swimlane.get_swimlane_users()
                if results:
                    blocks = formatter.users(results)
                    if not blocks:
                        blocks = formatter.error(endpoint='users', unknown=True)
                else:
                    blocks = formatter.error(endpoint='users')
            elif request_string[0] == 'health':
                results = swimlane.get_swimlane_health()
                if results:
                    blocks = formatter.health(results)
                    if not blocks:
                        blocks = formatter.error(endpoint='health', unknown=True)
                else:
                    blocks = formatter.error(endpoint='health')
            elif request_string[0] == 'help':
                blocks = Formatter(swimlane.swimlane.host).help(body['text'])
                if not blocks:
                    blocks = formatter.error(endpoint='help', unknown=True)
            else:
                blocks = Formatter(swimlane.swimlane.host).help(body['text'])
        elif len(request_string) == 2:
            if request_string[0] == 'search':
                search_term = request_string[1]
                if search_term and search_term.strip():
                    results = swimlane.search_swimlane(search_term.strip())
                    if results:
                        blocks = formatter.search_results(
                            results=results,
                            ioc_type='String Search',
                            ioc_value=search_term.strip()
                        )
                        if not blocks:
                            blocks = formatter.error(endpoint='search', unknown=True)
                    else:
                        blocks = formatter.error(endpoint='search')
                else:
                    blocks = formatter.error(endpoint='search', unknown=True)
            else: 
                blocks = Formatter(swimlane.swimlane.host).help(body['text'])
        elif len(request_string) == 3:
            if request_string[0] == 'get' and request_string[1] == 'record':
                tracking_id = body['text'].split('get record')[-1].strip()
                if tracking_id:
                    results = swimlane.get_swimlane_record(tracking_id=tracking_id)
                    if results:
                        blocks = formatter.record_info(results)
                        if not blocks:
                            blocks = formatter.error(endpoint='get record', unknown=True)
                    else:
                        blocks = formatter.error(endpoint='get record')
                else:
                    blocks = formatter.error(endpoint='get record')
            elif request_string[0] == 'get' and request_string[2] == 'tasks':
                application_acronym = request_string[1]
                matches = re.match('^[a-zA-z]{2,4}$', application_acronym.strip())
                if matches:
                    application = swimlane.get_application_by_acronym(matches.group())
                    if application and application.id:
                        results = swimlane.get_application_tasks(application.id)
                        if results:
                            blocks = formatter.task_names(
                                results=results,
                                acronym=matches.group(),
                                application_id=application.id
                            )
                            if not blocks:
                                blocks = formatter.error(endpoint='get tasks', unknown=True)
                        else:
                            blocks = formatter.error(endpoint='get tasks')
                    else:
                        blocks = formatter.error(endpoint='get tasks')
                else:
                    blocks = formatter.error(endpoint='get tasks')
            elif request_string[0] == 'create' and request_string[2] == 'record':
                # used when wanting to create a record in a desired application
                application_acronym = request_string[1]
                matches = re.match('^[a-zA-z]{2,4}$', application_acronym.strip())
                if matches:
                    results = swimlane.get_application_by_acronym(matches.group())
                    if results:
                        blocks = formatter.create_record_info(results)
                        if not blocks:
                            blocks = formatter.error(endpoint='create record', unknown=True)
                    else:
                        blocks = formatter.error(endpoint='create record')
                else:
                    blocks = formatter.error(endpoint='create record')
            else:
                blocks = formatter.help(body['text'])
        else:
            blocks = formatter.help(body['text'])
    if not blocks:
        blocks = formatter.error(endpoint='unknown', unknown=True)
    respond(blocks=blocks)


def create_bot():
    app.start(port=3001)
    return app
