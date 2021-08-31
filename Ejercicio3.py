#!/usr/bin/env python
# coding: utf-8

# In[6]:


#importaciones y conexion a mongodb
from pymongo import MongoClient
myClient = MongoClient ('mongodb://localhost:27017/')
try:
    myClient.admin.command('ismaster')
    print('MongoDB connection: Conexión exitosa')
except ConnectionFailure as cf:
    print('MongoDB connection: Conexión fallida', cf)
    
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
import json
from bson.raw_bson import RawBSONDocument

def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))
 
response = requests.get('https://olympics.com/tokyo-2020/es/')
soup = BeautifulSoup(response.content, "lxml")

Sustantivos=[]


#Etiqueta
post_titles= soup.find_all("span", class_="tk-card__titlelink")


for element in post_titles:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Sustantivos.append(limpio.strip())


print(Sustantivos)

#se guarda en dataframe con pandas y se lo envia a mongodb
#archivo = pd.DataFrame(Sustantivos, index=Sustantivos)
#archivo.to_json('datosextraidos.json')
#Base de datos:
db = myClient["Correccion"]
Collection= db["Ejercicio3"]
    
Collection.insert_one({'Sustantivos': Sustantivos})


# In[ ]:




