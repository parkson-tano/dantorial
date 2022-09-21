from dataclasses import fields
from rest_framework import serializers
from chat.models import PersonalMessage, PersonalRoom
from django.urls import reverse_lazy


class PersonalRoomSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    profile_pic = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    chat_url = serializers.SerializerMethodField()

    class Meta:
        model = PersonalRoom
        fields = (
            "id",
            "last_message",
            "last_message_time",
            "last_user_to_message",
            "user",
            "bio",
            "profile_pic",
            "chat_url",
        )

    def get_other_user_object(self, obj):
        user = self.context.get("request").user
        return obj.get_other_user(user)

    def get_user(self, obj):
        return self.get_other_user_object(obj).email.title()

    def get_profile_pic(self, obj):
        user = self.get_other_user_object(obj)
        return user.profilepersonal.profile_pic.url

    def get_bio(self, obj):
        bio = self.get_other_user_object(obj).profileinfo.bio
        return bio if bio else "User has not set a bio"

    def get_user_id(self, obj):
        return self.get_other_user_object(obj).id

    def get_chat_url(sel, obj):
        return reverse_lazy("contact-detail", kwargs={"pk": obj.id})


class PersonalMessageSerializer(serializers.ModelSerializer):
    isowner = serializers.SerializerMethodField()

    class Meta:
        model = PersonalMessage
        fields = ("username", "content", "created", "isowner", "userprofile")

    def get_isowner(self, obj):
        request = self.context.get("request")
        if not request.user.is_authenticated:
            return None
        return obj.user == request.user


class PersonalRoomAndMessageSerializer(serializers.ModelSerializer):
    messages = PersonalMessageSerializer(many=True)

    class Meta:
        model = PersonalRoom
        fields = ("messages",)
