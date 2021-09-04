from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View, ListView, FormView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models import Q
from django.shortcuts import  redirect, get_object_or_404
from .models import *
from django.utils.decorators import method_decorator
from django.http import Http404
from location.models import Country, City, Region, SubRegion
from category.models import Category, SubCategory
from .forms import AddSubjectForm, UserLoginForm, UserRegistrationForm, PersonalProfileForm, ProfileInfoForm, AddExperienceForm, AddQualificationForm
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
# Create your views here.

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # url_id = kwargs['pk']
        # profile = ProfilePersonal.objects.get(self.get_object())
        # profile.view_count += 1
        # profile.save()
        comments_connected = Review.objects.filter(profile=self.get_object()).order_by('-date_created')
        # context['userprofile'] = userprofile
        context["comments"] = comments_connected
        context['comment_form'] = ReviewForm
        return context

    def post(self, request, *args, **kwargs):
        new_comment = Review(content=request.POST.get('content'),
                                  rating=request.POST.get('rating'),
                                  profile=self.get_object(),
									user = self.request.user)
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
    # def get(self, request, *args, **kwargs):
    #     form = self.form_class
    #     return render(request, self.template_name, {'form':form})

#     def form_valid(self, form):
# 		form.instance.user = self.request.user
#         form.save()
#         return super().form_valid(form)

class AboutView(TemplateView):
    template_name = 'main/about_us.html'

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
    
    # def get(request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)

class SubjectEditView(CreateView):
    template_name = 'main/add_subject.html'
    form_class = AddSubjectForm
    success_url = reverse_lazy('dantorial:my-subject')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class SubjectDeleteView(DeleteView):
    # @method_decorator(csrf_exempt)
    model = Subject
    success_url = reverse_lazy('dantorial:my-subject')

class ExperienceEditView(CreateView):
    template_name = 'main/add_experience.html'
    form_class = AddExperienceForm
    success_url = reverse_lazy('dantorial:my-experience')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class ExperienceDeleteView(DeleteView):
    # @method_decorator(csrf_exempt)
    model = Experience
    success_url = reverse_lazy('dantorial:my-experience')

class QualificationEditView(CreateView):
    template_name = 'main/add_qualification.html'
    form_class = AddQualificationForm
    success_url = reverse_lazy('dantorial:my-qualification')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class QualificationDeleteView(DeleteView):
    # @method_decorator(csrf_exempt)
    model = Qualification
    success_url = reverse_lazy('dantorial:my-qualification')

class ProfileDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('dantorial:index')

class QualificationUpdateView(UpdateView):
    # @method_decorator(csrf_exempt)
    template_name = 'main/update_qualification.html'
    form_class = AddQualificationForm
    model = Qualification
    success_url = reverse_lazy('dantorial:my-qualification')

class ExperienceUpdateView(UpdateView):
    template_name = 'main/update_experience.html'
    form_class = AddExperienceForm
    model = Experience
    success_url = reverse_lazy('dantorial:my-experience')

class SubjectUpdateView(UpdateView):
    template_name = 'main/update_subject.html'
    form_class = AddSubjectForm
    model = Subject
    success_url = reverse_lazy('dantorial:my-subject')

class ProfileSubjectView(TemplateView):
    template_name = 'main/my_subject.html'

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

class ProfileVerificationView(TemplateView):
    template_name = 'main/my_verification.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = self.request.user
        context["account"] = account

        verification    = Verification.objects.filter(user = account).order_by('-id')
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
        city = self.request.GET['city']
        quater = self.request.GET['quater']
        user_obj = User.objects.all()
        profile_result = ProfilePersonal.objects.filter(Q(account_type = acc_type)).filter(Q(city_id = city) | Q(address_1__icontains = quater) | Q(address_2__icontains = quater))
        subject = Subject.objects.filter(subject = subject).order_by('user')
        final = list(set(list(chain(subject, profile_result))))
        # finals = list(set(final))

        print(profile_result)
        print(subject)
        print(f'final: {final}')
        context['profile_result'] = final
        # print(f'{acc_type} {subject} {city} {quater}')
        return context
