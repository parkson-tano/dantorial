from .models import Carousel
from mainapp.models import Subject, ProfilePersonal
def carousel_slide(request):
    return {
        'carousel' : Carousel.objects.all(),
        'subject_res' : Subject.objects.all(),
        'suggested': ProfilePersonal.objects.filter(paid=True)
     }