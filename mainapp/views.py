import http
from time import time
import json
import requests
import jwt
from django.template.loader import render_to_string, get_template
from django.utils.datastructures import MultiValueDictKeyError
from django.core.cache import cache
from io import SEEK_CUR
import re
import datetime
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View, ListView, FormView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from requests.api import request
from .models import *
from django.utils.decorators import method_decorator
from django.http import Http404
from category.models import Category, SubCategory
from .forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, PasswordResetForm
from django.core.paginator import Paginator
from django.db.models import Q
from location.models import Country, Region, Town, Quater
from itertools import chain
from review.models import Review
from review.forms import ReviewForm
from allauth.account.admin import EmailAddress
from messaging.models import Message, Contact, Chat
from messaging.forms import MessageForm, ContactForm
# Create your views here.
from django.core.mail import send_mail
from django.conf import Settings, settings
from campay.sdk import Client
from django.http import JsonResponse
from django.db.models import Avg
from django.utils.translation import gettext as _

import random
import os
from dotenv import load_dotenv
load_dotenv()


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = Country.objects.all()
        pro = ProfilePersonal.objects.all()
        pro_info = ProfileInfo.objects.all()
        category = Category.objects.all()
        context['category'] = category
        context['pro'] = pro
        context['pro_info'] = pro_info
        return context


class MyAccount(TemplateView):
    template_name = 'main/my_account.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/myaccount/')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prof = ProfilePersonal.objects.get(user=self.request.user)
        userEmail = EmailAddress.objects.get(user=self.request.user)
        context['auth'] = userEmail
        context['prof'] = prof
        return context


