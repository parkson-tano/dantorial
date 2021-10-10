from django.urls import path
from mainapp.views import *
from category.views import *
from .views import MessageView
app_name = 'dantorial_message'
urlpatterns = [
	path('', MessageView.as_view(), name='message'),
]