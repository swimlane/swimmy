from botbuilder.core import (
    ActivityHandler, 
    MessageFactory, 
    TurnContext
)
from botbuilder.schema import ChannelAccount
from .actions import TeamsActions
from ..actions import FrameworkActions


class TeamsBot(ActivityHandler):

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

    async def on_message_activity(self, turn_context: TurnContext):
        TurnContext.remove_recipient_mention(turn_context.activity)
        if turn_context.activity.text:
            text = turn_context.activity.text.strip().lower()
            resp = FrameworkActions().parse(text)
            if resp:
                resp.id = turn_context.activity.reply_to_id
                return await turn_context.send_activity(resp)
        if turn_context.activity.attachments:
            record_list = TeamsActions().submit_attachments(turn_context.activity.attachments)
            if record_list:
                return await turn_context.send_activity(
                    MessageFactory.text(f"We have submitted these attachments to Swimlane: {record_list}")
                )
