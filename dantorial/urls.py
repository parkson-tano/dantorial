from django.conf.urls import handler400, handler403, handler404, handler500
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.defaults import page_not_found
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
import notifications.urls
from django.conf.urls import url

# from agora.views import Agora

handler404 = 'mainapp.views.error404'
handler403 = 'mainapp.views.error403'
handler400 = 'mainapp.views.error400'
handler500 = 'mainapp.views.error500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('chaining/', include('smart_selects.urls')),
    path('', include('mainapp.urls')),
    path('course/', include('mooc.urls')),
    path('message/', include('messaging.urls')),
    path("accounts/email/", page_not_found,{'exception': Exception('Not Found')}, name="account_email"),
    path("api/", include('api.urls')),
    path('__debug__', include(debug_toolbar.urls)),
    path("__reload__/", include("django_browser_reload.urls")),
    path('cookies/', include('cookie_consent.urls')),
    re_path(r'^robots\.txt', include('robots.urls')),
    url('', include('pwa.urls')),
    # path('agora/',Agora.as_view(
    # app_id='4fb86dc603104fa5b15c80ead4b27d44',
    # channel='tantorial')),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications'), name='notification'),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
