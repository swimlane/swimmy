from io import BytesIO

import requests

from ...base import Base


class TeamsActions(Base):

    def submit_attachments(self, attachments):
        record_list = []
        if self.config.action_config:
            for app in self.config.action_config.get('eml'):
                pt = self.swimlane.swimlane.apps.get(name=app['name'])
                for attachment in attachments:
                    record = pt.records.create()
                    record['Attachments'].add(attachment.name, BytesIO(requests.get(attachment.content_url).content))
                    record.save()
                    record_list.append(record['Tracking Id'])
        return record_list
