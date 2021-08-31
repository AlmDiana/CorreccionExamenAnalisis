#!/usr/bin/env python
# coding: utf-8

# In[2]:


from facebook_scraper import get_posts
import json
import time
from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017") 
 
try:
    myclient.admin.command('ismaster')
    print('MongoDB connection: Conexion exitosa')
except ConnectionFailure as cf:
    print('MongoDB connection: Conexion fallida', cf)
    

db=myclient['Correccion_examen_analisis_de_datos']
collection= db['4']

i=1
for post in get_posts('tokyo2020', pages=100, extra_info=True):
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
        collection.insert_one(doc)

    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))


# In[ ]:




