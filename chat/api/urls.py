from django.urls import path
from . import views


urlpatterns = [
    path("personal/", views.AllUserRoomAPIView.as_view()),
    path(
        "messages/<int:pk>/", views.PersonalMessagesAPIView.as_view()
    )
]
