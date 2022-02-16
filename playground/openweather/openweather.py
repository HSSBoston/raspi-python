# Library to access and use OpenWeatherMap
# January 2, 2022 v0.01
# Jun Suzuki (https://github.com/jxsboston)
# IoT for Kids: https://jxsboston.github.io/IoT-Kids/

import requests, json, os
from geopy.geocoders import Nominatim

nominatimAppName = "iot" + os.uname()[1]
geolocator = Nominatim(user_agent=nominatimAppName)

def getGpsWeather(lat, lon, unit, apiKey):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=" + \
              str(lat) + "&lon=" + str(lon) + \
              "&exclude=minutely,hourly,daily" + \
              "&appid=" + apiKey + "&units=" + unit
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None

def getUsCityWeather(cityName, stateCode, unit, apiKey):
    structuredQuery = {"city" : cityName,
                       "state" : stateCode,
                       "country" : "United States"}
    location = geolocator.geocode(query=structuredQuery)
    locationDataset = location.raw
    return getGpsWeather(locationDataset["lat"], locationDataset["lon"], unit, apiKey)


def getUsTownWeather(townName, stateCode, unit, apiKey):
    structuredQuery = {"town" : townName,
                       "state" : stateCode,
                       "country" : "United States"}
    location = geolocator.geocode(query=structuredQuery)
    locationDataset = location.raw
    return getGpsWeather(locationDataset["lat"], locationDataset["lon"], unit, apiKey)

def getIntlCityWeather(cityName, countryCode, unit, apiKey):
    structuredQuery = {"city" : cityName,
                       "country" : countryCode}
    location = geolocator.geocode(query=structuredQuery)
    locationDataset = location.raw
    return getGpsWeather(locationDataset["lat"], locationDataset["lon"], unit, apiKey)

def getCurrentTempHumidity(response): 
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            temp = currentDict["temp"]
            feelsLike = currentDict["feels_like"]
            humidity = currentDict["humidity"]
            return (temp, feelsLike, humidity)
        else:
            return (None, None, None)
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))

def getCurrentRain(response): 
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            if "rain" in currentDict:
                rainDict = currentDict["rain"]
                rain1h = rainDict["rain.1h"]
                return rain1h
            else:
                return None
        else:
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None

def getCurrentSnow(response): 
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            if "snow" in currentDict:
                rainDict = currentDict["snow"]
                snow1h = rainDict["snow.1h"]
                return snow1h
            else:
                return None
        else:
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None

def getCurrentWind(response): 
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            if "wind_speed" in currentDict:
                windSpeed = currentDict["wind_speed"]
            else:
                windSpeed = None
            if "wind_deg" in currentDict:
                windDeg = currentDict["wind_deg"]
            else:
                windDeg = None
            if "wind_gust" in currentDict:
                windGust = currentDict["wind_gust"]
            else:
                windGust = None
            return (windSpeed, windDeg, windGust)
        else:
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None

def getCurrentWeatherDescription(response): 
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            if "weather" in currentDict:
                weatherDict = currentDict["weather"][0]
                if "description" in weatherDict:
                    return weatherDict["description"]
                else:
                    return None
            else:
                return None
        else:
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None

def getCurrentAtmosphericPressure(response): 
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            if "pressure" in currentDict:
                return currentDict["pressure"]
            else:
                return None
        else:
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None

def getCurrentUvi(response): 
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            if "uvi" in currentDict:
                return currentDict["uvi"]
            else:
                return None
        else:
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None


