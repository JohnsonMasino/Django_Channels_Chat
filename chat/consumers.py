import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from .models import Messaging

# ChatConsumer class
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'chat_room'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    # Disconnect from the websocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message 
        }))

    @database_sync_to_async
    def delete_message(self, message_id):
        try:
            message = Messaging.objects.get(id=message_id)
            message.delete()
        except Messaging.DoesNotExist:
            pass
        except Exception as e:
            print(e)
        