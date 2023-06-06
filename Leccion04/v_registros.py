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
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s '#placeholder
            entrada = input('Digite los id_persona a buscar(Separados por comas) : ')
            llaves_primarias = (tuple(entrada.split(', ')),)
            cursor.execute(sentencia,llaves_primarias)  # de esta manera ejecutamos la sentencia
            registros = cursor.fetchall()# Recuperamos todos los registros que seran una lista
            #registros = cursor.fetchone()
            for registros in registros :
                print(registros)

except Exception as e :
    print(f'Ocurrio un erro: {e}')
finally:
    conexion.close()
