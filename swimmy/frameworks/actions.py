import re
from ..base import Base


class FrameworkActions(Base):

    def parse(self, text):
        if text:
            request_string = text.split()
            if len(request_string) == 1:
                if request_string[0] == 'workspaces':
                    return self.instance.get_workspaces()
                elif request_string[0] == 'assets':
                    return self.instance.get_assets()
                elif request_string[0] == 'applications':
                    return self.instance.get_applications_light()
                elif request_string[0] == 'plugins':
                    return self.instance.get_plugins()
                elif request_string[0] == 'packages':
                    return self.instance.get_pip_packages()
                elif request_string[0] == 'users':
                    return self.instance.get_users()
                elif request_string[0] == 'health':
                    return self.instance.get_health()
                elif request_string[0] == 'help':
                    from .formatter import FormatterBase
                    return FormatterBase().try_command_string.substitute(search_results_max_results=self.config.search_results_max_results)
            elif len(request_string) == 2:
                if request_string[0] == 'search':
                    search_term = request_string[1]
                    if search_term and search_term.strip():
                        return self.instance.search(search_term.strip())
            elif len(request_string) == 3:
                if request_string[0] == 'get' and request_string[1] == 'record':
                    tracking_id = request_string[2].strip().upper()
                    if tracking_id:
                        return self.instance.get_record(tracking_id=tracking_id)
                elif request_string[0] == 'get' and request_string[2] == 'tasks':
                    application_acronym = request_string[1]
                    matches = re.match('^[a-zA-z]{2,4}$', application_acronym.strip())
                    if matches:
                        application = self.instance.get_application_by_acronym(matches.group())
                        if application and application.id:
                            return self.instance.get_application_tasks(application.id)
                elif request_string[0] == 'create' and request_string[2] == 'record':
                    # used when wanting to create a record in a desired application
                    application_acronym = request_string[1]
                    matches = re.match('^[a-zA-z]{2,4}$', application_acronym.strip())
                    if matches:
                        return self.instance.get_application_by_acronym(matches.group(), return_formatted_card=True)
