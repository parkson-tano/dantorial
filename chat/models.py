from django.db import models
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .managers import PersonalRoomManager

User = get_user_model()


class PersonalRoom(models.Model):
    # Provide unique related_names to user 1 and user 2 to avoid
    # clashes in reverse accessors on the user model
    user_1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="chatroom_user1")
    user_2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="chatroom_user2")
    created = models.DateTimeField(auto_now_add=True)
    objects = PersonalRoomManager()

    class Meta:
        unique_together = ("user_1", "user_2")

    def clean(self):
        if self.user_1 == self.user_2:
            raise ValidationError({
                "user_1": ValidationError(_("First user should not be equal to second user")),
                "user_2": ValidationError(_("Second user should not be equal to first user"))
            })
        query = (Q(user_1=self.user_1) & Q(user_2=self.user_2)) | (
            Q(user_1=self.user_2) & Q(user_2=self.user_1))

        if self.__class__.objects.filter(query).exists:
            raise ValidationError(
                _("Relationship between this users exists already")
            )
        return super().clean()

    def __str__(self):
        return f"Chat between {self.user_1.email} and {self.user_2.email}"

    @property
    def last_message(self):
        message = self.personal_messages.last()
        if not message:
            return ""
        return f"{message.content}"

    @property
    def last_user_to_message(self):
        message = self.personal_messages.last()

        return str(message.email)

    @property
    def last_message_time(self):
        message = self.personal_messages.last()
        if not message:
            return ""
        return str(naturaltime(message.created))

    def get_members(self):
        return {self.user_1, self.user_2}

    def get_other_user(self, user):
        if user == self.user_1:
            return self.user_2
        return self.user_1


class PersonalMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    chatroom = models.ForeignKey(
        PersonalRoom, on_delete=models.CASCADE, related_name="messages"
    )

    @property
    def username(self):
        return str(self.user.email.title())

    @property
    def userprofile(self):
        return str(self.user.profilepersonal.profile_pic.url)
