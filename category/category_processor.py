from .models import  *
import random
def category_list(request):
    return {
        'all_cat_ind': random.sample(list(Category.objects.all()), 4),
        'all_subcat_ind': random.sample(list(SubCategory.objects.all()), 4),
        'all_sub_ind': random.sample(list(Subject.objects.all()), 4),
        'all_cat': Category.objects.all().order_by('name'),
        'all_subcat': SubCategory.objects.all().order_by('name'),
        'all_sub': Subject.objects.all().order_by('subcategory')
    }