#!/usr/bin/env python
# coding: utf-8

# In[18]:


#importaciones
from facebook_scraper import get_posts
import json
import time
import pymongo
from pymongo import MongoClient

#conexion con mongodb
myclient =pymongo.MongoClient("mongodb://localhost:27017")
try:
    myclient.admin.command('ismaster')
    print('MongoDB connection: Conexion exitosa')
except ConnectionFailure as cf:
    print('MongoDB connection: Conexion fallida', cf)

try:
    db = myclient["Correccion"]
    collection= db["Ejercicio4"]
except:
    db = myclient["Correccion"]
    collection= db["Ejercicio4"]
    
#funcion para guardar en mongodb
i=1
for post in get_posts("olympics", pages=50, extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
    
    doc['id']=id
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}
        
        doc['post_url']=post['post_url']
        collection.save(doc)
        
        print('Guardado con exito')
    except Exception as e:
        print('No se pudo guardar:'+str(e))


# In[ ]:





# In[ ]:




