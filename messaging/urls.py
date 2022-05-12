from django.urls import path
from mainapp.views import *
from category.views import *
from .views import MessageView, ChatView, SendView, send_message
from mainapp.views import UserProfileView as up
app_name = 'dantorial_message'
urlpatterns = [
	path('', ChatView.as_view(), name='chat'),
	path('chat/<int:pk>', MessageView.as_view(), name='message'),
	path('chat/send/<int:pk>/', SendView.as_view(), name='send'),
	path('refresh/', send_message, name='refresh'),
	# path("ajax/<int:pk>/", views.ajax_load_messages, name="chatroom-ajax"),
]