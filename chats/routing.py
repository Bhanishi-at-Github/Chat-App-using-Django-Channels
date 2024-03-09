'''
Routing for chat app
'''

from django.urls import path
from chats import consumers


websocket_urlpatterns = [
    # path(r'ws/test/', consumers.TestConsumer.as_asgi()),
    path(r'ws/testasync/', consumers.ChatConsumer.as_asgi()),
]
