from .models import  *

def category_list(request):
    return {
        'all_cat_ind': Category.objects.all().order_by('-id')[:4],
        'all_subcat_ind': SubCategory.objects.all().order_by('name')[:4],
        'all_sub_ind': Subject.objects.all().order_by('subcategory')[:4],
        'all_cat': Category.objects.all().order_by('name'),
        'all_subcat': SubCategory.objects.all().order_by('name'),
        'all_sub': Subject.objects.all().order_by('subcategory')
    }