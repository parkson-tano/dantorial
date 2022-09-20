from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import PersonalRoomSerializer
from chat.models import PersonalRoom


class AllUserRoomAPIView(ListAPIView):
    serializer_class = PersonalRoomSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        qs = PersonalRoom.objects.by_user(user=self.request.user)
        print(qs)
        return qs
