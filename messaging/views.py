from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views import View
from django.contrib import messages
# def contactView(request):
#     if request.method == 'GET':
#         form = messagingForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             if (user.is_authenticated):
#                 sender_user = request.user
#                 receiver_user = 
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['admin@example.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "userprofile.html", {'form': form})

# def successView(request):
#     return HttpResponse('Success! Thank you for your message.')

