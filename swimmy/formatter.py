from .base import Base
from .config import Config
from .messaging import Messaging


class Formatter(Base):

    try_command_string = f"""

Please try one of the following commands:

* workspaces, assets, applications, plugins, packages, users, health, help
* search [search_string]
* get record [tracking_id]
* get [acronym] tasks
* create [acronym] record

When using the search command Swimmy is configured to return the first {Config.search_results_max_results} results.
"""

    def __init__(self, host_name) -> None:
        self.host_name = host_name
        self.message = Messaging()

    def get_common_usage(self, results):
        self.__logger.info('Creating format block for get_common_usage')
        self.message.add_header('Swimlane Common Usage Stats')
        if results and isinstance(results, list):
            for item in results:
                if item and isinstance(item, dict):
                    text = f'{item.pop("type")}: {item.pop("name")}'
                    for key,val in item.items():
                        if isinstance(val, int):
                            text += f"{key}: {val}"
                    self.message.add_markdown_section(
                        text=text,
                    )
        else:
            self.message.add_markdown_section()
        return self.message.get_blocks()

    def health(self, results):
        self.__logger.info('Creating format block for health')
        self.message.add_header(f'Swimlane Health')
        if results and isinstance(results, dict):
            text = ''
            for key,val in results.items():
                if not key.startswith('$') and val:
                    text += f':white_check_mark: \t{key}\n\n'
                elif not key.startswith('$') and not val:
                    text += f':x: \t{key}\n\n'
            self.message.add_markdown_section(
                text=text,
            )
        else:
            self.message.add_markdown_section()
        return self.message.get_blocks()

    def task_names(self, results, acronym, application_id):
        self.__logger.info('Creating format block for task_names')
        self.message.add_header(f'{acronym} Application Tasks')
        if results and isinstance(results, list):
            for item in results:
                if item:
                    text = f"{item.get('name')}\n{item.get('description')}"
                    self.message.add_markdown_section(
                        text=text,
                        accessory=self.message.create_accessory(
                            type='button',
                            url=f"{self.host_name}/integration/{application_id}/task/{item.get('id')}",
                            text=item.get('name')
                        )
                    )
        else:
            self.message.add_markdown_section()
        return self.message.get_blocks()

    def plugin_names(self, results):
        self.__logger.info('Creating format block for plugin_names')
        self.message.add_header('Installed Swimlane Plugins')
        if results and isinstance(results, list):
            for item in results:
                if item:
                    text = f"*{item.get('vendor')} {item.get('product')}* :zap:{item.get('version')}:zap:\n{item.get('description')}"
                    self.message.add_markdown_section(
                        text=text,
                        accessory=self.message.create_accessory(
                            type='button',
                            url=f"{self.host_name}/search/{item.get('id')}/{item.get('default_report_id')}",
                            text=item.get('name')
                        )
                    )
        else:
            self.message.add_markdown_section()
        return self.message.get_blocks()

    def application_names(self, results):
        self.__logger.info('Creating format block for application_names')
        self.message.add_header('Swimlane Applications')
        if results and isinstance(results, list):
            for item in results:
                if item:
                    self.message.add_markdown_section(
                        text=item.get('name'),
                        accessory=self.message.create_accessory(
                            type='button',
                            url=f"{self.host_name}/search/{item.get('id')}/{item.get('default_report_id')}",
                            text=item.get('name')
                        )
                    )
        else:
            self.message.add_markdown_section()
        return self.message.get_blocks()

    def workspace_names(self, results):
        self.__logger.info('Creating format block for workspace_names')
        self.message.add_header('Swimlane Workspaces')
        if results and isinstance(results, list):
            for item in results:
                if item:
                    self.message.add_markdown_section(
                        text=item.get('name'),
                        accessory=self.message.create_accessory(
                            type='button',
                            url=f"{self.host_name}/workspace/{item.get('id')}/",
                            text=item.get('name')
                        )
                    )
        else:
            self.message.add_markdown_section()
        return self.message.get_blocks()

    def asset_names(self, results):
        self.__logger.info('Creating format block for asset_names')
        self.message.add_header('Swimlane Assets')
        if results and isinstance(results, list):
            for item in results:
                if item:
                    self.message.add_markdown_section(
                        text=item.get('name'),
                        accessory=self.message.create_accessory(
                            type='button',
                            url=f"{self.host_name}/integration/assets",
                            text=item.get('name')
                        )
                    )
        else:
            self.message.add_markdown_section()
        return self.message.get_blocks()

    def pip_packages(self, results):
        self.__logger.info('Creating format block for pip_packages')
        self.message.add_header('Installed Pip Packages')
        if results and isinstance(results, list):
            for item in results:
                if item and 'pythonVersion' in item:
                    if item.get('pythonVersion'):
                        if item['pythonVersion'] == 'python3_6':
                            python_version = 'Python 3.6'
                        elif item['pythonVersion'] == 'python2_7':
                            python_version = 'Python 2.7'
                        elif item['pythonVersion'] == 'python3_7':
                            python_version = 'Python 3.7'
                        else:
                            python_version = 'Unknown'
                    else:
                        python_version = 'Unknown'
                    text = f"*{item['name']}* ({python_version}) :zap:{item['version']}:zap:\n{item['summary']}\n{item['homePage']}"
                    self.message.add_markdown_section(
                        text=text,
                        accessory=self.message.create_accessory(
                            type='button',
                            url=f"{self.host_name}/integration/python-packages",
                            text=item.get('name')
                        )
                    )
        else: 
            self.message.add_markdown_section()
        return self.message.get_blocks()

    def users(self, results):
        self.__logger.info('Creating format block for users')
        self.message.add_header('Swimlane Users')
        if results:
            for item in results:
                self.message.add_markdown_section(
                    text=f"{item.display_name} ({item.username})",
                    accessory=self.message.create_accessory(
                        type='button',
                        url=f"{self.host_name}/user/{item.id}",
                        text=item.display_name
                    )
                )
        else:
            self.message.add_markdown_section()
        return self.message.get_blocks()

    def record_info(self, results):
        self.__logger.info('Creating format block for record_info')
        self.message.add_header('Swimlane Record Info')
        if results:
            self.message.add_markdown_section(
                text=f"{results.get('json').get('Tracking Id')} ({results.get('id')})\nCreated: {results.get('created')}\nLast Modified: {results.get('modified')}",
                accessory=self.message.create_accessory(
                    type='button',
                    url=f"{self.host_name}/record/{results.get('application_id')}/{results.get('id')}",
                    text=results.get('json').get('Tracking Id')
                )
            )
        else:
            self.message.add_markdown_section()
        return self.message.get_blocks()

    def create_record_info(self, results):
        self.__logger.info('Creating format block for create_record_info')
        self.message.add_header('Swimlane Create Record')
        if results:
            self.message.add_markdown_section(
                text=f"Please create a new record below:\n",
            )
            self.message.add_button_action_element(
                f'New Swimlane Record', 
                url=f"{self.host_name}/record/{results.id}/",
                )
        else:
            self.message.add_markdown_section()
        return self.message.get_blocks()

    def search_results(self, results, ioc_type, ioc_value):
        self.__logger.info('Creating format block for search_results')
        self.message.add_header(f'Swimlane Search Results')
        if results:
            for result in results:
                if result:
                    self.message.add_markdown_section(
                        text=result.get('text'),
                        accessory=self.message.create_accessory(
                            type='button',
                            url=result.get('url'),
                            text=result.get('text')
                        )
                    )
        else:
            self.message.add_markdown_section()
        return self.message.get_blocks()

    def error(self, endpoint, unknown=False):
        if unknown:
            self.message.add_header('Swimmy was unable to process your request.')
            help_text = f"""
Swimmy encountered an unknown error when attempting to retrieve data about {endpoint}.
{self.try_command_string}
If you continue to encounter issues, please reach out to your Slack administrator.
"""
        else:
            self.message.add_header('Swimmy did not receive a response from Swimlane.')
            help_text = f"""
Swimmy did not receive a response from Swimlane. This means that either there were no results or an error occurred.
{self.try_command_string}
"""
        self.__logger.info('Creating format block for error message')
        self.message.add_markdown_section(
            text=help_text
        )
        return self.message.get_blocks()

    def help(self, text):
        self.message.add_header('How do I use Swimmy?')
        help_text = f"""
Swimmy cannot understand your request {text}
{self.try_command_string}
"""
        self.__logger.info('Creating format block for help')
        self.message.add_markdown_section(
            text=help_text
        )
        return self.message.get_blocks()