class UserProfileView(DetailView):
    template_name = 'main/userprofile.html'
    context_object_name = 'userprofile'
    model = ProfilePersonal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments_connected = Review.objects.select_related().filter(
            profile=self.get_object()).order_by('-date_created')
        user_rating = Review.objects.select_related().filter(
            profile=self.get_object()).aggregate(Avg('rating'))
        similar = ProfilePersonal.objects.select_related().filter(Q(user__profileinfo__subject=self.get_object().user.profileinfo.subject)
                                                                  | Q(user__profileinfo__subcategory=self.get_object().user.profileinfo.subcategory)
                                                                  | Q(user__profileinfo__category=self.get_object().user.profileinfo.category))
        pro = ProfilePersonal.objects.select_related().filter(paid=True)
        context["comments"] = comments_connected
        context['comment_form'] = ReviewForm
        context['message'] = MessageForm
        context['similar'] = similar
        context['prof'] = pro

        ur = user_rating['rating__avg']
        urr = str(ur)

        context['ur'] = urr[:3]
        print(ur)
        prof = ProfilePersonal.objects.get(
            user__username=self.get_object().user)
        if self.request.user.is_authenticated:
            if (self.request.user != self.get_object().user):
                new_view = ProfileViewed.objects.create(
                    user=self.get_object().user, viewed_by=self.request.user)
                prof.view_count += 1
                prof.save()

                if send_mail:
                    print('email sent')
            else:
                pass
        # new_view.save()
        else:
            if (self.request.user != self.get_object().user):
                new_view = ProfileViewed.objects.create(
                    user=self.get_object().user,)
                prof.view_count += 1
                prof.save()
            else:
                pass

        return context

    def post(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            new_comment = Review(content=request.POST.get('content'),
                                 rating=request.POST.get('rate'),
                                 profile=self.get_object(),
                                 user=self.request.user)

            if (Chat.objects.filter(user=self.request.user, receiver=self.get_object().user).exists()) or (Chat.objects.filter(receiver=self.request.user, user=self.get_object().user).exists()):
                ch = Chat.objects.get(Q(user=self.request.user, receiver=self.get_object(
                ).user) | Q(receiver=self.request.user, user=self.get_object().user))
                if ch.receiver == request.user:
                    receiver = ch.user
                else:
                    receiver = ch.receiver
                new_message = Message(chat=ch, sender_user=self.request.user,
                                      receiver_user=receiver,
                                      message=request.POST.get('message'),
                                      )
            else:
                new_chat = Chat(user=self.request.user,
                                receiver=self.get_object().user)
                new_message = Message(chat=new_chat, sender_user=self.request.user,
                                      receiver_user=self.get_object().user,
                                      message=request.POST.get('message'),
                                      )
                new_chat.save()
        else:
            return redirect(f'/accounts/login/?next=/userprofile/{self.get_object().id}')

        if 'post_schedule' in request.POST:

            new_schedule.save()

        if 'post_comment' in request.POST:
            new_comment.save()

        elif 'send_message' in request.POST:
            ctx = {
                'user': self.request.user.profilepersonal.first_name
            }
            new_message.save()
            subject = 'Message from Tantorial User'
            html_message = render_to_string('email/mail.html', {
                'user': self.request.user.profilepersonal.first_name,
                'id': self.request.user.profilepersonal.id,
                'asd': request.get_host()
            })
            message = f'{self.request.user.profilepersonal.first_name} sent you a messages'
            from_email = settings.EMAIL_HOST_USER
            to_email = (self.get_object().user.email,)

            send_mail(subject, message, from_email, to_email,
                      fail_silently=False, html_message=html_message)
            print(f'email sent: {to_email}')
            messages.success(self.request, 'message successfully sent')
        elif 'send_message' in request.GET:

            new_message.save()
            subject = 'Message from Tantorial User'
            message = f'{self.request.user.profilepersonal.first_name} sent you a messages'
            from_email = settings.EMAIL_HOST_USER
            to_email = (self.get_object().user.email,)

            send_mail(subject, message, from_email,
                      to_email, fail_silently=True)
            print(f'email sent: {to_email}')
        return self.get(self, request, *args, **kwargs)


class AboutView(TemplateView):
    template_name = 'main/about_us.html'


class PrivacyView(TemplateView):
    template_name = 'main/privacy_policy.html'


class TermsView(TemplateView):
    template_name = 'main/terms.html'


class ContactView(CreateView):
    template_name = 'main/contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('dantorial:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "We will get back to you shortly")
        subject = "Thanks for contacting us"
        message = f'{form.instance.first_name} thanks for contacting us'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = (form.instance.email, )

        send_mail(subject, message, from_email, to_email, fail_silently=True)
        form.save()
        return super().form_valid(form)


class UserRegistrationView(CreateView):
    template_name = 'main/signup.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('dantorial:index')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return super().form_valid(form)


class PersonalProfileEditView(UpdateView):
    template_name = 'main/edit_profile.html'
    form_class = PersonalProfileForm
    success_url = reverse_lazy('dantorial:profile')
    model = ProfilePersonal

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/profile/')

        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user.profilepersonal
        else:
            pass

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(self.request.user.profilepersonal.account_type)
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)


class ProfileView(TemplateView):
    template_name = 'main/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        profile_info = ProfilePersonal.objects.get(user=profile)
        context["profile"] = profile_info
        return context


class ProfileInfoView(TemplateView):
    template_name = 'main/profile_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        profile_info = ProfileInfo.objects.get(user=profile)
        context["profile_info"] = profile_info
        return context


class ProfileQualificationView(TemplateView):
    template_name = 'main/my_qualification.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = self.request.user
        context["account"] = account

        qualification = Qualification.objects.select_related().filter(
            user=account).order_by('-id')
        context['qualification'] = qualification
        return context


class ProfileExperienceView(TemplateView):
    template_name = 'main/my_experience.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = self.request.user
        context["account"] = account

        experience = Experience.objects.filter(user=account).order_by('-id')
        context['experience'] = experience
        return context


class ProfileInfoEditView(UpdateView):
    template_name = 'main/edit_prof_profile.html'
    form_class = ProfileInfoForm
    success_url = reverse_lazy('dantorial:profile-info')
    model = ProfileInfo

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/profile-info/')

        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return self.request.user.profileinfo

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)


