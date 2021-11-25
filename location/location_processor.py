from .models import Country, Region,Town, Quater
from mainapp.models import About, OurTeam,  HowToUse, ProfilePersonal
from messaging.models import Message


def location_renderer(request):
    messags = []
    if request.user.is_authenticated:
        messags = Message.objects.filter(receiver_user = request.user).filter(is_read=False)
    return {
        'country' : Country.objects.all(),
        'region' : Region.objects.all(),
        'town' : Town.objects.all(),
        'quater': Quater.objects.all(),
        'about': About.objects.get(id=1),
        'team': OurTeam.objects.all(),
        'how':  HowToUse.objects.all(),
        'messags': messags,
        # 'favourite': ProfilePersonal.objects.get(user=request.user),

    }
    print(messags)