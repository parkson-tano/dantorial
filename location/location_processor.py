from .models import Country, Region, Town, Quater
from mainapp.models import About, OurTeam,  HowToUse, ProfilePersonal, Privacy, OnlineLesson
from messaging.models import Message
from notifications.models import Notification


def location_renderer(request):
    messags = []
    if request.user.is_authenticated:
        messags = Message.objects.filter(
            receiver_user=request.user).filter(is_read=False)
        notification = OnlineLesson.objects.filter(
            teacher=request.user).filter(is_seen=False)
    else:
        notification = ''
    return {
        'country': Country.objects.all(),
        'region': Region.objects.all(),
        'towns': Town.objects.all(),
        'quater': Quater.objects.all(),
        'about': About.objects.get(id=1),
        'privacy': Privacy.objects.get(id=1),
        'team': OurTeam.objects.all(),
        'how':  HowToUse.objects.all(),
        'messags': messags,
        'notificatio': notification,
        # 'favourite': ProfilePersonal.objects.get(user=request.user),

    }
    print(messags)
