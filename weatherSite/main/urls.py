from django.urls import path
from . import views



urlpatterns = [
    path('', views.weather_tab, name="main"),
    path('weather/', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('check_weather/', views.new_weather, name="new_weather"),
    path('add_weather/', views.add_weather, name="Check_weather"),
    path('weather/<int:id>/delete', views.weather_delete, name="Delete_weather")
]