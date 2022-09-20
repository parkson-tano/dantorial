from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/chat/personal/(?P<id>\d+)/$',
            consumers.PersonalChatConsumer.as_asgi()),
]
