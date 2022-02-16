import gpsserial as gps
from geopy.geocoders import Nominatim

serialPort = "/dev/serial0"
gpsSerialPort = gps.init(serialPort)

appName = "jwst-demo-panda"
geolocator = Nominatim(user_agent=appName)


while True:
    try:
        gpsData = gps.getData(gpsSerialPort)
        print(gpsData)

        lat = gps.getLatitude(gpsData)
        lon = gps.getLongitude(gpsData)
        print("Raw latitude: " + lat + ", Raw longitude: " + lon)
        
        decimalLat = gps.getDecimalLatitude(gpsData)
        decimalLon = gps.getDecimalLongitude(gpsData)
        print("Decimal latitude: " + str(decimalLat) + ", Decimal longtitude: " + str(decimalLon))

        gMapsLink = "https://www.google.com/maps?q=" + str(decimalLat) + "," + str(decimalLon)
        print("Google Maps link: " + gMapsLink)
            
        location = geolocator.reverse( query=(decimalLat, decimalLon ) )
        print(location.address)

        print("")


        locationDataset = location.raw
        address = locationDataset["address"]
        if "city" in address:
            print(address["city"])
        if "town" in address:
            print(address["town"])
        print(address["county"])
        print(address["state"])
        print(address["postcode"])
        print(address["country"])
        print(locationDataset)
        
    except KeyboardInterrupt:
        break
gpsSerialPort.close()