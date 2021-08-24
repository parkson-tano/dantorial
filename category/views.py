from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, SubCategory, Subject
from mainapp.models import ProfilePersonal
from django.contrib.auth.models import User
# Create your views here.

class CategoryView(TemplateView):
    template_name = 'main/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all().order_by('name')
        context["category"] = category
        
        return context

class SubcategoryView(TemplateView):
    template_name = 'main/subcategory.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = kwargs['slug']
        category = Category.objects.get(slug=url_slug)
        subcat = SubCategory.objects.filter(category=category)
        pro = ProfilePersonal.objects.all()
        context["subcat"] = subcat
        context['pro'] = pro
        return context
    
class SubjectView(TemplateView):
    template_name = 'main/subject.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = kwargs['slug']
        subcat = SubCategory.objects.get(slug=url_slug)
        subject = Subject.objects.filter(subcategory=subcat)
        context["subject"] = subject
        return context
    