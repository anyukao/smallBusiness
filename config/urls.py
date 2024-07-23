from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from .views import *
from . import views

urlpatterns = [
    path('anyu/', admin.site.urls),
    path("",include('apps.onoxo.urls')),

    
    
 
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

handler404 = views.custom_page_not_found_view
handler500 = views.custom_error_view
handler403 = views.custom_permission_denied_view
handler400 = views.custom_bad_request_view
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
