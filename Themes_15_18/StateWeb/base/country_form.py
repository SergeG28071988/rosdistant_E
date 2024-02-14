from django import forms
from .models import Country
from django.forms import ModelForm, TextInput, Textarea

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'area', 'population', 'city']
        