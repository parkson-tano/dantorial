from .models import  *
from review.models import Review
from mainapp.models import ProfilePersonal
import random
def category_list(request):
    suggested = []
    tutor = ProfilePersonal.objects.filter(account_type="tutor")
    profil = ProfilePersonal.objects.all()
    print('erjejr')
    print(tutor)
    if request.user.is_authenticated:
        if request.user.profilepersonal in tutor:
            suggested = ProfilePersonal.objects.filter(account_type="student")
            print(suggested)
            print('sdfghfghm')
    else:
        suggested = ProfilePersonal.objects.filter(account_type="tutor")
    return {
        # 'all_cat_ind': random.sample(list(Category.objects.all()), 4),
        # 'all_subcat_ind': random.sample(list(SubCategory.objects.all()), 4),
        # 'all_sub_ind': random.sample(list(Subject.objects.all()), 4),
        'all_cat': Category.objects.all().order_by('name'),
        'all_subcat': SubCategory.objects.select_related('category').all().order_by('name'),
        'all_sub': Subject.objects.select_related('subcategory').all().order_by('subcategory'),
        'review' : Review.objects.all(),
        'tutors': random.sample(list(ProfilePersonal.objects.all()),4),
        # 'suggest_tutor': random.sample(list(ProfilePersonal.objects.filter(account_type='tutor')),25),
        'suggested': suggested

         
    }