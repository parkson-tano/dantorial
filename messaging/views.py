from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import MessageForm
from .models import Message

class MessageView(TemplateView):
	template_name = 'main/message.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		url_pk = kwargs['pk']
		message = Message.objects.filter(sender_user=url_pk)
		out = Message.objects.filter(receiver_user=url_pk)
		context["message"] = message
		context['out'] = out
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

	
