from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View, ListView, FormView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import  redirect, get_object_or_404
from requests.api import request
from .models import *
from django.utils.decorators import method_decorator
from django.http import Http404
from location.models import Country, City, Region, SubRegion
from category.models import Category, SubCategory
from .forms import (AddSubjectForm, UserLoginForm, UserRegistrationForm, VerificationForm,
PersonalProfileForm, ProfileInfoForm, AddExperienceForm, AddQualificationForm, UpgradeForm)
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
from location.models import Country, Region, SubRegion, City
from itertools import chain
from review.models import Review
from review.forms import ReviewForm
from allauth.account.admin import EmailAddress
from messaging.models import Message, Contact
from messaging.forms import MessageForm, ContactForm
# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
from campay.sdk import Client



class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = Country.objects.all()
        pro = ProfilePersonal.objects.all()
        category = Category.objects.all()
        context['category'] = category
        context['pro'] = pro
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
        prof = ProfilePersonal.objects.get(user = self.request.user)
        userEmail = EmailAddress.objects.get(user=self.request.user)
        context['auth'] = userEmail
        context['prof'] = prof
        return context  

class UserProfileView(DetailView):
    template_name = 'main/userprofile.html'
    context_object_name = 'userprofile'
    model = ProfilePersonal

    
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         pass
    #     else:
    #         return redirect('/accounts/login/?next=userprofile/6')
            
    #     return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments_connected = Review.objects.filter(profile=self.get_object()).order_by('-date_created')
        context["comments"] = comments_connected
        context['comment_form'] = ReviewForm 
        context['message'] = MessageForm

        
        prof = ProfilePersonal.objects.get(user__username=self.get_object())
        if self.request.user.is_authenticated:
            current = ProfilePersonal.objects.get(user=self.request.user)
            if (self.request.user != self.get_object().user):
                new_view = ProfileViewed.objects.create(user=self.get_object().user, viewed_by =self.request.user )
                prof.view_count += 1
                current.favourite.add(self.get_object().user)
                current.save()
                prof.save()

                # send_mail('profile viewed', f'{self.request.user.profilepersonal.first_name} viewed your profile', settings.DEFAULT_FROM_EMAIL, (self.get_object().user.email,))
            else:
                pass
        # new_view.save()
        else:
            if (self.request.user != self.get_object().user):
                new_view = ProfileViewed.objects.create(user=self.get_object().user,)
                prof.view_count += 1
                prof.favourite.add(self.get_object().user)
                prof.save()
            else:
                pass

        return context

    def post(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            new_comment = Review(content=request.POST.get('content'),
                                  rating=request.POST.get('rate'),
                                  profile=self.get_object(),
									user = self.request.user)

            new_message = Message(sender_user = self.request.user,
                receiver_user = self.get_object().user,
                message = request.POST.get('message'),
                )
        else:
            return redirect(f'/accounts/login/?next=/userprofile/{self.get_object().id}')

        if 'post_comment' in request.POST:
            new_comment.save()

        elif 'send_message' in request.POST:
            new_message.save()
            messages.success(self.request, 'message sucessfully sent')

        return self.get(self, request, *args, **kwargs)
        
        
    # def get(self, request, *args, **kwargs):
    #     form = self.form_class
    #     return render(request, self.template_name, {'form':form})

#     def form_valid(self, form):
# 		form.instance.user = self.request.user
#         form.save()
#         return super().form_valid(form)

# class MessageView(View):
#     def post(self, request, pk, *args, **kwargs):
#         form = MessageForm(request.POST)
#         if request.user.is_authenticated:
#             new_message = Message(sender_user = self.request.user,
#                     receiver_user = self.get_object().user,
#                     message = request.POST.get('message'),
#                     )
#         else:
#             new_message = Message(
#                     receiver_user = self.get_object().user,
#                     name = request.POST.get('name'),
#                     email = request.POST.get('email'),
#                     phone_number = request.POST.get('phone_number'),
#                     message = request.POST.get('message'),
#                     )
#         new_message.save()
#         return self.get(self, request, *args, **kwargs)

class AboutView(TemplateView):
    template_name = 'main/about_us.html'

class ContactView(CreateView):
    template_name = 'main/contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('dantorial:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "We will get back to you shortly")
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
        user = User.objects.create_user(username, email,password)
        form.instance.user = user
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return super().form_valid(form)