class SubjectAddView(CreateView):
    template_name = 'main/add_subject.html'
    form_class = AddSubjectForm
    success_url = reverse_lazy('dantorial:my-subject')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/add-availability/')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Subject Added Successfully")
        form.save()
        return super().form_valid(form)


class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = reverse_lazy('dantorial:my-subject')

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, 'sucessfully removed subject')
        return super().delete(request, *args, **kwargs)


class AvailabilityAddView(CreateView):
    template_name = 'main/add_availability.html'
    form_class = AvailabilityForm
    success_url = reverse_lazy('dantorial:my-availability')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/add-availability/')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Availability Added Successfully")
        form.save()
        return super().form_valid(form)


class AvailabilityDeleteView(DeleteView):
    model = Availability
    success_url = reverse_lazy('dantorial:my-availability')

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, 'availability removed subject')
        return super().delete(request, *args, **kwargs)


class AvailabilityUpdateView(UpdateView):
    template_name = 'main/update_availability.html'
    form_class = AvailabilityForm
    model = Availability
    success_url = reverse_lazy('dantorial:my-availability')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/my-availability/')

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Availability.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)


class ProfileAvailabilityView(TemplateView):
    template_name = 'main/my_availability.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/my-availability/')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = self.request.user
        context["account"] = account

        availability = Availability.objects.filter(
            user=account).order_by('-id')
        context['availability'] = availability
        return context


class ExperienceAddView(CreateView):
    template_name = 'main/add_experience.html'
    form_class = AddExperienceForm
    success_url = reverse_lazy('dantorial:my-experience')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)


class ExperienceDeleteView(DeleteView):
    model = Experience
    success_url = reverse_lazy('dantorial:my-experience')

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, 'sucessfully removed experience')
        return super().delete(request, *args, **kwargs)


class QualificationAddView(CreateView):
    template_name = 'main/add_qualification.html'
    form_class = AddQualificationForm
    success_url = reverse_lazy('dantorial:my-qualification')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/add-qualification/')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)


class QualificationDeleteView(DeleteView):
    model = Qualification
    success_url = reverse_lazy('dantorial:my-qualification')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'sucessfully removed Qualification')
        return super().delete(request, *args, **kwargs)


class ProfileDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('dantorial:index')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'sucessfully removed Profile')
        return super().delete(request, *args, **kwargs)


class QualificationUpdateView(UpdateView):
    template_name = 'main/update_qualification.html'
    form_class = AddQualificationForm
    model = Qualification
    success_url = reverse_lazy('dantorial:my-qualification')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/my-qualification/')

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Qualification.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)


class ExperienceUpdateView(UpdateView):
    template_name = 'main/update_experience.html'
    form_class = AddExperienceForm
    model = Experience
    success_url = reverse_lazy('dantorial:my-experience')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/my-experience/')

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Experience.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)


class SubjectUpdateView(UpdateView):
    template_name = 'main/update_subject.html'
    form_class = AddSubjectForm
    model = Subject
    success_url = reverse_lazy('dantorial:my-subject')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if Subject.user == self.request.user:
                pass
        else:
            return redirect('/accounts/login/?next=/my-subject/')

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Subject.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)


class ProfileSubjectView(TemplateView):
    template_name = 'main/my_subject.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/my-subject/')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = self.request.user
        context["account"] = account

        subject = Subject.objects.filter(user=account).order_by('-id')
        context['subject'] = subject
        return context


class VerificationAddView(CreateView):
    template_name = 'main/add_verification.html'
    model = Verification
    form_class = VerificationForm
    success_url = reverse_lazy('dantorial:my-verification')

    def dispatch(self, request, *args, **kwargs):
        if Verification.objects.filter(user=self.request.user).exists():
            return redirect('dantorial:my-verification')
        else:
            pass

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)


