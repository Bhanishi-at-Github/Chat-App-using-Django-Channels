'''
Consumer file for chat app

'''
# Chat app consumers

import json
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

# class TestAsyncConsumer(AsyncConsumer):

#     async def websocket_connect(self, event):
#         print('connected', event)

#         # Add channels to a existing group

#         self.channel_layer.group_add(
#             'Test_Group', 
#             self.channel_name
#         )

#         await self.send({
#             'type': 'websocket.accept'
#         })

#     async def websocket_receive(self, event):
#         print('receive', event['text'])

#         await self.channel_layer.group_send(
#         'Test_Group',
#         {
#             'type': 'chat_message',
#             'message': event['text']
#         }
#     )

#     async def chat_message(self, event):
#         print('message...', event['message'])

#     # Send the message to the WebSocket
#         await self.send(text_data=event['message'])



#     async def websocket_disconnect(self, event):
#         print('disconnected', event)

#         self.channel_layer.group_discard(
#             'Test_Group', 
#             self.channel_name
#         )

#         raise StopConsumer


class ChatConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print('connected', event)

        # Add channels to a existing group

        async_to_sync (self.channel_layer.group_add)(
            'Test_Group', 
            self.channel_name
        )

        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print('receive', event['text'])

        async_to_sync (self.channel_layer.group_send)(
        'Test_Group',
        {
            'type': 'chat.message',
            'text': event['text']
        }
    )
    
    def chat_message(self, event):

        print('message...', event['text'])

        self.send({
            'type': 'websocket.send',
            'text': event['text']
        })

    # Send the message to the WebSocket
        

        
