import psycopg2 as bd
# psycopg2 as bd-----otra menera de importar el psycopg2
from logger_base import log
import sys


class Conexion:
    _DATABASE= 'test_bd'
    _USERNAME = 'postgres'
    _PASSWORD = '7875751m'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    @classmethod
    def obternerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                log.debug(f'Conexcion exitosa : {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio un error de tipo : ´{e}')
                sys.exit()
        else:
         return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obternerConexion().cursor()
                log.debug(f'Se abrio correctamente el cursor : {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrion un error : {e}')
                sys.exit()
        else:
             return cls._cursor


if __name__ == '__main__':
    Conexion.obternerConexion()
    Conexion.obtenerCursor()