from django.urls import path
from mainapp.views import *
from category.views import *
from .views import MessageView, ChatView
app_name = 'dantorial_message'
urlpatterns = [
	path('', ChatView.as_view(), name='chat'),
	path('message', MessageView.as_view(), name='message'),
]