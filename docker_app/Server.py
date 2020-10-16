# import del manejo de listas
from typing import List, Dict
# import para el funcionamiento general de flask
from flask import Flask
# import de conexion con mysql
import mysql.connector
# import para el manejo de variables tipo json
import json  


app = Flask(__name__)  # creacion de la app en python de flask


def clientes() -> List[Dict]:
    # Variable utilizada para la conexion con la base de datos
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'practica8'
    }
    # variable de la conexion con la base de datos
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

# FUNCION de tipo get para mostrar los datos de la BD
@app.route('/')
def index():
    return clientes()


if __name__ == '__main__':
    # comando para configurar la ip del servicio
    app.run(host='0.0.0.0')
