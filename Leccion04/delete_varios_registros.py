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
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s '
            entrada = input('Digite los numero de registro a eliminar(Separados por comas ): ')
            valores =(tuple (entrada.split(',')),)#tUPLA DE TUPLA
            cursor.execute(sentencia,valores)  # de esta manera ejecutamos la sentencia

            registros_eliminados = cursor.rowcount# Recuperamos todos los registros que seran una lista
            #registros = cursor.fetchone()
            print(f'Los registros eliminados son : ´{registros_eliminados}')

except Exception as e :
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()