from django.urls import path, include

from . import views

urlpatterns = (
    path('', views.index, name='index'),
    path("<int:pk>/", views.PersonalRoomDetailView.as_view(), name="contact-detail"),
    path("api/", include('chat.api.urls')),
)
