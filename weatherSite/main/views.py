from datetime import date
from django.shortcuts import render, redirect

from .models import Weather
from .apiOperations import *

from .forms import WeatherForm

def new_weather(request):
    cityName = request.GET.get('name')
    weatherInfo = getWeather(cityName)
    obj = Weather.objects.create(
        cityName=getCityName(weatherInfo),
        temperature=getTemperature(weatherInfo),
        feels_like_temperature=getFeelsLikeTemperature(weatherInfo),
        sky=getCloudStatus(weatherInfo),
        time=date.today()
    )
    obj.save()

    weather = Weather.objects.order_by('-auto_increment_id')
    return render(request, 'main/index_tab.html', {'title': 'Main page', 'weather': weather})

def index(request):
    weather = Weather.objects.all()
    return render(request, 'main/index.html', {'title': 'Main page', 'weather': weather})


def about(request):
    return render(request, 'main/about.html')

def add_weather(request):
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            weatherInfo = getWeather(form.cleaned_data['cityName'])
            obj = Weather.objects.create(
                cityName=getCityName(weatherInfo),
                temperature=getTemperature(weatherInfo),
                feels_like_temperature=getFeelsLikeTemperature(weatherInfo),
                sky=getCloudStatus(weatherInfo),
                time=date.today()
            )
            obj.save()
            return redirect('home')

    form = WeatherForm()
    context = {
        'form': form
    }
    return render(request, 'main/add_weather.html', context)

def weather_tab(request):
    weather = Weather.objects.all()
    return render(request, 'main/index_tab.html', {'title': 'List of weather', 'weather': weather})

def weather_delete(request, id=0):
    weather = Weather.objects.get(auto_increment_id=id)
    weather.delete()
    weather = Weather.objects.all()
    return render(request, 'main/index_tab.html', {'title': 'Main page', 'weather': weather})
