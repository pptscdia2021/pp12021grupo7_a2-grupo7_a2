import pymongo
import pandas as pd

client = pymongo.MongoClient('localhost',27017)
db = client['mongo']
collection = db['income']

column_names_list = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'label', '_id']


with open('adult.data')as finput:
    for line in finput:
        row_list =line.rstrip('\n').split(',')
        row_dict = dict(zip(column_names_list,row_list))
        try:
            row_dict['age']= int(row_dict['age'])
            collection.insert_one(row_dict)
        except:
            pass


# devuelve la cantidad de registros
print(collection.estimated_document_count())

# encuentra un elemento de la coleccion 
age39 = collection.find_one({'age':{'$eq' : 39}}) #alternatively, {'age': 39} can be used
print(age39)

ing = collection.find_one({'education': ' Ingenieria'}) # Deberia devolver None
print(ing)

mydict = { 'age': 26, 'workclass': ' State-gov', 'fnlwgt': ' 79516', 'education': ' Ingenieria', 
          'education-num': ' 13', 'marital-status': ' Never-married', 'occupation': ' student', 
          'relationship': ' Not-in-family', 'race': ' black', 'sex': ' Male', 'capital-gain': ' 2174', 
          'capital-loss': ' 0', 'hours-per-week': ' 40', 'native-country': ' United-States', 'label': ' <=70K'}

x = collection.insert_one(mydict)

ing = collection.find_one({'education': ' Ingenieria'}) # Deberia devolver None
print(ing)

# elimina la coleccion
collection.drop()