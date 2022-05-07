from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.signals import pre_social_login
from allauth.account.utils import perform_login
from allauth.utils import get_user_model
from django.http import HttpResponse
from django.dispatch import receiver
from django.shortcuts import redirect
from django.conf import settings
import json
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, resolve_url

class MyAccountAdapter(DefaultAccountAdapter):

    def get_signup_redirect_url(self, request):
        path = "/profile-edit/{user}"
        return path.format(user=request.user.profilepersonal.id)

    def get_login_redirect_url(self, request):
        user =request.user.profilepersonal
        if (user.account_type == 'tutor' or user.account_type == 'student' or user.account_type == 'parent'):
            path = "/"
            return path
        path = '/profile-edit/{user}'
        return path.format(user=request.user.profilepersonal.id)