import json
# =================================================================================
# Reading Text File and fetching the data from Dictionary Data Type for the items
# =================================================================================
textFilePath = "products1.txt"
textFile = open("products1.txt", "r")
print(textFile.readlines())

print(f'Reading Text File -: ')
textFileListData = []
dictionaryData = {}
# Loop through the list of lines
try:
    with open(textFilePath, 'r') as file:
        for line in file.readlines():
            print(line.strip())
            productId, name, price, inStock = line.strip().split(',')
            textDictionaryData = {
                'productId': productId,
                'name': name,
                'price': price,
                'inStock': inStock
            }
            textFileListData.append(textDictionaryData)
    print(f'Text File List Data is - {textFileListData}')
    print(textFileListData[0]['price'])
except FileNotFoundError as Fnfe:
    print(Fnfe)
except RuntimeError as Rte:
    print(Rte)
else:
    print('Everything went well while reading the data from a text file.')  # will run when there is no execption.
finally:
    print('I will be executed every time in both case of program failure or program success!')


