# Correccion del Examen - Analisis de Datos

# Ejercicio 1
Script 1 : "Ejercicio1.py" Contiene la cosecha de datos de Twitter en base a la localización de 3 ciudades donde se realizan los juegos olímpicos, las 3 ciudades elegidas fueron: Shibuya, Izu, Koto.Para este ejercicio se colocó las credenciales de una cuenta de Twitter Developer. En el código se obtiene los datos provenientes de Twitter útiles para la conexión con CouchDB.
A continuación una captura de confirmación de guardado en la base de datos "juegoscorreccion" de CouchDB y su vista en CouchDB: 
![imagen](https://user-images.githubusercontent.com/58041267/131422008-be485f8e-fcd5-491b-ba31-51291e358769.png)
![imagen](https://user-images.githubusercontent.com/58041267/131423123-21de1608-d843-4684-b32c-13806e504246.png)

# Ejercicio 2
Script 2 : "Ejercicio2.py" Contiene la cosecha de datos de Twitter en base a un track de palabras clases relacionadas con los juegos olímpicos, las palabras usadas fueron: 'juegosolimpicos','olimpiadas2021', 'juegos2021','Tokioolimpiadas'. Para este ejercicio se colocó las credenciales de una cuenta de Twitter Developer. En el código se obtiene los datos provenientes de Twitter útiles para la conexión con CouchDB.
A continuación una captura de confirmación de guardado en la base de datos "juegoscorreccion2" de CouchDB y su vista en CouchDB:
![imagen](https://user-images.githubusercontent.com/58041267/131424071-46e93ca4-c943-4d02-a007-68e44004a938.png)
![imagen](https://user-images.githubusercontent.com/58041267/131424613-e1b11846-4a10-4eea-8deb-c5dfbecec373.png)


# Ejercicio 3
Script 3 : "Ejercicio3.py" A continuación se detalla el proceso que se realizó para completar este ejercicio:
1.  Desde Mongo DB Atlas conectarse a MongoDB Compass:
![imagen](https://user-images.githubusercontent.com/58041267/131428437-9706bc17-972a-41a0-ba2d-a378efb4cd7b.png)
![imagen](https://user-images.githubusercontent.com/58041267/131428772-25428b1f-6d27-469d-8ba4-43ae3dcd0274.png)
2. 
3.  
Se empieza realizando la conexion con mongodb por medio de pymongo, se muestra el mensaje de si se realizo correctamente la conexion o no. Se importan las herramientas necesarias y se generan las funciones que permitiran limpiar las etiquetas. Usamos el request para obtener los datos html y posteriormente se los limpia con un for el cual guardara los datos limpiados en Titles, una vez realizado esto se lo guarada como json y se lo manda a la BD y coleccion previamente creadas.

#Ejercicio 5
Se presentara  a continucacion la creacion de los CSV referentes a TIkTok para su posterior carga a MySQL
1.- Se abre un terminal, en donde  se ejecutan los siguientes comandos
![parte 5 tiktok 1 - CSV_ primera_pag_tiktok](https://user-images.githubusercontent.com/65979995/131430748-a69f8a2b-ad83-4d08-8120-47b44df11b17.png)
2.- Esperamos a que se generen los CSV para poder ver su posterior ubicacion en la carpeta CSV tiktok
![Creacion de csv](https://user-images.githubusercontent.com/65979995/131430914-ce52afe5-aac2-43b0-b2a2-737c78aeb671.PNG)


