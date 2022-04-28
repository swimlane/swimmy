import inspect
from botbuilder.core import (
    CardFactory, 
    MessageFactory
)
from botbuilder.schema import (
    BasicCard, 
    CardAction, 
    HeroCard
)
from botbuilder.schema._connector_client_enums import ActionTypes
from ..formatter import FormatterBase


class TeamsFormatter(FormatterBase):

    def _create_button(self, title, value, display):
        return CardAction(
            type=ActionTypes.open_url,
            title=title,
            value=value,
            display_text=display
        )

    def _build_card(self, method_name, results, application_id=None, record_id=None):
        caller = method_name.rsplit('_',1)[-1].capitalize()
        card = BasicCard()
        card.title = 'Swimlane'
        card.subtitle = caller
        button_list = []
        if record_id:
            card.subtitle = 'Record'
            endpoint = self.ENDPOINT_MAP.get(method_name).substitute(id=record_id)
            button_list.append(
                self._create_button(
                    title=f"New Swimlane Record",
                    value=f"{self.instance.swimlane.host}/{endpoint}/",
                    display="New Swimlane Record"
                )
            )
        elif results and isinstance(results, list):
            for item in results:
                endpoint = self.ENDPOINT_MAP.get(method_name).substitute(
                    id=item.get('id'), 
                    default_report_id=item.get('default_report_id'),
                    application_id=application_id
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
                button_list.append(
                    self._create_button(
                        title=text,
                        value=url,
                        display=display_text
                    )
                )
        elif isinstance(results, dict):
            text = ''
            if results.get('json') and results['json'].get('Tracking Id'):
                button_list.append(
                    self._create_button(
                        title=f"{results.get('json').get('Tracking Id')} ({results.get('id')})\nCreated: {results.get('created')}\nLast Modified: {results.get('modified')}",
                        value=f"{self.instance.swimlane.host}/record/{results.get('application_id')}/{results.get('id')}",
                        display=results.get('json').get('Tracking Id')
                    )
                )
            else:
                for key,val in results.items():
                    if not key.startswith('$') and val:
                        button_list.append(f':white_check_mark: \t{key}')
                    elif not key.startswith('$') and not val:
                        button_list.append(f':x: \t{key}')
        card.buttons = button_list
        card = HeroCard(
            title="Swimlane", text=caller, buttons=card.buttons
        )
        return MessageFactory.attachment(CardFactory.hero_card(card))

    def build(self, results, application_id=None, record_id=None):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        method_name = calframe[1][3]
        self.__logger.info(f'Creating format block for {method_name}')
        return self._build_card(method_name=method_name, results=results, application_id=application_id, record_id=record_id)
