import numpy
import psycopg2
import statistics as stat


import psycopg2
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


nota1=int(input("primer nota: "))
nota2=int(input("segundada nota: "))
nota3=int(input("tercera nota: "))
nota4=int(input("cuarta nota: "))
nota5=int(input("quinta nota: "))
cursor = conexion.cursor()
arreglo=[nota1,nota2,nota3,nota4,nota5]
media=numpy.mean(arreglo)
mediana=numpy.median(arreglo)   
moda=stat.mode(arreglo)
maximo=max(arreglo)
minimo=min(arreglo)
rango=maximo-minimo
desvest=numpy.std(arreglo)
varianza=numpy.var(arreglo)
print("La media es: ",media)
print("La media es: ",mediana) 
print("La moda es: ",moda)
print("El rango es: ",rango)
print("La varianza es: ",varianza)
print("La desviación estándar es: ",desvest)
cursor.execute("insert into p2(media, mediana, moda, rango, desviacion, varianza) values(%s, %s,%s, %s,%s, %s);",(media,mediana,moda,rango,desvest,varianza))
conexion.commit()
cursor.close()
conexion.close()

