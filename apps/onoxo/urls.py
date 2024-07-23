from django import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path("",mainForm_fun,name='home'),
    path("home/",mainForm_fun,name='homes'),
    path("budjet/",budjet_fun,name='budjet'),
    path("Employee/",employee_fun,name='Employee'),
    path("finishedProduct/",finishedProduct_fun,name='finishedProduct'),
    path("Ingredients/<int:id>",ingredients_funred,name='Ingredientslog'),
    path("Ingredients/",ingredients_fun,name='Ingredients'),
    path("jobTitlePage/",jobTitlePage_fun,name='jobTitlePage'),
    path("production/",production_fun,name='production'),
    path("purchaseRawM/",purchaseRawM_fun,name='purchaseRawM'),
    path("rawMaterials/",rawMaterials_fun,name='rawMaterials'),
    path("saleOfProduct/",saleOfProduct_fun,name='saleOfProduct'),
    path("Unit/",unit_fun,name='Unit'),
    path("employeeedit/<int:id>",employeeedit,name='employeeedit'),
    path("finishedProductedit/<int:id>",finishedProductedit,name='finishedProductedit'),
    path("jobTitlePageedit/<int:id>",jobTitlePageedit,name='jobTitlePageedit'),
    path("saleOfProductedit/<int:id>",saleOfProductedit,name='saleOfProductedit'),
    path("ingredientsedit/<int:id>",ingredientsedit,name='ingredientsedit'),
    path("unitEdit/<int:id>",unitEdit,name='unitEdit'),
    path("budjetEdit/<int:id>",budjetEdit,name='budjetEdit'),
    path("productionEdit/<int:id>/",productionEdit,name='productionEdit'),
    path("rawMaterialsEdit/<int:id>",rawMaterialsEdit,name='rawMaterialsEdit'),
    path("purchaseRawMEdit/<int:id>",purchaseRawMEdit,name='purchaseRawMEdit'),
    path("salaryedit/<int:id>",SalaryEdit,name='salaryedit'),
    path("salary/<check>",SalaryNext,name='salarys'),
    path("credit/",credit,name='credit'),
    path("credit/<int:id>",CreditForEveryMonth,name='creditik'),

]

urlpatterns += static(settings.STATIC_URL,
                              document_root=settings.STATIC_URL)
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
