from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View, ListView, FormView, CreateView
from django.core.mail import send_mail
from django.conf import Settings, settings
from django.shortcuts import  redirect, get_object_or_404
from campay.sdk import Client
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from mainapp.models import *
# Create your views here.
import campay


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


class PaymentView(TemplateView):
    template_name = 'main/payment.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/payments/')

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
            "app_username": "3_4hXF79S-PPnrduRjwCqu10EOjm6nXHezUaE76Gv-ZGuCa8qQxV-GwQP-xiaVQ_oFg4FqrduN33Od_Mi7FUmw",
            "app_password": "ICqt9K5kx-GdFfPP52Z3apDwS0LJChjSs0h1SYZ4yDAuTAXDGxgsVZ8h_Ihk9j8kxqOsQGXqj6TurNnMNwDxLw",
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

            # messages.success(self.request, "Successful")
        else:
            form.instance.is_complete = False
            self.success_url = reverse_lazy('dantorial:pay-fail')
            # messages.success(self.request, "Failed")
            subject = "Payment Fail"
            message = f'{self.request.user.profilepersonal.first_name},Your Payment for Premium Service is not complete'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = (self.request.user.email, )
            # send_mail(subject, message, from_email, to_email, fail_silently=True)
            # send_mail('hey thanks for nothing', 'here is the message', settings.DEFAULT_FROM_EMAIL, (self.request.user.email,), fail_silently=True,)
            pay.save()

        return super().form_valid(form)

class WithdrawView(TemplateView):
    template_name = 'main/withdraw.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/withdraws/')

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
            "app_username": "3_4hXF79S-PPnrduRjwCqu10EOjm6nXHezUaE76Gv-ZGuCa8qQxV-GwQP-xiaVQ_oFg4FqrduN33Od_Mi7FUmw",
            "app_password": "ICqt9K5kx-GdFfPP52Z3apDwS0LJChjSs0h1SYZ4yDAuTAXDGxgsVZ8h_Ihk9j8kxqOsQGXqj6TurNnMNwDxLw",
            "environment": "DEV"  # use "DEV" for demo mode or "PROD" for live mode
        })

        disburse = campay.disburse({
            "amount": "5", #The amount you want to disburse
            "currency": "XAF",
            "to": form.instance.phone_number, #Phone number to disburse amount to. Must include country code
            "description": "Withdrwal from tantorial"
        })
        print(disburse)
        form.instance.reference = disburse['reference']
        form.instance.status = disburse['status']
        form.instance.reason = disburse['reason']
        form.instance.code = disburse['code']
        form.instance.operator = disburse['operator']
        form.instance.operator_ref = disburse['operator_reference']
        form.instance.external_ref = disburse['external_reference']
        # print(disburse)
        pay = form.save(commit=False)
        if disburse['status'] == 'SUCCESSFUL':
            form.instance.is_complete = True
            profile.paid = True
            profile.save()
            pay.save()
            self.success_url = reverse_lazy('dantorial:pay-success')
            subject = "Withdrawal Confirmation"
            message = f'{self.request.user.profilepersonal.first_name},Your Withdrawal is complete'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = (self.request.user.email, )
            send_mail(subject, message, from_email,
                    to_email, fail_silently=True)

            # messages.success(self.request, "Successful")
        else:
            form.instance.is_complete = False
            self.success_url = reverse_lazy('dantorial:pay-fail')
            # messages.success(self.request, "Failed")
            subject = "Withdraw Fail"
            message = f'{self.request.user.profilepersonal.first_name},Your Withdrawal is not complete'
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
