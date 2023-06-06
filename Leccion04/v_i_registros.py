import  psycopg2 # Esto es para conectarnos al postgre

conexion = psycopg2.connect(
    user='postgres',
    password='7875751m',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try :
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre , apellido, email) VALUES (%s, %s, %s)'
            valores = (
                ('Carlos', 'Lara', 'clara@gmail.com'),
                ('Marcos', 'canto','mcanto@gmail.com'),
                ('Marcelo', 'Cuenca','cuencaM@gmail.com')
            )#es una tupla
            cursor.executemany(sentencia,valores)  # de esta manera ejecutamos la sentencia
            #conexion.commit() se utiliza para guardar cambios en a base de datos
            registros_insertados = cursor.rowcount# Recuperamos todos los registros que seran una lista
            #registros = cursor.fetchone()
            print(f'Los registros insertados son : ´{registros_insertados}')

except Exception as e :
    print(f'Ocurrio un erro: {e}')
finally:
    conexion.close()
