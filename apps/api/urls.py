from django import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #api для получения токена
    path('employee/', EmployeeApiView.as_view()),
    path('employees/', EmployeesApiView.as_view()),
    path('employee/<int:id>', EmployeeIDApiView.as_view()),
    path('employeeid/', EmployeeIDApi.as_view()),
]

urlpatterns += static(settings.STATIC_URL,
                              document_root=settings.STATIC_URL)
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
