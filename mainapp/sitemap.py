from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from category.models import *
 
 
class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.date_created
        
    def location(self,obj):
        return '/category/%s' % (obj.slug)


 
class SubCategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return SubCategory.objects.get(id=1)

    def lastmod(self, obj):
        return obj.date_created
        
    def location(self,obj):
        return '/sub/%s/%s' % (obj.category.slug, obj.id)

 
class SubjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Subject.objects.all()

    def lastmod(self, obj):
        return obj.date_created
        
    def location(self,obj):
        return '/subj/%s/%s/%s' % (obj.subcategory.category.slug, obj.subcategory.id, obj.slug)

class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['dantorial:index', 'dantorial:aboutus', 'dantorial:contactus', 'dantorial:landing']
    def location(self, item):
        return reverse(item)