from slack_bolt import App
from slack_sdk.web import WebClient
from ..actions import FrameworkActions
from ...base import Base


try:
    # Initialize a Bolt for Python app
    APP = App(
        token=Base.config.slack['bot_token'],
        signing_secret=Base.config.slack['bot_signing_secret']
    )
    client = WebClient(token=Base.config.slack['bot_token'])
except:
    raise Exception('Please make sure you have provided your Slack Token and Signing Secret')


@APP.command("/swimmy")
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
    if body.get('text'):
        text = body['text'].strip().lower()
        resp = FrameworkActions().parse(text)
        if resp:
            respond(blocks=resp)


def create_bot():
    APP.start(port=3001)
    return APP
