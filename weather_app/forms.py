from django.db.models import fields
from django.forms import (
    ModelForm, 
    TextInput
)

from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        exclude = ('user',)
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'city', 
            'id': 'city',
            'placeholder': 'Введите город'
        })}
