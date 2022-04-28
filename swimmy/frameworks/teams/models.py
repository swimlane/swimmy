from typing import (
    List,
    AnyStr
)
from attr import (
    define,
    field,
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
