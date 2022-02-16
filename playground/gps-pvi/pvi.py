import requests, csv, os

# Fields in each row:
#
# "ToxPi Score", <== PVI 
# "HClust Group",
# "KMeans Group",
# "Name", <== "State, County" (e.g. "Massachusetts, Middlesex")
# "Source",
# "Infection Rate: Transmissible Cases!20!0xcc3333ff",
# "Infection Rate: Disease Spread!5!0xe64d4dff",
# "Pop Concentration: Pop Mobility!10!0x57b757ff",
# "Pop Concentration: Residential Density!5!0x5ced5cff",
# "Intervention: Vaccines!15!0x4258c9ff",
# "Intervention: Social Distancing!5!0x6079f7ff",
# "Intervention: Testing!5!0x7d90f3ff",
# "Health & Environment: Hospital Beds!10!0x6b0b9eff",
# "Health & Environment: Hospital Ventilators!10!0x7e24aeff",
# "Health & Environment: Pop Demographics!3!0x933fbfff",
# "Health & Environment: Air Pollution!3!0xa95ad2ff",
# "Health & Environment: Age Distribution!3!0xc177e7ff",
# "Health & Environment: Co-morbidities!3!0xdb95feff",
# "Health & Environment: Health Disparities!3!0xe1a6ffff"

pviDate = "20220122"

county = "Middlesex"
state = "Massachusetts"
stateCounty = state + ", " + county

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
    print("Parsed " + fileName + ". Total # of rows (counties): " + str(totalRowCount))
  
for index, row in enumerate(rows):
    if row[3] == stateCounty:
        print(stateCounty, end=" ")
        print("PVI: " + row[0], end=" ")
        rank = index/totalRowCount
        print("Risk rank: " + str(rank))