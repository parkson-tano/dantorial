from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View, ListView, FormView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models import Q
from django.shortcuts import  redirect, get_object_or_404
from .models import *
from location.models import Country, City, Region, SubRegion
from category.models import Category, SubCategory
from .forms import UserLoginForm, UserRegistrationForm, PersonalProfileForm, ProfileInfoForm
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
# Create your views here.

class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = Country.objects.all()

        category = Category.objects.all()
        context['category'] = category
        return context


    # def get(self, request, *args, **kwargs):
    #     form = self.form_class
    #     return render(request, self.template_name, {'form':form})

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

class AboutView(TemplateView):
    template_name = 'main/about_us.html'

class CategoryView(DetailView):
    template_name = 'main/category.html'
    context_object_name = 'category'
    model = Category

class SubCategoryView(View):
    template_name = 'main/sub_category.html'

    def get(self, request, category_slug, subcat_slug, *args, **kwargs):
        context = {}
        category = get_object_or_404(Category, slug=category_slug)
        sub_cat = get_object_or_404(SubCategory, slug=subcat_slug)
        context["subcat"] = sub_cat

        return render(request, self.template_name, context)


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
    success_url = '/'
    model = ProfilePersonal
    
    def get(request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProfileView(TemplateView):
    pass

class ProfileInfoView(TemplateView):
    pass

class ProfileInfoEditView(UpdateView):
    template_name = 'main/edit_prof_profile.html'
    form_class = ProfileInfoForm
    success_url = '/'
    model = ProfileInfo
    
    def get(request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

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
            return render(self.request, self.template_name, {'form': self.form_class, 'error':'invalid creditials'})	
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

# class SearchView(TemplateView):
#     template_name = 'main/search.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         language = self.request.GET['language']
#         category = self.request.GET['category']
#         level_education = self.request.GET['level_of_education']
#         target = self.request.GET['target']
#         country = self.request.GET['country']
#         region = self.request.GET['region']
#         city = self.request.GET['city']
#         quater = self.request.GET['quater']
#         results = TutorProfile.objects.filter(Q())
#         return context