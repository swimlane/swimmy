from .base import Base
from .config import Config


class Messaging(Base):
    """Constructs messages sent as response"""

    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self):
        self.__header = {}
        self.__sections = []
        self.__actions = []
        self.username = Config.slack['bot_username']

    def add_header(self, text):
        self.__header = {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": text
            }
        }

    def create_accessory(self, type, url, text=None):
        if type == 'image':
            return {
                    "type": "image",
                    "image_url": url
                }
        elif type == 'button':
            return {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": text,
                    "emoji": True
                },
                "url": url,
            }

    def add_markdown_section(self, text='We are unable to process your request.', accessory={}):
        if accessory:
            self.__sections.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": text
                },
                "accessory": accessory
            })
        else:
            self.__sections.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": text
                }
            })

    def add_button_action_element(self, text, url):
        self.__actions.append({
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": text,
                "emoji": True,
            },
            "url": url
        })

    def get_action_elements(self):
        if self.__actions:
            return {
                "type": "actions",
                "elements": self.__actions
            }
        else:
            return {}


    def get_blocks(self):
        actions = self.get_action_elements()
        if actions:
            return [
                self.__header,
                self.DIVIDER_BLOCK,
                *self.__sections,
                self.DIVIDER_BLOCK,
                actions
            ]
        else:
            return [
                self.__header,
                self.DIVIDER_BLOCK,
                *self.__sections,
                self.DIVIDER_BLOCK,
            ]