class PersonalProfileEditView(UpdateView):
    template_name = 'main/edit_profile.html'
    form_class = PersonalProfileForm
    success_url = reverse_lazy('dantorial:profile')
    model = ProfilePersonal

    def get_object(self):
        return self.request.user.profilepersonal

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)
    
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and ProfilePersonal.objects.get(user=request.user):
    #         pass
    #     else:
    #         redirect('dantorial:index')

    #     return super().dispatch(request, *args, **kwargs)
    

    # def get(request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)

class ProfileView(TemplateView):
    template_name = 'main/profile.html'
    # model = ProfilePersonal
    # context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        profile_info = ProfilePersonal.objects.get(user=profile)
        context["profile"] = profile_info
        return context

class ProfileInfoView(TemplateView):
    template_name = 'main/profile_info.html'
    # model = ProfileInfo
    # context_object_name = 'profile_info'  

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

        qualification = Qualification.objects.filter(user = account).order_by('-id')
        context['qualification'] = qualification
        return context

class ProfileExperienceView(TemplateView):
    template_name = 'main/my_experience.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = self.request.user
        context["account"] = account

        experience = Experience.objects.filter(user = account).order_by('-id')
        context['experience'] = experience
        return context

class ProfileInfoEditView(UpdateView):
    template_name = 'main/edit_prof_profile.html'
    form_class = ProfileInfoForm
    success_url = reverse_lazy('dantorial:profile-info')
    model = ProfileInfo

    def get_object(self):
        return self.request.user.profileinfo
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)
    # def get(request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)

class SubjectEditView(CreateView):
    template_name = 'main/add_subject.html'
    form_class = AddSubjectForm
    success_url = reverse_lazy('dantorial:my-subject')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Subject Added Successfully")
        form.save()
        return super().form_valid(form)

class SubjectDeleteView(DeleteView):
    # @method_decorator(csrf_exempt)
    model = Subject
    success_url = reverse_lazy('dantorial:my-subject')

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, 'sucessfully removed subject')
        return super().delete(request, *args, **kwargs)

class ExperienceEditView(CreateView):
    template_name = 'main/add_experience.html'
    form_class = AddExperienceForm
    success_url = reverse_lazy('dantorial:my-experience')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)

class ExperienceDeleteView(DeleteView):
    # @method_decorator(csrf_exempt)
    model = Experience
    success_url = reverse_lazy('dantorial:my-experience')
    def delete(self, request, *args, **kwargs):
        messages.error(self.request, 'sucessfully removed experience')
        return super().delete(request, *args, **kwargs)

class QualificationEditView(CreateView):
    template_name = 'main/add_qualification.html'
    form_class = AddQualificationForm
    success_url = reverse_lazy('dantorial:my-qualification')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)

class QualificationDeleteView(DeleteView):
    # @method_decorator(csrf_exempt)
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
    # @method_decorator(csrf_exempt)
    template_name = 'main/update_qualification.html'
    form_class = AddQualificationForm
    model = Qualification
    success_url = reverse_lazy('dantorial:my-qualification')

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

        subject = Subject.objects.filter(user = account).order_by('-id')
        context['subject'] = subject
        return context

class VerificationEditView(CreateView):
    template_name   = 'main/add_verification.html'
    model = Verification
    form_class  = VerificationForm
    success_url  = reverse_lazy('dantorial:my-verification')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Successful")
        form.save()
        return super().form_valid(form)

class VerificationDeleteView(DeleteView):
    # @method_decorator(csrf_exempt)
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = self.request.user
        context["account"] = account

        verification    = Verification.objects.get(user = account)
        context['verify'] = verification    
        return context

# class SubjectView(DetailView):
#     template_name = 'main/my_subject.html'
#     model = Subject
#     context_object_name = 'subject'

#     def dispatch(self, request, *args, **kwargs):
#         account = self.request.user
#         sub_id = self.kwargs['pk']
#         subject = Subject.objects.filter(id=sub_id)

#         action = request.GET.get('action')
#         sub_obj = subject.user
#         if action == 'rmv':
#             sub_obj.save()
#             sub_obj.delete()
#             return redirect('/')
#         else:
#             pass
#         return super().dispatch(request, *args, **kwargs)
    

