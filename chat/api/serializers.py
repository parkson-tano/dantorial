from rest_framework import serializers
from chat.models import PersonalRoom


class PersonalRoomSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    profile_pic = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()

    class Meta:
        model = PersonalRoom
        fields = (
            "last_message",
            "last_message_time",
            "last_user_to_message",
            "user",
            "bio",
            "profile_pic",
        )

    def get_other_user_object(self, obj):
        request = self.context.get("request")
        if not request:
            return
        user = request.user
        if not user.is_authenticated:
            return
        other_user = obj.user_1
        if other_user == user:
            other_user = obj.user_2
        return other_user

    def get_user(self, obj):
        return self.get_other_user_object(obj).email

    def get_profile_pic(self, obj):
        user = self.get_other_user_object(obj)
        return user.profilepersonal.profile_pic.url

    def get_bio(self, obj):
        bio = self.get_other_user_object(obj).profileinfo.bio
        return bio if bio else ""
