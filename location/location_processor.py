from .models import Country, Region,SubRegion, City
from mainapp.models import About, OurTeam,  HowToUse, ProfilePersonal
from messaging.models import Message


def location_renderer(request):
    messags = []
    if request.user.is_authenticated:
        messags = Message.objects.filter(receiver_user = request.user).filter(is_read=False)
    return {
        'country' : Country.objects.filter(continent='AF').order_by('phone'),
        'city' : City.objects.all(),
        'region' : Region.objects.filter(country = 1),
        'subregion': SubRegion.objects.all(),
        'city_cmr': City.objects.filter(country = 1),
        'about': About.objects.get(id=1),
        'team': OurTeam.objects.all(),
        'how':  HowToUse.objects.all(),
        'messags': messags,
        

        # 'favourite': ProfilePersonal.objects.get(user=request.user),

    }
    print(messags)