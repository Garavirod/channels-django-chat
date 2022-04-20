from django.urls import path
from . import consumers

websocket_url_patterns = [
    path('ws/chat/room/<room_id>', consumers.ChatConsumer.as_asgi())
]