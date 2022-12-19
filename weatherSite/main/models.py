from django.db import models

class Weather(models.Model):
    cityName = models.CharField('City name', max_length=50)
    temperature = models.CharField('temperature', max_length=50)
    feels_like_temperature = models.CharField('feels_like temperature', max_length=50)
    sky = models.CharField('sky', max_length=50)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    auto_increment_id = models.AutoField(primary_key=True)

def __str__(self):
    return self.auto_increment_id