class UserLoginView(FormView):
    template_name = 'main/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('dantorial:index')
    def form_valid(self, form):
        uname = form.cleaned_data.get('username')
        pword = form.cleaned_data.get('password')
        usr = authenticate(username=uname, password=pword)
        if usr is not None and ProfilePersonal.objects.filter(user=usr).exists():
            login(self.request, usr, backend='django.contrib.auth.backends.ModelBackend')
        else:
            return render(self.request,self.template_name, {'form': self.form_class, 'error':'invalid creditials'})	
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
    template_name = 'main/search_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        acc_type = self.request.GET['typ']
        subject = self.request.GET['subject']
        category = self.request.GET['category']
        quater = self.request.GET['quater']
        user_obj = User.objects.all()
        profile_result = ProfilePersonal.objects.filter(Q(account_type = acc_type)).filter(Q(address_1__icontains = quater) | Q(address_2__icontains = quater) & Q(user__profileinfo__category = category) & Q(user__profileinfo__subject = subject))
        # subject = Subject.objects.filter(subject = subject).order_by('user')
        # final = list(set(list(chain(subject, profile_result))))
        # finals = list(set(final))

        print(profile_result)
        # print(subject)
        # print(f'final: {final}')
        context['profile_result'] = profile_result
        # print(f'{acc_type} {subject} {city} {quater}')
        return context


class SearchAllView(TemplateView):
    template_name = 'main/search_all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET['keywords']
        result = ProfilePersonal.objects.filter(Q(first_name__icontains=kw) | Q(last_name__icontains=kw) | Q(user__profileinfo__bio__icontains=kw) | Q(user__profileinfo__experience__icontains=kw))
        context["result"] = result
        return context

def subscribe(amount, number):
    campay = Client({
        "app_username" : "3_4hXF79S-PPnrduRjwCqu10EOjm6nXHezUaE76Gv-ZGuCa8qQxV-GwQP-xiaVQ_oFg4FqrduN33Od_Mi7FUmw",
        "app_password" : "ICqt9K5kx-GdFfPP52Z3apDwS0LJChjSs0h1SYZ4yDAuTAXDGxgsVZ8h_Ihk9j8kxqOsQGXqj6TurNnMNwDxLw",
        "environment" : "DEV" #use "DEV" for demo mode or "PROD" for live mode
    })
    collect = campay.collect({
         "amount": amount, #The amount you want to collect
         "currency": "XAF",
         "from": number, #Phone number to request amount from. Must include country code
         "description": "some description"
      })
    print(collect)

class UpgradeAccountView(FormView):
    template_name = 'main/upgrade.html'
    form_class = UpgradeForm
    success_url = reverse_lazy('dantorial:upgrade_profile')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.amount = 2
        form.instance.phone_number = form.cleaned_data.get('phone_number')
        form.instance.is_complete = True
        pay = form.save(commit=False)
        profile = ProfilePersonal.objects.get(user = self.request.user)
        # subscribe(form.instance.amount, form.instance.phone_number)
        campay = Client({
        "app_username" : "3_4hXF79S-PPnrduRjwCqu10EOjm6nXHezUaE76Gv-ZGuCa8qQxV-GwQP-xiaVQ_oFg4FqrduN33Od_Mi7FUmw",
        "app_password" : "ICqt9K5kx-GdFfPP52Z3apDwS0LJChjSs0h1SYZ4yDAuTAXDGxgsVZ8h_Ihk9j8kxqOsQGXqj6TurNnMNwDxLw",
        "environment" : "DEV" #use "DEV" for demo mode or "PROD" for live mode
        })
        collect = campay.collect({
         "amount": 2, #The amount you want to collect
         "currency": "XAF",
         "from": form.instance.phone_number, #Phone number to request amount from. Must include country code
         "description": "Tantorial Premium Account",
         "first_name": self.request.user.profilepersonal.first_name
         })
        print(collect)
        # disburse = campay.disburse({
        #  "amount": "5", #The amount you want to disburse
        #  "currency": "XAF",
        #  "to": form.instance.phone_number, #Phone number to disburse amount to. Must include country code
        #  "description": "Withdrwal from tantorial"
        # })
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
            send_mail('hey thanks ', 'here is the message', settings.DEFAULT_FROM_EMAIL, (self.request.user.email,))
            # messages.success(self.request, "Successful")
        else:
            form.instance.is_complete = False
            self.success_url = reverse_lazy('dantorial:pay-fail')
            # messages.success(self.request, "Failed")
            send_mail('hey thanks for nothing', 'here is the message', settings.DEFAULT_FROM_EMAIL, (self.request.user.email,))
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
        profile_info = ProfileViewed.objects.filter(user=profile)
        context["profile"] = profile_info
        return context

class FavouriteAddView():
    pass