class VerificationDeleteView(DeleteView):
    model = Verification
    success_url = reverse_lazy('dantorial:my-verification')


class VerificationUpdateView(UpdateView):
    template_name = 'main/update_verification.html'
    form_class = VerificationForm
    model = Verification
    success_url = reverse_lazy('dantorial:my-verification')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)


class ProfileVerificationView(TemplateView):
    template_name = 'main/my_verification.html'

    def dispatch(self, request, *args, **kwargs):
        if Verification.objects.filter(user=self.request.user).exists():
            pass
        else:
            return redirect('dantorial:add-verification')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = self.request.user
        context["account"] = account

        verification = Verification.objects.get(user=account)
        context['verify'] = verification
        return context


class UserLoginView(FormView):
    template_name = 'main/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('dantorial:index')

    def form_valid(self, form):
        uname = form.cleaned_data.get('username')
        pword = form.cleaned_data.get('password')
        usr = authenticate(username=uname, password=pword)
        if usr is not None and ProfilePersonal.objects.filter(user=usr).exists():
            login(self.request, usr,
                  backend='django.contrib.auth.backends.ModelBackend')
        else:
            return render(self.request, self.template_name, {'form': self.form_class, 'error': 'invalid creditials'})
        return super().form_valid(form)

    def get_success_url(self):
        if 'next' in self.request.GET:
            next_url = self.request.GET.get('next')
            print(next_url)
            return next_url
        else:
            return self.success_url


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('dantorial:index')


class SearchView(TemplateView):
    template_name = 'main/search_all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        acc_type = self.request.GET['typ']

        try:
            subject = self.request.GET['subject']
        except MultiValueDictKeyError:
            subject = None
        category = self.request.GET['category']
        region = self.request.GET['region']
        try:
            town = self.request.GET['town']
        except MultiValueDictKeyError:
            town = None

        if subject is None and town is None:
            profile_result = ProfilePersonal.objects.filter(Q(account_type=acc_type) & Q(
                region=region) & Q(user__profileinfo__category=category))

        elif subject is None:
            profile_result = ProfilePersonal.objects.filter(Q(account_type=acc_type)).filter(
                Q(region=region)).filter(Q(town=town) & Q(user__profileinfo__category=category))
        elif town is None:
            profile_result = ProfilePersonal.objects.filter(Q(account_type=acc_type)).filter(
                Q(region=region) & Q(user__profileinfo__category=category) & Q(user__profileinfo__subject=subject))
        else:
            profile_result = ProfilePersonal.objects.filter(Q(account_type=acc_type)).filter(Q(region=region)).filter(
                Q(town=town) & Q(user__profileinfo__category=category) & Q(user__profileinfo__subject=subject))
        if self.request.user.is_authenticated:
            fav = ProfilePersonal.objects.get(
                id=self.request.user.profilepersonal.id)
            context['fav'] = fav
        print(profile_result)
        context['result'] = profile_result
        return context


