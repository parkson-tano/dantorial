from .models import Carousel

def carousel_slide(request):
    return {
        'carousel' : Carousel.objects.all()
     }