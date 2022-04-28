from cgitb import text
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
from pendulum import local_timezone
from ..formatter import FormatterBase

from typing import (
    List,
    AnyStr
)
from attr import (
    define,
    field,
    asdict
)


@define
class Button:
    displayText: AnyStr = field(default=None)
    title: AnyStr = field(default=None)
    type: AnyStr = field(default='openUrl')
    value: AnyStr = field(default=None)


@define 
class Content:
    buttons: List[Button] = field(default=[])
    text: AnyStr = field(default=None)
    title: AnyStr = field(default='Swimlane')


@define
class Attachment:
    content: Content = field(default={})
    content_type: AnyStr = field(default='application/vnd.microsoft.card.hero')


@define
class TeamsMessage:
    attachment_layout: AnyStr = field(default='list')
    attachments: List[Attachment] = field(default=[])
    type: AnyStr = field(default='message')
    additional_properties: dict = field(default={})
    id: AnyStr = field(default=None)
    timestamp: AnyStr = field(default=None)
    local_timestamp: AnyStr = field(default=None)
    local_timezone: AnyStr = field(default=None)
    service_url: AnyStr = field(default=None)
    channel_id: AnyStr = field(default=None)
    from_property: AnyStr = field(default=None)
    conversation: AnyStr = field(default=None)
    recipient: AnyStr = field(default=None)
    text_format: AnyStr = field(default=None)
    members_added: AnyStr = field(default=None)
    members_removed: AnyStr = field(default=None)
    reactions_added: AnyStr = field(default=None)
    reactions_removed: AnyStr = field(default=None)
    topic_name: AnyStr = field(default=None)
    history_disclosed: AnyStr = field(default=None)
    locale: AnyStr = field(default=None)
    text: AnyStr = field(default=None)
    speak: AnyStr = field(default=None)
    input_hint: AnyStr = field(default=None)
    summary: AnyStr = field(default=None)
    suggested_actions: AnyStr = field(default=None)
    entities: AnyStr = field(default=None)
    channel_data: AnyStr = field(default=None)
    action: AnyStr = field(default=None)
    reply_to_id: AnyStr = field(default=None)
    label: AnyStr = field(default=None)
    value_type: AnyStr = field(default=None)
    value: AnyStr = field(default=None)
    name: AnyStr = field(default=None)
    relates_to: AnyStr = field(default=None)
    code: AnyStr = field(default=None)
    expiration: AnyStr = field(default=None)
    importance: AnyStr = field(default=None)
    delivery_mode: AnyStr = field(default=None)
    listen_for: AnyStr = field(default=None)
    text_highlights: AnyStr = field(default=None)
    semantic_action: AnyStr = field(default=None)
    caller_id: AnyStr = field(default=None)


{
    'attachment_layout': 'list',
    'attachments': [
        {
            'content': {
                'buttons': [
                    {
                        'displayText': 'Content Migration',
                        'title': 'Content Migration',
                        'type': 'openUrl',
                        'value': 'https://10.32.100.207/workspace/aLgSvwSD75XVuHf26/'
                    },
                    {
                        'displayText': 'QuickStart Record Generator',
                        'title': 'QuickStart Record Generator',
                        'type': 'openUrl',
                        'value': 'https://10.32.100.207/workspace/aBK9FOKTjdrRiIzhe/'
                    },
                    {'displayText': 'Swimlane '
                                    'Administrator',
                    'title': 'Swimlane Administrator',
                    'type': 'openUrl',
                    'value': 'https://10.32.100.207/workspace/aWjKAbBILwr2DSm7V/'},
                    {'displayText': 'Swimlane Analyst',
                    'title': 'Swimlane Analyst',
                    'type': 'openUrl',
                    'value': 'https://10.32.100.207/workspace/aWPNWzhWf52XWebZF/'},
                    {'displayText': 'Swimlane Domain '
                                    'Squatting',
                    'title': 'Swimlane Domain Squatting',
                    'type': 'openUrl',
                    'value': 'https://10.32.100.207/workspace/aX2GpCg42neXvGwgl/'},
                    {'displayText': 'Swimlane Health & '
                                    'Maintenance '
                                    'Operations',
                    'title': 'Swimlane Health & '
                            'Maintenance Operations',
                    'type': 'openUrl',
                    'value': 'https://10.32.100.207/workspace/aDNTJW4f9suXDsXIJ/'},
                    {'displayText': 'Swimlane Record '
                                    'Retention',
                    'title': 'Swimlane Record Retention',
                    'type': 'openUrl',
                    'value': 'https://10.32.100.207/workspace/aBnypDKy5igHGwkAA/'},
                    {'displayText': 'Test App Workspace',
                    'title': 'Test App Workspace',
                    'type': 'openUrl',
                    'value': 'https://10.32.100.207/workspace/aZF9Nrtq0qK3GSmQp/'},
                    {'displayText': 'Test App Workspace',
                    'title': 'Test App Workspace',
                    'type': 'openUrl',
                    'value': 'https://10.32.100.207/workspace/aNJfvGLA7Q6j5_67B/'},
                    {'displayText': 'Test Application '
                                    'Workspace',
                    'title': 'Test Application '
                            'Workspace',
                    'type': 'openUrl',
                    'value': 'https://10.32.100.207/workspace/aT71mmdcu9C3QZ4bc/'}
                    ],
                'text': 'Workspaces',
                'title': 'Swimlane'
            },
            'content_type': 'application/vnd.microsoft.card.hero'
        }
    ],
 'type': 'message'}

