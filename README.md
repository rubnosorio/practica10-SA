# Tarea No.6 del Laboratorio de Software Avanzado

## Ruben Osorio - 201407303


## Aplicacion flask 

### Conexion a bd y extraccion de datos
```sh 

    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'practica8'

    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    # ejecucion de consulta hacia la base de datos
    cursor.execute('SELECT * FROM cliente')
    # creacion de objeto donde se almacenara el contenido de la tabla
    results =  cursor.fetchall()
    data = ''
    for row in results:
      data += "Id = " +  str(row[0]) 
      data += "first name = " + str(row[1])
      data += "last name  = " + str(row[2])
      data += "email = " + str(row[3])
      data += "gender = " + str(row[4]) +  "\n"
    # se cierra el cursor
    cursor.close()
    # se cierra tambien con la conexion hacia la BD
    connection.close()
    # retorno del objeto con el contenido de la tabla
    return data

```
### Servir la pagina web y renderizar contenido


```sh 
# FUNCION de tipo get para mostrar los datos de la BD
@app.route('/')
def index():
    return data

```


## Archivo requeriments

Solo necesita indicar la version de flask y del conector de MySQL con python

```sh
Flask
mysql-connector
```

## Datos a cargar en MySQL

Los datos a cargar en mysql se encuentran en un archivo con el nombre init.sql en una carpeta con el nombre db la misma se le pasa como parametro de volumen de datos en el archivo docker-compose.yml

El contenido del archivo es el siguiente:

```sh
CREATE TABLE IF NOT EXISTS cliente(
   id         INTEGER  NOT NULL PRIMARY KEY 
  ,first_name VARCHAR(12) NOT NULL
  ,last_name  VARCHAR(15) NOT NULL
  ,email      VARCHAR(37) NOT NULL
  ,gender     VARCHAR(6) NOT NULL
  ,ip_address VARCHAR(15) NOT NULL
);
INSERT INTO cliente(id,first_name,last_name,email,gender,ip_address) VALUES (1,'Fenelia','McCurrie','fmccurrie0@sitemeter.com','Female','18.150.49.169');
INSERT INTO cliente(id,first_name,last_name,email,gender,ip_address) VALUES (2,'Mikel','Rainford','mrainford1@fema.gov','Male','76.21.75.12');
INSERT INTO cliente(id,first_name,last_name,email,gender,ip_address) VALUES (3,'Imogene','Bloxham','ibloxham2@dyndns.org','Female','238.165.241.180');
INSERT INTO cliente(id,first_name,last_name,email,gender,ip_address) VALUES (4,'Jojo','Facey','jfacey3@purevolume.com','Female','98.156.127.45');
INSERT INTO cliente(id,first_name,last_name,email,gender,ip_address) VALUES (5,'Baxter','Ruppeli','bruppeli4@purevolume.com','Male','34.192.190.56');

continua..

```


## Archivo Dockerfile

Este archivo se construye desde una imagen de python3.6 a la cual se le pasara y configurara todo lo necesario para el despligue de la aplicacion en flask y su conexion en mysql

El contenido del archivo es el siguiente:

```sh
# creacion de imagen de python 
FROM python:3.6

EXPOSE 80
# Configuro la carpeta de trabajo
WORKDIR /app
# copia todos los archivos a la carpeta app para la instalacion de flask y el conector y paso del proyecto
ADD . /app
# instalacion de los requeriemientos en la imagen
RUN pip install -r ./docker_app/requirements.txt
# configuracion del comando para correr la aplicacion
CMD python ./docker_app/Server.py
```


## Correr todo

Simplemente ubicando en la carpeta raiz de proyecto procedemos a abrir un terminal y escribir el comando.

```sh
docker-compose up -d
```
Nota:-d sirve para ejecute todo desde segundo plano sin necesidad de tener una terminal abierta.


## Video Demostracion de la aplicación

[![Ver en youtube]](https://youtu.be/xLrdV4S_UGs) 
