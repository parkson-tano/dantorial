from django.urls import path
from mainapp.views import *
from category.views import *
from .views import MessageView, ChatView
from mainapp.views import UserProfileView as up
app_name = 'dantorial_message'
urlpatterns = [
	path('', ChatView.as_view(), name='chat'),
	path('chat/<int:pk>', MessageView.as_view(), name='message'),
	path('chat/send/', up.as_view(), name='send'),
]