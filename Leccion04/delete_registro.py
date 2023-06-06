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
            sentencia = 'DELETE FROM persona WHERE id_persona = %s '
            entrada = input('Digite el numero de registro a eliminar: ')
            valores = (entrada ,)#Esto es una tupla de valores
            cursor.execute(sentencia,valores)  # de esta manera ejecutamos la sentencia

            registros_eliminados = cursor.rowcount# Recuperamos todos los registros que seran una lista
            #registros = cursor.fetchone()
            print(f'Los registros eliminados son : ´{registros_eliminados}')

except Exception as e :
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()