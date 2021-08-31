# Correccion del Examen - Analisis de Datos
Integrantes: 

- Diana Almeida


- Mateo Cevallos


- Josué Singaña


- Christian Soledispa

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
A continuación se detalla el proceso que se realizó para completar este ejercicio:
1.  Desde Mongo DB Atlas conectarse a MongoDB Compass y creación de Base de datos "Corrección" y de la colección "Ejercicio3":
![imagen](https://user-images.githubusercontent.com/58041267/131428437-9706bc17-972a-41a0-ba2d-a378efb4cd7b.png)
![imagen](https://user-images.githubusercontent.com/58041267/131428772-25428b1f-6d27-469d-8ba4-43ae3dcd0274.png)
![imagen](https://user-images.githubusercontent.com/58041267/131429903-596a977a-b8fe-4548-b940-725fc775b470.png)

2. Conexión con MongoDB por medio de pymongo, el código se encuentra en el Script 3 : "Ejercicio3.py" donde inicialmente se obtiene los datos html, se filtra por etiqueta y finalmente se guarda en la base de datos y colección creadas previamente. A continuación, se presenta el mensaje de conexión exitosa y aparece el archivo insertado en MongoDB Compass dentro de la base de datos y colección establecidas.
![imagen](https://user-images.githubusercontent.com/58041267/131431688-74b767d0-6861-40da-9349-ce7c4a7631ae.png)
![imagen](https://user-images.githubusercontent.com/58041267/131432307-a6f44c74-e882-49bb-9add-552d7b5e5bff.png)

# Ejercicio 4
