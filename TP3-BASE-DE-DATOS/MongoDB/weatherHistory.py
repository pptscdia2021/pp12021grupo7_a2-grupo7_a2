import pymongo
import csv
import pandas as pd

#Conexión a MongoDB
client = pymongo.MongoClient('localhost',27017)
#db weatherHistory
db = client['weatherHistory']
#Colección
collection = db['weatherHistory']


# Function to parse csv to dictionary
reader = csv.DictReader(open('weatherHistory.csv'))
for row in reader:
    key = row.pop('Formatted Date')
    collection.insert_one(row)
    

# devuelve la cantidad de registros
print(collection.estimated_document_count())

# encuentra un elemento de la coleccion 
objeto1 = collection.find_one({ 'Humidity' : "0.89" })
print(objeto1)

# elimina la coleccion
collection.drop()