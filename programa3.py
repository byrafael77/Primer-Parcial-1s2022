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

def calcular():
    precio = float(input("Ingrese el precio: "))
    cursor = conexion.cursor()

    siniva = (precio/1.12)
    iva = precio - siniva
    print("El precio sin iva es: ",siniva)
    cursor.execute("insert into p3(ejercicio,siniva,coniva) values(%s, %s,%s);",(precio,siniva,iva))
    conexion.commit()

    print("El iva es: ",iva)
    cursor.execute("insert into p3(ejercicio,siniva,coniva) values(%s, %s,%s);",(precio,siniva,iva))
    conexion.commit()

calcular()