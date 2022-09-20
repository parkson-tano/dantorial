from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import PersonalRoomSerializer, PersonalRoomAndMessageSerializer
from chat.models import PersonalRoom


class AllUserRoomAPIView(ListAPIView):
    serializer_class = PersonalRoomSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        qs = PersonalRoom.objects.by_user(user=self.request.user)
        return qs


class PersonalMessagesAPIView(RetrieveAPIView):
    serializer_class = PersonalRoomAndMessageSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        qs = PersonalRoom.objects.by_user(user=self.request.user)
        return qs
