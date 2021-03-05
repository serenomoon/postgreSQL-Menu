from logger_base import logger
from psycopg2 import pool
import sys

class Conexion:
    __HOST = '127.0.0.1'
    __DB_PORT = '5432'
    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __MIN_CON = 1
    __MAX_CON = 5
    __pool = None

    @classmethod
    def obtenerPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(cls.__MIN_CON,
                                                        cls.__MAX_CON,
                                                        host=cls.__HOST,
                                                        user=cls.__USERNAME,
                                                        password=cls.__PASSWORD,
                                                        database=cls.__DATABASE)
                logger.debug(f'Creacion de pool exitosa: {cls.__pool}')
                return cls.__pool
            except Exception as e:
                logger.debug(f'Error al crear el pool de conexiones: {e}')
                sys.exit()
        else:
            return cls.__pool

    @classmethod
    def obtenerConexion(cls):
        #obtener una conexion del pool
        conexion = cls.obtenerPool().getconn()
        logger.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        #regresar el objeto conexion al pool
        cls.obtenerPool().putconn(conexion)
        logger.debug(f'Regresamos la conexion al pool: {conexion}')
        logger.debug(f'Estado del pool: {cls.__pool}')

    @classmethod
    def cerrarConexiones(cls):
        #Cerrar pool y todas sus conexiones
        cls.obtenerPool().closeall()
        logger.debug(f'Cerramos todas las conexiones del pool: {cls.__pool}')
