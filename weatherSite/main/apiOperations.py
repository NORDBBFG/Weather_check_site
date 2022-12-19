import requests
import re

def getWeather(siity = "Kyiv") :
    restReq = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={siity}&appid=f9be53a807681d57676f98510dbfa870&units=metric")
    return restReq.text

def getCityName(forregex) :
    match = re.findall(r'name([^<>]+)cod', forregex)
    match1 = re.sub('[^a-zA-Z ]', "", match[0])
    return match1.strip()

def getTemperature(forregex) :
    match = re.findall(r'temp([^<>]+)feels_like', forregex)
    match1 = re.sub('[^-.0-9]', "", match[0])
    return match1.strip()

def getFeelsLikeTemperature(forregex) :
    match = re.findall(r'feels_like([^<>]+)temp_min', forregex)
    match1 = re.sub('[^-.0-9]', "", match[0])
    return match1.strip()

def getCloudStatus(forregex) :
    match = re.findall(r'description([^<>]+)icon', forregex)
    match1 = re.sub('[^a-z ]', "", match[0])
    return match1.strip()