from django import forms
from .models import Finished_Products_Model

class ProductForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Finished_Products_Model.objects.all())