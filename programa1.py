import os
from numpy import empty 
import psycopg2
import time
import random

from pyparsing import Char 
try: 
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "3062887960313",
        dbname = "postgres"
    )
    print("Conectado")
except psycopg2.Error as e:
    print("Ocurrió un error en la conexión")
    print("Verifique")


dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
print(dado1,"+",dado2)

resultado = dado1 + dado2
cursor = conexion.cursor()
print("La suma es: ", resultado)

if resultado == 7 :
   
   input("Perdedor")
   cursor.execute("insert into p1(dado1,dado2,resultado) values(%s, %s,%s);",(dado1,dado2,resultado))
   conexion.commit()

elif resultado == 8 :
   
   input("Ganador")
   cursor.execute("insert into p1(dado1,dado2,resultado) values(%s, %s,%s);",(dado1,dado2,resultado))
   conexion.commit()
else:
    print("Juega de nuevo")
    cursor.execute("insert into p1(dado1,dado2,resultado) values(%s, %s,%s);",(dado1,dado2,resultado))
    conexion.commit()
    cursor.close()
    conexion.close()
   


