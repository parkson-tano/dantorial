from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .models import PersonalRoom
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


@login_required
def index(request):
    return render(request, 'chat/index.html')


def average_rating(qs):
    if not qs.first():
        return 0


class PersonalRoomDetailView(LoginRequiredMixin, DetailView):
    model = PersonalRoom
    template_name = "chat/chat.html"

    def get_queryset(self):
        return self.model.objects.by_user(user=self.request.user)

    def get_other_user_rating(self):
        user = self.request.user
        other_user = self.get_object().get_other_user(user)
        return

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["other_user"] = self.get_object().get_other_user(user)
        return context