{
    'type': 'message', 
    'attachment_layout': 'list', 
    'attachments': [
        {
            'content_type': 'application/vnd.microsoft.card.hero', 
            'content': {
                'title': 'Swimlane', 
                'text': 'Record', 
                'buttons': [
                    {'type': 'openUrl', 
                    'title': 'SAIM-1 (aeT_QXNCZ0C4XFMZt)\nCreated: 2022-02-28T19:25:52.603000+00:00\nLast Modified: 2022-02-28T23:30:14.245000+00:00', 
                    'displayText': 'SAIM-1', 
                    'value': 'https://10.32.100.207/record/a5V3YYzGQuQen5Hen/aeT_QXNCZ0C4XFMZt'}
                ]
            }
        }
    ]
}


class TeamsFormatter(FormatterBase):

    def _create_button(self, title, value, display):
        return CardAction(
            type=ActionTypes.open_url,
            title=title,
            value=value,
            display_text=display
        )

    def _build_button(self, item, method_name):
        try:
            endpoint = self.ENDPOINT_MAP.get(method_name).substitute(
                id=item.get('id'), 
                default_report_id=item.get('default_report_id')
            )
            url = f"{self.instance.swimlane.host}/{endpoint}/"
        except:
            url = None
            pass
        text = item.get('name')
        display_text = text
       # url = f"{self.instance.swimlane.host}/{endpoint}/"
        if item.get('json') and item['json'].get('Tracking Id'):
            text =f"{item.get('json').get('Tracking Id')} ({item.get('id')})\nCreated: {item.get('created')}\nLast Modified: {item.get('modified')}"
            url=f"{self.instance.swimlane.host}/record/{item.get('application_id')}/{item.get('id')}",
            display_text=item.get('json').get('Tracking Id')
        if method_name == 'get_application_tasks':
            display_text = f"{item.get('name')}\n{item.get('description')}"
        if item.get('url') and item.get('text'):
            text = item['text']
            url = item['url']
        if item.get('vendor') and item.get('product'):
            text = f"{item.get('vendor')} {item.get('product')} ({item.get('version')})\n{item.get('description')}"
        if item.get('pythonVersion'):
            text = f"{item['name']} ({self.VERSION_MAP.get(item['pythonVersion'])}) {item['version']}\n{item['summary']}\n{item['homePage']}"
        return Button(
            displayText=display_text,
            title=text,
            value=url
        )

    def parse_lists(self, results, application_id=None):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        method_name = calframe[1][3]
        self.__logger.info(f'Creating format block for {method_name}')
        button_list = []
        content = Content(
            text=method_name.rsplit('_',1)[-1].capitalize()
        )
        if results and isinstance(results, list):
            for item in results:
                button_list.append(
                    self._build_button(
                        item=item,
                        method_name=method_name
                    )
                )
        elif results and isinstance(results, dict):
            text = ''
            for key,val in results.items():
                if not key.startswith('$') and val:
                    button_list.append(f':white_check_mark: \t{key}')
                elif not key.startswith('$') and not val:
                    button_list.append(f':x: \t{key}')
        content.buttons = button_list
        attachment = Attachment(content=content)
        return TeamsMessage(attachments=[attachment])

    def parse_record(self, results):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        method_name = calframe[1][3]
        self.__logger.info(f'Creating format block for {method_name}')
        content = Content(
            text=method_name.rsplit('_',1)[-1].capitalize()
        )
        content.buttons.append(
            self._build_button(results, method_name)
        )
        print(content.buttons)
        return TeamsMessage(
            attachments=[Attachment(content=content)]
        )
        card = BasicCard()
        card.title = 'Swimlane'
        card.subtitle = 'Record'
        button_list = []
        button_list.append(
            self._create_button(
                title=f"{results.get('json').get('Tracking Id')} ({results.get('id')})\nCreated: {results.get('created')}\nLast Modified: {results.get('modified')}",
                value=f"{self.instance.swimlane.host}/record/{results.get('application_id')}/{results.get('id')}",
                display=results.get('json').get('Tracking Id')
            )
        )
        card.buttons = button_list
        card = HeroCard(
            title="Swimlane", text='Record', buttons=card.buttons
        )
        print(card.as_dict())
        temp = MessageFactory.attachment(CardFactory.hero_card(card))
        import pprint
        pprint.pprint(temp.as_dict())
        return temp

    def new_record(self, record_id):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        method_name = calframe[1][3]
        self.__logger.info(f'Creating format block for {method_name}')
        card = BasicCard()
        card.title = 'Swimlane'
        card.subtitle = 'Record'
        button_list = []
        endpoint = self.ENDPOINT_MAP.get(method_name).substitute(id=record_id)
        button_list.append(
            self._create_button(
                title=f"New Swimlane Record",
                value=f"{self.instance.swimlane.host}/{endpoint}/",
                display="New Swimlane Record"
            )
        )
        card.buttons = button_list
        card = HeroCard(
            title="Swimlane", text='Record', buttons=card.buttons
        )
        return MessageFactory.attachment(CardFactory.hero_card(card))
