import gpsserial as gps
from geopy.geocoders import Nominatim
import requests, csv, os
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
        
        county = address["county"]
        countyStrlist = county.split()
        county = countyStrlist[0]
        
        state = address["state"]
        stateCounty = state + ", " + county
        pviDate = "20220122"
        fileName = "Model_12.4_" + pviDate +"_results.csv"
        url = "https://raw.githubusercontent.com/COVID19PVI/data/master/Model12.4/" + fileName
        fields = []
        rows = []

        if not os.path.isfile(fileName):
            r = requests.get(url, allow_redirects=True)
            open(fileName, "wb").write(r.content)
            print("Downloaded and saved a PVI data file: " + fileName)

        with open(fileName, "r") as csvFile:
            csvReader = csv.reader(csvFile)      
            # Read the first row to extract field names
            fields = next(csvReader)
            # Extract the remaining rows
            for row in csvReader:
                rows.append(row)
            totalRowCount = csvReader.line_num - 1
            print("Parsed " + fileName + ". Total # of rows (counties): " + str(totalRowCount) )
       
        for index, row in enumerate(rows):
            if row[3] == stateCounty:
                print(stateCounty, end=" ")
                print("PVI: " + row[0], end=" ")
                rank = index/totalRowCount
                print("Risk rank: " + str(rank))

    except KeyboardInterrupt:
        break
gpsSerialPort.close()