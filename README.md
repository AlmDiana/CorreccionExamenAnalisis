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
Se necesita extraer datos de una página de Facebook y guardarlos en MongoDB
1. Realizamos el script para poder generar la base de datos con lo extraído desde Facebook y la palabra que buscamos
![2](https://user-images.githubusercontent.com/85883884/131435545-3b404ec9-f2c6-4db1-9d06-ecd099842dd0.png)
![3](https://user-images.githubusercontent.com/85883884/131435554-7413751d-d64b-4c06-88b1-9276ba385454.png)
![4](https://user-images.githubusercontent.com/85883884/131435567-f586045c-aab6-40bf-8d24-a3f048170e93.png)

2. Comprobamos en MongoDB qeu todos los datos se hayan guardado correctamente
![1](https://user-images.githubusercontent.com/85883884/131435616-c4a68aee-7f64-48d5-afcf-ff6e9fa63f55.png)
![5](https://user-images.githubusercontent.com/85883884/131436278-2b04593d-1090-4104-a345-520a6fd3d2e9.png)
![6](https://user-images.githubusercontent.com/85883884/131436291-78fae731-fa09-493c-954c-5834251f0ef9.png)
![7](https://user-images.githubusercontent.com/85883884/131436303-a2c9845e-0bbc-4c89-8518-f3e365da6c46.png)
![8](https://user-images.githubusercontent.com/85883884/131436314-9be9ecc9-2517-4e0b-bf12-0847f9cc3839.png)

# Ejercicio 5

1. Para este ejercicio haremos uso de la libreria tiktok-scraper y una carpeta donde guadaremos los csv generados.
2. Para descargar los datos, ingresaremos a la carpeta deseada e instanciaremos tiktok-scraper junto a su nombre de usuario, la funcion -t y el formato a descargar csv como se muestra en la imagen
![image](https://user-images.githubusercontent.com/66786471/131437651-6482c32d-42e5-4d18-9532-5be4095cf315.png)


3. Posteriormente mientras se vayan generando los csv, podemos ver como en la carpeta creada anteriormente, se van guardando los csv, esto permite ver de mejor manera que estructura tienes y permitira la utilizacion facilmente en un futuro

  ![Creacion de csv](https://user-images.githubusercontent.com/65979995/131438713-f473a84f-ecab-4bef-b4e5-a24bfcb3dc85.PNG)

4. 
![image](https://user-images.githubusercontent.com/66786471/131439398-af1294fa-a330-4d4b-a150-194fe0589481.png)

![image](https://user-images.githubusercontent.com/66786471/131439642-b212023e-3545-4efe-967b-da5d6cb3f270.png)

![image](https://user-images.githubusercontent.com/66786471/131439896-8b685b19-eaa3-4283-8826-de0edca47db8.png)

![image](https://user-images.githubusercontent.com/66786471/131440074-54f9aaa9-798a-413b-b64a-f2676acc8170.png)


# Ejercicio 6
1. Se genero la coleccion en donde se almacenaran los datos provenientes del CSV de MySQL, posteriormente se abrira la ventana donde se podra seleccionar los tipos de datos que se van a subir.

![image](https://user-images.githubusercontent.com/66786471/131441515-f28181da-7fd9-41af-a4da-e663b653188d.png)

![image](https://user-images.githubusercontent.com/66786471/131441670-66297698-13c1-45c8-bb98-aec7b461c466.png)

2.
3.

# Ejercicio 7
1. Para pasar los archivos de Couch DB a Mongo DB, se lo hizo manualmente, por lo tanto se tomó los archivos "juegoscorreccion" y "juegoscorreccion2" y se los guardó como archivo de tipo JSON.
![imagen](https://user-images.githubusercontent.com/58041267/131440760-93e5adce-1a50-42bc-80ef-7b0ad89e1e7e.png)
![imagen](https://user-images.githubusercontent.com/58041267/131440803-cf87a6fa-6f49-4d63-ac58-e8b57857b5f2.png)
![imagen](https://user-images.githubusercontent.com/58041267/131440878-21c454d7-4e00-47dc-868e-e94655face17.png)

2. Se crea una colección para guardar los archivos JSON mencionados en MongoB Compass y se comprueba.
![imagen](https://user-images.githubusercontent.com/58041267/131440960-14a8ea59-860d-4f43-9ecb-2b3167c92864.png)


