from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View
from .models import Category, SubCategory, Subject
from mainapp.models import ProfilePersonal
from django.contrib.auth.models import User
import random
# Create your views here.

class CategoryView(TemplateView):
    template_name = 'main/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = kwargs['slug']
        category = Category.objects.get(slug=url_slug)
        subcat = SubCategory.objects.filter(category=category)
        pro = ProfilePersonal.objects.filter(user__profileinfo__category__slug=url_slug)
        # pro = random.shuffle(list(pro))
        context["subcat"] = subcat
        context['pro'] = pro
        print(pro)
        return context

class SubcategoryView(View):
    # template_name = 'main/subcategory.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     url_slug = kwargs['slug']
    #     subcat = SubCategory.objects.get(slug=url_slug)
    #     subject = Subject.objects.filter(subcategory = subcat)
    #     pro = ProfilePersonal.objects.all()
    #     context["subcat"] = subcat
    #     context['subject'] = subject
    #     context['pro'] = pro
    #     return context

    def get(self, request, category_slug, subcat_slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=category_slug)
        subcate = get_object_or_404(SubCategory, pk=subcat_slug) 
        context = {}
        subject = Subject.objects.filter(subcategory = subcate)
        pro = ProfilePersonal.objects.filter(user__profileinfo__subcategory=subcat_slug)
        # context["subcat"] = subcat
        context['subject'] = subject
        context['pro'] = pro        
        return render(request, 'main/subcategory.html', context)


class SubjectView(View):
    # template_name = 'main/subject.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     url_slug = kwargs['slug']
    #     subject = Subject.objects.filter(slug = url_slug)
    #     context["subject"] = subject
    #     return context
    
    def get(self, request, category_slug, subcat_slug, subject_slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=category_slug)
        subcate = get_object_or_404(SubCategory, pk=subcat_slug) 
        subject = get_object_or_404(Subject, slug=subject_slug)  
        context = {}
        subject = Subject.objects.filter(subcategory = subcate)
        pro = ProfilePersonal.objects.filter(user__profileinfo__subject__slug=subject_slug)
        context['subject'] = subject
        context['pro'] = pro        
        return render(request, 'main/subject.html', context)    


class AllCategoryView(TemplateView):
    template_name = 'main/all_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        pro = ProfilePersonal.objects.all()
        context["pro"] = pro
        context['category'] = category 
        return context
    
class AllSubCategoryView(TemplateView):
    template_name = 'main/all_subcategory.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subcategory = SubCategory.objects.all()
        pro = ProfilePersonal.objects.all()
        context["pro"] = pro
        context['subcat'] = subcategory 
        return context

class AllSubjectView(TemplateView):
    template_name = 'main/all_subject.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = Subject.objects.all()
        pro = ProfilePersonal.objects.all()
        context["pro"] = pro
        context['sub'] = subject
        return context

# class AllCategoryView(TemplateView):
#     template_name = 'main/all.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         pro = ProfilePersonal.objects.all()
#         context["pro"] = pro
#         return context