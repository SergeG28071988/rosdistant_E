from django import forms
from .models import City
from django.forms import ModelForm, TextInput, Textarea

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'population']
        