class FilterView(TemplateView):
    template_name = 'main/search_all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        acc_type = self.request.GET['typ']
        category = self.request.GET['category']
        charge = self.request.GET['charge']
        gender = self.request.GET['gender']
        education = self.request.GET['education']
        region = self.request.GET['region']

        try:
            town = self.request.GET['town']
        except MultiValueDictKeyError:
            town = None

        try:
            subject = self.request.GET['subject']
        except MultiValueDictKeyError:
            subject = None
        user_obj = User.objects.all()

        if subject is None and town is None:
            profile_result = ProfilePersonal.objects.filter(Q(account_type=acc_type)).filter(Q(region=region) & Q(gender=gender) & Q(
                level_of_education=education) & Q(user__profileinfo__category=category) & Q(user__profileinfo__charge=charge))

        elif subject is None:

            profile_result = ProfilePersonal.objects.filter(Q(account_type=acc_type)).filter(Q(region=region) | Q(town=town) & Q(
                gender=gender) & Q(level_of_education=education) & Q(user__profileinfo__category=category) & Q(user__profileinfo__charge=charge))

        elif town is None:
            profile_result = ProfilePersonal.objects.filter(Q(account_type=acc_type)).filter(Q(region=region) & Q(gender=gender) & Q(level_of_education=education) & Q(user__profileinfo__category=category)
                                                                                             & Q(user__profileinfo__subject=subject) & Q(user__profileinfo__charge=charge))
        else:
            profile_result = ProfilePersonal.objects.filter(Q(account_type=acc_type)).filter(Q(region=region) | Q(town=town) & Q(gender=gender) & Q(level_of_education=education) & Q(user__profileinfo__category=category)
                                                                                             & Q(user__profileinfo__subject=subject) & Q(user__profileinfo__charge=charge))
        if self.request.user.is_authenticated:
            fav = ProfilePersonal.objects.get(
                id=self.request.user.profilepersonal.id)
            context['fav'] = fav
        print(profile_result)
        context['result'] = profile_result
        return context


class SearchAllView(TemplateView):
    template_name = 'main/search_all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET['keywords']
        result = ProfilePersonal.objects.filter(Q(first_name__icontains=kw) | Q(last_name__icontains=kw) | Q(user__profileinfo__subject__name__icontains=kw) | Q(
            user__profileinfo__category__name__icontains=kw) | Q(user__profileinfo__subcategory__name__icontains=kw))
        if self.request.user.is_authenticated:
            fav = ProfilePersonal.objects.get(
                id=self.request.user.profilepersonal.id)
            context['fav'] = fav
        context["result"] = result
        return context


def subscribe(amount, number):
    campay = Client({
        "app_username": "3_4hXF79S-PPnrduRjwCqu10EOjm6nXHezUaE76Gv-ZGuCa8qQxV-GwQP-xiaVQ_oFg4FqrduN33Od_Mi7FUmw",
        "app_password": "ICqt9K5kx-GdFfPP52Z3apDwS0LJChjSs0h1SYZ4yDAuTAXDGxgsVZ8h_Ihk9j8kxqOsQGXqj6TurNnMNwDxLw",
        "environment": "DEV"  # use "DEV" for demo mode or "PROD" for live mode
    })
    collect = campay.collect({
        "amount": amount,  # The amount you want to collect
        "currency": "XAF",
        "from": number,  # Phone number to request amount from. Must include country code
        "description": "some description"
    })
    print(collect)


