from .models import Weather
from django.forms import ModelForm, TextInput, Textarea, NumberInput


class WeatherForm(ModelForm):
    class Meta:
        model = Weather
        fields =['cityName']
        widgets = {
            'cityName': TextInput(attrs={
                'class': 'format-control',
                'placeholder': 'Add city name'
            })
        }