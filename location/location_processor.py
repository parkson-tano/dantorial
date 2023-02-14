from .models import Country, Region, Town, Quater
from mainapp.models import About, OurTeam,  HowToUse, ProfilePersonal, Privacy, OnlineLesson


def location_renderer(request):
    return {
        'country': Country.objects.all(),
        'region': Region.objects.all(),
        'towns': Town.objects.all(),
        'quater': Quater.objects.all(),
        # 'about': About.objects.get(id=1),
        # 'privacy': Privacy.objects.get(id=1),
        'team': OurTeam.objects.all(),
        'how':  HowToUse.objects.all(),
        # 'favourite': ProfilePersonal.objects.get(user=request.user),

    }
