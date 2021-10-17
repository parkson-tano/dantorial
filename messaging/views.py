from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView
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

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		profile = self.request.user
		chat = Chat.objects.filter(Q(user=profile) | Q(receiver=profile))
		context['chats'] = chat
		return context
class MessageView(TemplateView):
	template_name = 'main/message.html'
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			pass
		else:
			return redirect('/accounts/login/?next=/message/')
		return super().dispatch(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		url_id = kwargs['pk']
		profile = self.request.user
		message = Message.objects.filter(Q(chat=url_id) & (Q(sender_user=profile) | Q(receiver_user=profile))).order_by('-date_created')
		# out = Message.objects.filter(receiver_user=profile).order_by('-date_created')
		for mess in message:
			if self.request.user == mess.receiver_user:
				if self.request.user != mess.sender_user:
					mess.is_read = True
					mess.save()
				else:
					pass
		context["message"] = message
		# context['out'] = out
		return context

# def contactView(request):
#     if request.method == 'GET':
#         form = MessageForm()
#     else:
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             if (user.is_authenticated):
#                 sender_user = request.user
#                 receiver_user = self.get_object().user
 
#             message = form.cleaned_data['message']
     
#             return redirect('success')
#     return render(request, "userprofile.html", {'message': form})

class SendView(View):
    def post(self, request, pk, *args, **kwargs):
        form = MessageForm(request.POST)
        thread = Chat.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver

        if form.is_valid():
            message = form.save(commit=False)
            message.chat = thread
            message.sender_user = request.user
            message.receiver_user = receiver
            message.save()
        return redirect('thread', pk=pk)