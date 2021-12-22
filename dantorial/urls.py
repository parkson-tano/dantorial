"""dantorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler400, handler403, handler404, handler500
from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

handler404 = 'mainapp.views.error404'
handler403 = 'mainapp.views.error403'
handler400 = 'mainapp.views.error400'
handler500 = 'mainapp.views.error500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('chaining/', include('smart_selects.urls')),
    path('', include('mainapp.urls')),
    path('message/', include('messaging.urls')),
    path("accounts/email/", page_not_found,{'exception': Exception('Not Found')}, name="account_email"),
    path("api/u/", include('api.urls')),
    path('__debug__', include(debug_toolbar.urls))


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