class UpgradeAccountView(FormView):
    template_name = 'main/upgrade.html'
    form_class = UpgradeForm
    success_url = reverse_lazy('dantorial:upgrade_profile')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/upgrade/')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.amount = 2
        form.instance.phone_number = form.cleaned_data.get('phone_number')
        form.instance.is_complete = True
        pay = form.save(commit=False)
        profile = ProfilePersonal.objects.get(user=self.request.user)
        # subscribe(form.instance.amount, form.instance.phone_number)
        campay = Client({
            "app_username": os.getenv('CAMPAY_APP_USERNAME'),
            "app_password": os.getenv('CAMPAY_APP_PASSWORD'),
            "environment": "DEV"  # use "DEV" for demo mode or "PROD" for live mode
        })
        collect = campay.collect({
            "amount": 2,  # The amount you want to collect
            "currency": "XAF",
            # Phone number to request amount from. Must include country code
            "from": form.instance.phone_number,
            "description": "Tantorial Premium Account",
            "first_name": self.request.user.profilepersonal.first_name
        })
        print(collect)
        disburse = campay.disburse({
            "amount": "5",  # The amount you want to disburse
            "currency": "XAF",
            # Phone number to disburse amount to. Must include country code
            "to": form.instance.phone_number,
            "description": "Withdrwal from tantorial"
        })
        form.instance.reference = collect['reference']
        form.instance.status = collect['status']
        form.instance.reason = collect['reason']
        form.instance.code = collect['code']
        form.instance.operator = collect['operator']
        form.instance.operator_ref = collect['operator_reference']
        form.instance.external_ref = collect['external_reference']
        # print(disburse)
        pay = form.save(commit=False)
        if form.instance.payment_method == 'MTN Mobile Money':
            messages.success(self.request, "Dial *126# to complete payment")
        else:
            messages.success(self.request, "Dial #150*50# to complete payment")
        # if collect.status == 'SUCCESSFUL':
        # if Upgrade.objects.filter(user=self.request.user).exists():
        #     redirect('dantorial:index')
        if collect['status'] == 'SUCCESSFUL':
            form.instance.is_complete = True
            profile.paid = True
            profile.save()
            pay.save()
            self.success_url = reverse_lazy('dantorial:pay-success')
            subject = "Payment Confirmation"
            message = f'{self.requset.user.profilepersonal.first_name},Your Payment for Premium Service is complete'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = (self.request.user.email, )
            send_mail(subject, message, from_email,
                      to_email, fail_silently=True)
        else:
            form.instance.is_complete = False
            self.success_url = reverse_lazy('dantorial:pay-fail')
            subject = "Payment Fail"
            message = f'{self.request.user.profilepersonal.first_name},Your Payment for Premium Service is not complete'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = (self.request.user.email, )
            # send_mail(subject, message, from_email, to_email, fail_silently=True)
            # send_mail('hey thanks for nothing', 'here is the message', settings.DEFAULT_FROM_EMAIL, (self.request.user.email,), fail_silently=True,)
            pay.save()

        return super().form_valid(form)


class PaymentSuccessView(TemplateView):
    template_name = 'main/payment-successful.html'


class PaymentFailView(TemplateView):
    template_name = 'main/payment-fail.html'


class ProfileViewList(TemplateView):
    template_name = "main/profile_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        profile_info = ProfileViewed.objects.filter(
            user=profile).order_by('-date_created')
        context["profile"] = profile_info
        return context


@login_required(login_url='/accounts/login/')
def profile_like(request):
    if request.GET.get('action') == 'get':
        flag = False
        profileid = int(request.GET.get('profile_id'))
        userprofile = ProfilePersonal.objects.get(id=profileid)
        print(f'prof id {profileid}')
        profile_obj = ProfilePersonal.objects.get(user=request.user)
        print(f"prof obj {profile_obj} ")
        print(f'hhs {profile_obj.favourite.filter(user=userprofile.id).exists()}')

        if profile_obj.favourite.filter(user=userprofile.id).exists():
            profile_obj.favourite.remove(userprofile.user)
            profile_obj.save()
            flag = False

        else:
            profile_obj.favourite.add(userprofile.user)
            profile_obj.save()

            flag = True
            subject = "Notification from Tantorial"
            message = f'{profile_obj.first_name} liked Your Profile'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = (userprofile.user.email, )
            send_mail(subject, message, from_email,
                      to_email, fail_silently=True)
        print(flag)
        return JsonResponse({'total_favourites': profile_obj.total_likes, 'flag': flag})
    return HttpResponse("Error access Denied")


class FavouriteView(TemplateView):
    template_name = "main/favourite.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        profile_info = ProfilePersonal.objects.select_related(
            'user').get(user=profile)
        context["favourite"] = profile_info
        return context


class FavouriteDeleteView(DeleteView):
    queryset = ProfilePersonal.objects.all()


@login_required
def updateimage(request):
    profile = ProfilePersonal.objects.get(user=request.user)
    if request.method == 'POST' and request.FILES['picture']:

        image = request.FILES["picture"]

        if image:
            profile.profile_pic = image
            profile.save(update_fields=['profile_pic'])
            return redirect("dantorial:profile")
    return render(request, 'main/photo.html')


def error404(request, exception, template_name='404.html'):
    return render(request, template_name)


