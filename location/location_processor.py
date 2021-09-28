from .models import Country, Region,SubRegion, City
from mainapp.models import About, OurTeam

def location_renderer(request):
    return {
        'country' : Country.objects.filter(continent='AF').order_by('phone'),
        'city' : City.objects.all(),
        'region' : Region.objects.filter(country = 1),
        'subregion': SubRegion.objects.all(),
        'city_cmr': City.objects.filter(country = 1),
        'about': About.objects.get(id=1),
        'team': OurTeam.objects.all(),

    }