from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, View
from django.contrib import messages
from .forms import MessageForm
from .models import Message, Chat
from django.db.models import Count
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from messaging.forms import MessageForm
from django.urls import reverse_lazy, reverse
class ChatView(TemplateView):
	template_name = 'main/chat.html'
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			pass
		else:
			return redirect('/accounts/login/?next=/message/')
		return super().dispatch(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		profile = self.request.user
		chat = Chat.objects.filter(Q(user=profile) | Q(receiver=profile))
		context['chats'] = chat
		return context
class MessageView(TemplateView):
	template_name = 'main/message.html'
	# context_object_name = 'mess'
	# model = Message

	def dispatch(self, request, *args, **kwargs):
		url_id = kwargs['pk']
		profile = self.request.user
		chat = Chat.objects.get(id=url_id)
		if request.user.is_authenticated and (chat.user == profile or chat.receiver == profile):
			pass
		else:
			return redirect('/accounts/login/?next=/message/')
		return super().dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		url_id = kwargs['pk']
		profile = self.request.user
		chat = Chat.objects.get(id=url_id)
		message = Message.objects.filter(Q(chat=url_id) & (Q(sender_user=profile) | Q(receiver_user=profile))).order_by('-date_created')
		# out = Message.objects.filter(receiver_user=profile).order_by('-date_created')
		for mess in message:
			if self.request.user == mess.receiver_user:
				if self.request.user != mess.sender_user:
					mess.is_read = True
					mess.save()
				else:
					pass
			chats_id = mess.chat.id
		context['chat'] = url_id
		context["message"] = message
		return context
		# context['out'] = out
		
		
class SendView(View):
    def post(self, request, *args, **kwargs):
    	url_id = self.kwargs['pk']
    	msg = request.POST.get('message')
    	user = request.user
    	print(msg)
    	print(user)
    	print(url_id)
    	print('helloooooo')
    	c = Chat.objects.get(id=url_id)
    	if c.receiver == request.user:
    		receiver = c.user
    	else:
    		receiver = c.receiver
    	new_message = Message(chat = c, sender_user = self.request.user,
                receiver_user = receiver,
                message = msg,
                )
    	new_message.save()
    	print('saved')
    	return redirect(f'/message/chat/{url_id}')