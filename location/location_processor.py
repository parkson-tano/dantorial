from .models import Country, Region,SubRegion, City

def location_renderer(request):
    return {
        'country' : Country.objects.all(),
        'city' : City.objects.all(),
        'region' : Region.objects.all(),
        'subregion': SubRegion.objects.all(),
        'city_cmr': City.objects.filter(country = 1),
    }