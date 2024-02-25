# =================================================================================
# Reading CSV File and fetching the data from Dictionary Data Type for the items
# =================================================================================
import json

csvFilePath = "products.csv"
csvFile = open("products.csv", "r")
print(csvFile.readlines())
print(f'Reading CSV File -: ')
csvFileListData = []
csvDictionaryData, dictionaryForJsonData = {}, {}
# Loop through the list of lines
try:
    with open(csvFilePath, 'r') as file:
        for line in file.readlines():
            print(line.strip())
            productId, name, price, inStock = line.strip().split(',')
            csvDictionaryData = {
                'productId': productId,
                'name': name,
                'price': price,
                'inStock': inStock
            }
            csvFileListData.append(csvDictionaryData)
    print(f'CSV File List Data is - {csvFileListData}')
    print(csvFileListData[0]['price'])
    print(f'Dictionary Data prepared from the CSV File Data -: {dictionaryForJsonData}')
except FileNotFoundError as Fnfe:
    print(Fnfe)
except RuntimeError as Rte:
    print(Rte)
else:
    print('Everything went well while reading the data from a text file.')  # will run when there is no execption.
finally:
    print('I will be executed every time in both case of program failure or program success!')

json_data = json.dumps(csvFileListData, indent=2)
print(f'Below is the JSON Data - ')
print(json_data)

# =====================================
# dumping the data out to a JSON file
# =====================================
dumpedJsonFileOfCsvDataFile = open("dumpedJsonFileOfCsvData.json", "w")
csvFileListData = {item["productId"]: item for item in csvFileListData}
print(csvFileListData)
json.dump(csvFileListData, dumpedJsonFileOfCsvDataFile, indent=2)