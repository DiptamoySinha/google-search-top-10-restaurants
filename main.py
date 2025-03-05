from Util.restaurantsSearch import search
from Util.restaurantsSearch import dumpFile

city = input("Enter the name of the city: \n")

# google search for top 10 restaurants
res = search(city)

# dump the res into extract.json file
try:
    dumpFile('extractedData', res) #extractedData is folder name. 
    print('data is dumped into extract.json file') 
except Exception as e:
    print(e.with_traceback)


