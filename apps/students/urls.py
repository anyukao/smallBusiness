from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import *

urlpatterns = [
        path('personalaccounts/<int:id>',views.KSTUpersonalaccounts, name='personalaccounts'),
        path('studentaccount/<int:id>',views.KSTUstudentaccount, name='studentaccount'),
        path('editpersonalaccounts/<int:id>',KSTUeditemployeeaccounts, name='editpersonalaccounts'),
        path("editstud/",KSTUeditstud,name='editstud'),
        path("editstuds/<int:id>",KSTUeditstuds,name='editstuds'),
        path("studentleaflet/",createStudent,name='studentleaflet'),
        
        path('addstudent/', views.createStudent, name='addstudent'),
        path('dataadded/', DataAdded, name='dataadded'),
        path('saikal/', name, name='saikal'),
        path('studleaflet/', views.createStudentLeaflet, name='studleaflet'),
        path('studleaflet/<int:id>', views.createStudentLeaflet, name='studleaflet'),
        path('studpd/', views.KSTUspd, name='studpd'),
        path('studpl/', views.KSTUspl, name='studpl'),
        path('studadd/', views.KSTUsadd, name='studadd'),

        path('studentleafletsearch/', SearchSData.as_view(), name='studentleafletsearch'),


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
