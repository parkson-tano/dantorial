from django.db import models
from notifications.models import notify_handler
from notifications.signals import notify
from notifications.models import Notification

# Create your models here.


class NotificationCTA(models.Model):
    notification = models.OneToOneField(Notification, on_delete=models.CASCADE)
    cta_link = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.cta_link)


def custom_notify_handler(*args, **kwargs):
    notifications = notify_handler(*args, **kwargs)
    cta_link = kwargs.get("cta_link", "")
    for notification in notifications:
        NotificationCTA.objects.create(notification=notification, cta_link=cta_link)
    return notifications


notify.disconnect(notify_handler, dispatch_uid='notifications.models.notification')
notify.connect(custom_notify_handler)  # , dispatch_uid='notifications.models.notification')