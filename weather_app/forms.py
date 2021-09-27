from django.db.models.fields import TextField
from django.forms import (
    ModelForm, 
    TextInput,
    CharField,
    Textarea
)

from .models import City, Support

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'city', 
            'id': 'city',
            'placeholder': 'Введите город'
        })}

class SupportForm(ModelForm):
    title = CharField(max_length=100, widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'title',
        'name': 'title',
        'placeholder': 'Придумайте название темы',
        'style': 'min-width: 100%;'
    }))
    text = CharField(max_length=3000, widget=Textarea(attrs={
        'class': 'form-control mt-2',
        'id': 'text',
        'name': 'text',
        'placeholder': 'Опишите проблему',
        'style': 'resize: both; min-width:100%;'
    }))

    class Meta:
        model = Support
        exclude = ('title', 'text',)