from .models import Carousel
from mainapp.models import Subject
def carousel_slide(request):
    return {
        'carousel' : Carousel.objects.all(),
        'subject_res' : Subject.objects.all()
     }