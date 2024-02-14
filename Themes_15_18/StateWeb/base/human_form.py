from django import forms
from .models import Human
from django.forms import ModelForm, TextInput, Textarea

class HumanForm(ModelForm):
    class Meta:
        model = Human
        fields = ['name', 'surname', 'date_birth', 'place_residence']
        
