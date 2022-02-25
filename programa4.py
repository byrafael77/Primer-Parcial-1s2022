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


n=int(input("Ingrese un número: "))
cursor = conexion.cursor()
if n <= 0:
    print("El número debe ser mayor que cero")
else:
    cant_divisores = 0
    i = 1
    while (i <= n):
        if n % i == 0:
            cant_divisores+=1
        i+=1
    if cant_divisores==2:
        print("El número es primo")
        res = "Número primo"
        cursor.execute("insert into p4(numero, respuesta) values(%s, %s);",(n, res))
        conexion.commit()
    else:
        print("El número es compuesto")
        res = "Número compuesto"
        cursor.execute("insert into p4(numero, respuesta) values(%s, %s);",(n, res))
        conexion.commit()
        cursor.close()
        conexion.close()