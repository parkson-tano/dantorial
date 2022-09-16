from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View, ListView, FormView, CreateView
from django.core.mail import send_mail
from django.conf import Settings, settings
from django.shortcuts import redirect, get_object_or_404
from numpy import less
from campay.sdk import Client
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.contrib import messages
from mainapp.models import *
from .models import Payment
from .forms import *
from django.contrib.auth import get_user_model
User = get_user_model()
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
    # form_class = PaymentForm
    # success_url = reverse_lazy('dantorial:payment')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/payments/')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs['pk']
        lesson = OnlineLesson.objects.get(id=pk)
        context["lesson"] = lesson
        return context

    # def get_queryset(self):
    #     self.pk = get_object_or_404(OnlineLesson, id=self.kwargs['pk'])
    #     return super().get_queryset()

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        lesson = OnlineLesson.objects.get(id=pk)
        lesson_escrow = LessonEscrow.objects.get(lesson=lesson)
        user = self.request.user

        payment_method = self.request.POST.get('payment_method')
        amount = lesson.amount
        phone_number = self.request.POST.get('phone_number')
        withdrawal = False
        reason_payment = "Escrow Payment"
        is_complete = False
        pay = Payment(user=user,)

        pay.amount = amount
        pay.lesson = lesson
        pay.payment_method = payment_method
        pay.phone_number = phone_number
        pay.withdrawal = withdrawal
        pay.reason_payment = reason_payment
        pay.is_complete = is_complete
        pay.save()
        profile = ProfilePersonal.objects.get(user=self.request.user)
        # subscribe(form.instance.amount, form.instance.phone_number)
        campay = Client({
            "app_username": "3_4hXF79S-PPnrduRjwCqu10EOjm6nXHezUaE76Gv-ZGuCa8qQxV-GwQP-xiaVQ_oFg4FqrduN33Od_Mi7FUmw",
            "app_password": "ICqt9K5kx-GdFfPP52Z3apDwS0LJChjSs0h1SYZ4yDAuTAXDGxgsVZ8h_Ihk9j8kxqOsQGXqj6TurNnMNwDxLw",
            "environment": "DEV"  # use "DEV" for demo mode or "PROD" for live mode
        })
        collect = campay.collect({
            "amount": 5,  # The amount you want to collect
            "currency": "XAF",
            # Phone number to request amount from. Must include country code
            "from": "237" + phone_number,
            "description": "Tantorial Premium Account",
            "first_name": self.request.user.profilepersonal.first_name
        })
        print(collect)

        pay.reference = collect['reference']
        pay.status = collect['status']
        pay.reason = collect['reason']
        pay.code = collect['code']
        pay.operator = collect['operator']
        pay.operator_ref = collect['operator_reference']
        pay.external_ref = collect['external_reference']

        # print(disburse)
        # pay = form.save(commit=False)
        # if pay.payment_method == 'mobile money':
        #     messages.success(self.request, "Dial *126# to complete payment")
        # else:
        #     messages.success(self.request, "Dial #150*50# to complete payment")
        # if collect.status == 'SUCCESSFUL':
        # if Upgrade.objects.filter(user=self.request.user).exists():
        #     redirect('dantorial:index')
        if collect['status'] == 'SUCCESSFUL':
            pay.is_complete = True
            profile.paid = True
            lesson_escrow.complete = True
            lesson_escrow.amount = amount
            # lesson_escrow.payout_amount = amount
            lesson_escrow.save()
            profile.save()
            contract = Contract(escrow=lesson_escrow)
            contract.save()

            pay.save()

            subject = "Payment Confirmation"
            message = f'{self.request.user.profilepersonal.first_name},Your Payment for a lesson with {lesson.teacher.profilepersonal.first_name} {lesson.teacher.profilepersonal.last_name} is complete'
            message2 = f'{self.request.user.profilepersonal.first_name} has successful paid the sum of {amount}XAF for a lesson with you.'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = (self.request.user.email, )
            to_email2 = (lesson.teacher.email,)
            send_mail(subject, message, from_email,
                      to_email, fail_silently=True)
            send_mail(subject, message2, from_email,
                      to_email2, fail_silently=True)

            # messages.success(self.request, "Successful")
            return redirect('dantorial:pay-success')
        else:
            is_complete = False

            # messages.success(self.request, "Failed")
            subject = "Payment Fail"
            message = f'{self.request.user.profilepersonal.first_name},Your Payment for Premium Service is not complete'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = (self.request.user.email, )
            # send_mail(subject, message, from_email, to_email, fail_silently=True)
            # send_mail('hey thanks for nothing', 'here is the message', settings.DEFAULT_FROM_EMAIL, (self.request.user.email,), fail_silently=True,)
            pay.save()

            return redirect('dantorial:pay-fail')

        return self.get(self, request, *args, **kwargs)


class WithdrawView(FormView):
    template_name = 'main/withdraw.html'
    form_class = PaymentForm
    success_url = reverse_lazy('dantorial:payment')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/login/?next=/withdraws/')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.payment_method = self.request.POST.get('payment_method')
        form.instance.amount = self.request.POST.get('amount')
        form.instance.phone_number = self.request.POST.get('phone_number')
        form.instance.withdrawal = True
        form.instance.reason_payment = "Fund withdrawal"
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
            # The amount you want to disburse
            "amount": self.request.POST.get('amount'),
            "currency": "XAF",
            # Phone number to disburse amount to. Must include country code
            "to": "237" + form.instance.phone_number,
            "description": "Withdrawal from tantorial"
        })
        print(disburse)
        if (disburse['reference']):
            form.instance.reference = disburse['reference']
            form.instance.status = disburse['status']
            form.instance.reason = disburse['reason']
            form.instance.code = disburse['code']
            form.instance.operator = disburse['operator']
            form.instance.operator_ref = disburse['operator_reference']
            form.instance.external_ref = disburse['external_reference']
            # print(disburse)
            pay = form.save(commit=False)
            if form.instance.payment_method == 'MTN Mobile Money':
                messages.success(
                    self.request, "Dial *126# to complete payment")
            else:
                messages.success(
                    self.request, "Dial #150*50# to complete payment")
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
