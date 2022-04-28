from swimlane import Swimlane
from .base import Base
from .config import Config
from .decorators import log_exception


class SwimlaneInstance(Base):

    """Creates a connection to a Swimlane instance
    """

    def __init__(self, host='https://sw_web:4443', username=None, password=None, access_token=None,
                 verify_ssl=False, verify_server_version=False, default_timeout=300,
                 resource_cache_size=0, write_to_read_only=False):
        if self.config.framework == 'slack':
            from .frameworks.slack.formatter import Formatter
        elif self.config.framework == 'teams':
            from .frameworks.teams.formatter import TeamsFormatter as Formatter
        self.formatter = Formatter()
        if username and password:
            self.swimlane = Swimlane(
                host=host,
                username=username,
                password=password,
                verify_ssl=False,
                verify_server_version=verify_server_version,
                default_timeout=default_timeout,
                resource_cache_size=resource_cache_size,
                write_to_read_only=write_to_read_only
            )
        elif access_token:
            self.swimlane = Swimlane(
                host=host,
                access_token=access_token,
                verify_ssl=False,
                verify_server_version=verify_server_version,
                default_timeout=default_timeout,
                resource_cache_size=resource_cache_size,
                write_to_read_only=write_to_read_only
            )
        else:
            raise AttributeError('Please provide either a username and password or a access token!')

    @log_exception
    def get_record(self, tracking_id: str):
        self.__logger.info(f'Attempting to retrieve information about swimlane record {tracking_id}')
        acronym = tracking_id.split('-')[0]
        if acronym:
            app = self.get_application_by_acronym(acronym)
            if app:
                application = self.swimlane.apps.get(name=app.name)
                if application:
                    record = application.records.get(tracking_id=tracking_id.strip())
                    if record:
                        return self.formatter.parse_record(results={
                            'json': record.for_json(),
                            'created': record.created,
                            'modified': record.modified,
                            'id': record.id,
                            'application_id': app.id
                        })
        return {}

    @log_exception
    def get_application_by_acronym(self, acronym, return_formatted_card=False):
        self.__logger.info('Getting application by provided acronym')
        apps = self.swimlane.apps.list()
        if apps:
            for app in apps:
                if app.acronym == acronym.upper():
                    if return_formatted_card:
                        return self.formatter.build(record_id=app.id)
                    else:
                        return app

    @log_exception
    def get_plugins(self):
        return self.formatter.build(self.swimlane.request('GET', '/task/packages').json())

    def get_pip_packages(self, versions=['Python2_7', 'Python3_6', 'Python3']):
        return_list = []
        for version in versions:
            try:
                return_list.extend(self.swimlane.request('GET', '/pip/packages/{}'.format(version)).json())
            except:
                self.__logger.info(f"The specified version does not exist: {version}")
                pass
        return self.formatter.build(return_list)

    @log_exception
    def get_application_tasks(self, application_id):
        try:
            data = self.swimlane.request('GET', '/task?applicationId={}'.format(application_id)).json()
        except:
            data = self.swimlane.request('GET', '/task?parentId={}'.format(application_id)).json()
       # print(data)
        return self.formatter.build(data, application_id=application_id)

    @log_exception
    def get_assets(self):
        return self.formatter.build(self.swimlane.request('GET', '/asset').json())

    @log_exception
    def get_applications_light(self):
        results = self.swimlane.request('GET', '/app/light').json()
        if results:
            for item in results:
                item.update({
                    'default_report_id': self.get_default_report_by_application_id(item.get('id')).get('id')
                })
        return self.formatter.build(results)

    @log_exception
    def get_default_report_by_application_id(self, application_id):
        return self.swimlane.request('GET', f'/reports/app/{application_id}/default').json()

    @log_exception
    def get_workspaces(self):
        return self.formatter.build(self.swimlane.request('GET', '/workspaces').json())

    @log_exception
    def get_users(self):
        return self.formatter.build(self.swimlane.request('GET', '/user/light').json())

    @log_exception
    def get_health(self):
        return self.formatter.build(self.swimlane.request('GET', '/health').json())

    @log_exception
    def search(self, keyword):
        application_dict = {}
        url_list = []
        max_results = Config.search_results_max_results
        result = self.swimlane.request('GET', f'/search/keyword?keywords={keyword}&page=1&size={max_results}', **{'verify': False}).json()
        if result:
            if result.get('totalCount') >= 1:
                count = 0
                for item in result.get('results').get('items'):
                    if count < max_results:
                        if item.get('applicationId') and item['applicationId'] not in application_dict:
                            application_dict[item['applicationId']] = []
                        application_dict[item['applicationId']].append(item.get('id'))
                    else: break
                if application_dict:
                    for key,val in application_dict.items():
                        app = self.swimlane.apps.get(id=key)
                        for v in val:
                            url_list.append({
                                'url': f'{self.swimlane.host}/record/{key}/{v}',
                                'text': f'{app.name} - {app.records.get(id=v)}'
                            })
        return self.formatter.build(url_list)
