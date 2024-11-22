# from logger_base import log
from psycopg2 import pool
import sys

class Conexion:

    _DATABASE = 'test_dentista'
    _HOST = '127.0.0.1'
    _USER = 'postgres'
    _PASSWORD = 'admin'
    _PORT = '5432'
    _MIN_CON = 1
    _MAC_CON = 5
    _pool = None


    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAC_CON,
                                                     host=cls._HOST,
                                                     port=cls._PORT,
                                                     database=cls._DATABASE,
                                                     user=cls._USER,
                                                     password=cls._PASSWORD)
                # log.debug(f'Pool de conexiones obtenido correctamente: {cls._pool}')
                return cls._pool

            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        # log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        # log.debug(f'Conexion liberada del pool: {conexion}')

    @classmethod
    def cerrarPool(cls):
        cls.obtenerPool().closeall()
        # log.debug(f'Pool de conexiones cerrado correctamente')
        cls._pool = None


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion2)
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    conexion6 = Conexion.obtenerConexion()

