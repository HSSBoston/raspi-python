from openweather import *

weatherApiKey = ""

latitude = 40.5
longitude = -70.5
weatherData = getGpsWeather(latitude, longitude, "metric", weatherApiKey)
print("Location: " + str(latitude) + ", " + str(longitude))
description = getCurrentWeatherDescription(weatherData)
print("Weather description: " + description)

windSpeed, windDegrees, windGust = getCurrentWind(weatherData)
print("Wind speed (m/s): " + str(windSpeed) + \
      ", Wind direction (degrees): " + str(windDegrees) + \
      ", Wind gust (m/s): " + str(windGust))

uvi = getCurrentUvi(weatherData)
print("UV Index: " + str(uvi))

pressure = getCurrentAtmosphericPressure(weatherData)
print("Atomospheric pressure (hPa): " + str(pressure))
print("----------")


cityName = "Boston"
stateCode = "MA"
weatherData = getUsCityWeather(cityName, stateCode, "imperial", weatherApiKey)
print("Location: " + cityName + ", " + stateCode)
description = getCurrentWeatherDescription(weatherData)
print("Weather description: " + description)

windSpeed, windDegrees, windGust = getCurrentWind(weatherData)
print("Wind speed (miles/hr): " + str(windSpeed) + \
      ", Wind direction (degrees): " + str(windDegrees) + \
      ", Wind gust (miles/hr): " + str(windGust))

uvi = getCurrentUvi(weatherData)
print("UV Index: " + str(uvi))

pressure = getCurrentAtmosphericPressure(weatherData)
print("Atomospheric pressure (hPa): " + str(pressure))
print("----------")

townName = "Brookline"
stateCode = "MA"
weatherData = getUsTownWeather(townName, stateCode, "imperial", weatherApiKey)
print("Location: " + townName + ", " + stateCode)
description = getCurrentWeatherDescription(weatherData)
print("Weather description: " + description)

windSpeed, windDegrees, windGust = getCurrentWind(weatherData)
print("Wind speed (miles/hr): " + str(windSpeed) + \
      ", Wind direction (degrees): " + str(windDegrees) + \
      ", Wind gust (miles/hr): " + str(windGust))

uvi = getCurrentUvi(weatherData)
print("UV Index: " + str(uvi))

pressure = getCurrentAtmosphericPressure(weatherData)
print("Atomospheric pressure (hPa): " + str(pressure))
print("----------")

cityName = "Sagamihara"
countryCode = "JP"
weatherData = getIntlCityWeather(cityName, countryCode, "metric", weatherApiKey)
print("Location: " + cityName + ", " + countryCode)
description = getCurrentWeatherDescription(weatherData)
print("Weather description: " + description)

windSpeed, windDegrees, windGust = getCurrentWind(weatherData)
print("Wind speed (m/s): " + str(windSpeed) + \
      ", Wind direction (degrees): " + str(windDegrees) + \
      ", Wind gust (m/s): " + str(windGust))

uvi = getCurrentUvi(weatherData)
print("UV Index: " + str(uvi))

pressure = getCurrentAtmosphericPressure(weatherData)
print("Atomospheric pressure (hPa): " + str(pressure))


