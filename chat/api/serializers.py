from rest_framework import serializers
from chat.models import PersonalRoom


class PersonalRoomSerializer(serializers.ModelSerializer):
    other_user = serializers.SerializerMethodField()

    class Meta:
        model = PersonalRoom
        fields = (
            "last_message",
            "last_message_time",
            "last_user_to_message",
            "other_user",
        )

    def get_other_user(self, obj):
        request = self.context.get("request")
        if not request:
            return
        user = request.user
        if not user.is_authenticated:
            return
        other_user = obj.user_1
        if other_user == user:
            other_user = obj.user_2
        return other_user.email
