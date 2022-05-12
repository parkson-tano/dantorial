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
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.http.response import JsonResponse
import json

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
		message = Message.objects.filter(Q(chat=url_id) & (Q(sender_user=profile) | Q(receiver_user=profile))).order_by('date_created')
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

def send_message(request):
    if request.POST.get('action') == 'post':
        chatid = int(request.POST.get('chat_id'))
        u = Chat.objects.get(id=chatid)
        print(f'prof id {chatid}')
        message_obj = Message.objects.filter(chat=chatid)
        print(f"prof obj {message_obj} ")
        return JsonResponse({'message': message_obj})
    return HttpResponse("Error access Denied by")

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


# @login_required
# def chatroom(request, pk:int):
#     other_user = get_object_or_404(User, pk=pk)
#     messages = Message.objects.filter(
#         Q(receiver=request.user, sender=other_user)
#     )
#     messages.update(seen=True)
#     messages = messages | Message.objects.filter(Q(receiver=other_user, sender=request.user) )
#     return render(request, "chatroom1.html", {"other_user": other_user, 'users': User.objects.all(), "user_messages": messages})


# @login_required
# def ajax_load_messages(request, pk):
#     other_user = get_object_or_404(User, pk=pk)
#     messages = Message.objects.filter(seen=False, receiver=request.user)
    
#     print("messages")
#     message_list = [{
#         "sender": message.sender.username,
#         "message": message.message,
#         "sent": message.sender == request.user,
#         "picture": other_user.profile.picture.url,

#         "date_created": naturaltime(message.date_created),

#     } for message in messages]
#     messages.update(seen=True)
    
#     if request.method == "POST":
#         message = json.loads(request.body)['message']
        
#         m = Message.objects.create(receiver=other_user, sender=request.user, message=message)
#         message_list.append({
#             "sender": request.user.username,
#             "username": request.user.username,
#             "message": m.message,
#             "date_created": naturaltime(m.date_created),

#             "picture": request.user.profile.picture.url,
#             "sent": True,
#         })
#     print(message_list)
#     return JsonResponse(message_list, safe=False)