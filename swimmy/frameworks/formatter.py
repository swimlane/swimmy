from abc import abstractmethod
from string import Template
from ..base import Base


class FormatterBase(Base):
    
    ENDPOINT_MAP = {
        'get_assets': Template("integration/assets"),
        'get_workspaces': Template("workspace/$id"),
        'get_applications_light': Template("search/$id/$default_report_id"),
        'get_plugins': Template("integration/plugins"),
        'get_pip_packages': Template("integration/python-packages"),
        'get_users': Template("user/$id"),
        'get_application_tasks': Template("integration/$application_id/task/$id"),
        'get_application_by_acronym': Template('record/$id')

    }
    VERSION_MAP = {
        'python3_6': 'Python 3.6',
        'python2_7': 'Python 2.7',
        'python3_7': 'Python 3.7',
        'python3': 'Python 3.7'
    }
    try_command_string = Template("""

Please try one of the following commands:

* workspaces, assets, applications, plugins, packages, users, health, help
* search [search_string]
* get record [tracking_id]
* get [acronym] tasks
* create [acronym] record

When using the search command Swimmy is configured to return the first $search_results_max_results results.
""")

    @abstractmethod
    def build(self, results):
        raise NotImplementedError()
