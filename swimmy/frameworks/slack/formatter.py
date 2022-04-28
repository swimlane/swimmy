import inspect
from ..formatter import FormatterBase
from .messaging import Messaging


class Formatter(FormatterBase):

    def _build_card(self, method_name, results, application_id=None, record_id=None):
        caller = method_name.rsplit('_',1)[-1].capitalize()
        message = Messaging()
        if record_id:
            message.add_header(f'Swimlane Record')
            endpoint = self.ENDPOINT_MAP.get(method_name).substitute(id=record_id)
            message.add_markdown_section(
                text='New Swimlane Record',
                accessory=message.create_accessory(
                    type='button',
                    url=f"{self.instance.swimlane.host}/{endpoint}/",
                    text='New Swimlane Record'
                )
            )
        elif results and isinstance(results, list):
            message.add_header(f'Swimlane {caller}')
            for item in results:
                text = item.get('name')
                endpoint = self.ENDPOINT_MAP.get(method_name).substitute(
                    application_id=application_id,
                    id=item.get('id'),
                    default_report_id=item.get('default_report_id')
                )
                text = item.get('name')
                display_text = text
                url = f"{self.instance.swimlane.host}/{endpoint}/"
                if method_name == 'get_application_tasks':
                    display_text = f"{item.get('name')}\n{item.get('description')}"
                if item.get('url') and item.get('text'):
                    text = item['text']
                    url = item['url']
                if item.get('vendor') and item.get('product'):
                    text = f"{item.get('vendor')} {item.get('product')} ({item.get('version')})\n{item.get('description')}"
                if item.get('pythonVersion'):
                    text = f"{item['name']} ({self.VERSION_MAP.get(item['pythonVersion'])}) {item['version']}\n{item['summary']}\n{item['homePage']}"
                message.add_markdown_section(
                    text=text,
                    accessory=message.create_accessory(
                        type='button',
                        url=url,
                        text=display_text
                    )
                )         
        elif results and isinstance(results, dict):
            text = ''
            if results.get('json') and results['json'].get('Tracking Id'):
                message.add_markdown_section(
                    text=f"{results.get('json').get('Tracking Id')} ({results.get('id')})\nCreated: {results.get('created')}\nLast Modified: {results.get('modified')}",
                    accessory=message.create_accessory(
                        type='button',
                        url=f"{self.instance.swimlane.host}/record/{results.get('application_id')}/{results.get('id')}",
                        text=results.get('json').get('Tracking Id')
                    )
                )
            else:
                for key,val in results.items():
                    if not key.startswith('$') and val:
                        text += f':white_check_mark: \t{key}'
                    elif not key.startswith('$') and not val:
                        text += f':x: \t{key}'
                message.add_markdown_section(text=text)
        return message.get_blocks()

    def build(self, results, application_id=None, record_id=None):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        method_name = calframe[1][3]
        self.__logger.info(f'Creating format block for {method_name}')
        return self._build_card(method_name=method_name, results=results, application_id=application_id, record_id=record_id)