def error403(request, exception, template_name='403.html'):
    return render(request, template_name)


def error400(request, exception, template_name='400.html'):
    return render(request, template_name)


def error500(request, template_name='500.html'):
    return render(request, template_name)


class ScheduleView(DetailView):
    template_name = 'main/schedule.html'
    context_object_name = 'userprofile'
    model = ProfilePersonal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_form'] = AddScheduleForm
        return context

    def post(self, request, *args, **kwargs):

        if request.user.is_authenticated:

            new_schedule = OnlineLesson(student=self.request.user, teacher=self.get_object().user,
                                        start=request.POST.get('start'), end=request.POST.get('end'), mode=request.POST.get('mode'),
                                        amount=request.POST.get('amount'))
        else:
            return redirect(f'/accounts/login/?next=/userprofile/{self.get_object().id}')

        if 'post_schedule' in request.POST:
            new_schedule.save()
            messages.success(
                self.request, f"Your Request has ben sent to {self.get_object().user.profilepersonal.first_name} {self.get_object().user.profilepersonal.last_name}")
            return redirect(f'/accounts/login/?next=/userprofile/{self.get_object().id}')

        return self.get(self, request, *args, **kwargs)


class OnlineLessonNotification(TemplateView):
    template_name = 'main/notification.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/request/')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_lesson = OnlineLesson.objects.filter(teacher=self.request.user).filter(
            Q(is_decline=False) & Q(is_confirm=False))
        my_proposal = OnlineLesson.objects.filter(student=self.request.user)
        context['my_lesson'] = my_lesson
        return context


class OnlineLessonRequest(TemplateView):
    template_name = 'main/history.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/request_history/')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        final = OnlineLesson.objects.filter(Q(student=self.request.user) | Q(
            teacher=self.request.user)).order_by('-date_created')

        print(f'final {final}')
        context['my_proposal'] = final
        return context


class NotificationDetail(TemplateView):
    template_name = 'main/notification_detail.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/request/')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs['pk']
        notification = OnlineLesson.objects.get(id=pk)
        notification.is_seen = True
        notification.save()
        # print(f'not {notification.is_seen}')
        context['notification'] = notification
        return context

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        noti = OnlineLesson.objects.get(id=pk)
        if 'post_accept' in request.POST:
            noti.is_confirm = True
            noti.is_decline = False
            noti.save()
        if 'post_decline' in request.POST:
            noti.is_decline = True
            noti.is_confirm = False
            noti.save()
        if 'post_cancel' in request.POST:
            noti.is_decline = False
            noti.is_confirm = False
            noti.is_cancel = True
            noti.save()
        return self.get(self, request, *args, **kwargs)


class LandingView(TemplateView):
    template_name = 'main/landing.html'

    def post(self, request, *args, **kwargs):
        con = Contact(message=request.POST.get('message'),
                      first_name=request.POST.get('first_name'),
                      last_name=request.POST.get('last_name'),
                      email=request.POST.get('email'),
                      phone_number=request.POST.get('phone_number')
                      )
        con.save()
        messages.success(self.request, "We will get back to you shortly")
        subject = "Thanks for contacting us"
        message = request.POST.get('first_name') + " thanks for contacting us"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [request.POST.get('email'), ]

        send_mail(subject, message, from_email, to_email, fail_silently=True)
        return redirect('dantorial:index')


class FilterRegionView(TemplateView):
    template_name = 'main/region.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = kwargs['pk']
        prof = ProfilePersonal.objects.filter(region=kw)
        regi = Region.objects.get(id=kw)
        # print(f'region: {regi}')
        context["regi"] = regi
        context["prof"] = prof
        return context


class PriceView(TemplateView):
    template_name = 'main/pricing.html'


def load_test(request):
    return HttpResponse('loaderio-c1a185840f545fea9a1f72d3524a5531')
    # return render(request, 'loaderio-c1a185840f545fea9a1f72d3524a5531.html')
