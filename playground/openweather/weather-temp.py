from openweather import *

weatherApiKey = ""

latitude = 42.3656
longitude = -71.0096
weatherData = getGpsWeather(latitude, longitude, "metric", weatherApiKey)
temp, feelsLike, humidity = getCurrentTempHumidity(weatherData)
print("Lat: " + str(latitude) + ", Lon: " + str(longitude))
print("Temp (C): " + str(temp) + ", Feels like (C): " + str(feelsLike) + \
      ", Humidity (%): " + str(humidity))
print("----------")

cityName = "Boston"
stateCode = "MA"
weatherData = getUsCityWeather(cityName, stateCode, "imperial", weatherApiKey)
temp, feelsLike, humidity = getCurrentTempHumidity(weatherData)
print(cityName + ", " + stateCode)
print("Temp (F): " + str(temp) + ", Feels like (F): " + str(feelsLike) + \
      ", Humidity (%): " + str(humidity))
print("----------")

townName = "Brookline"
stateCode = "MA"
weatherData = getUsTownWeather(townName, stateCode, "imperial", weatherApiKey)
temp, feelsLike, humidity = getCurrentTempHumidity(weatherData)
print(townName + ", " + stateCode)
print("Temp (F): " + str(temp) + ", Feels like (F): " + str(feelsLike) + \
      ", Humidity (%): " + str(humidity))
print("----------")

cityName = "Sagamihara"
countryCode = "JP"
weatherData = getIntlCityWeather(cityName, countryCode, "metric", weatherApiKey)
temp, feelsLike, humidity = getCurrentTempHumidity(weatherData)
print(cityName + ", " + countryCode)
print("Temp (C): " + str(temp) + ", Feels like (C): " + str(feelsLike) + \
      ", Humidity (%): " + str(humidity))
