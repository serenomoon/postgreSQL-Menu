from logger_base import logger
from conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None

    #inicion de with
    def __enter__(self):
        logger.debug(f'Inicion de with metodo __enter__')
        self.__conn = (Conexion.obtenerConexion())
        self.__cursor = self.__conn.cursor()
        return self.__cursor

    #fin del bloque with
    def __exit__(self,exception_type,exception_value,exception_traceback):
        logger.debug(f'Se ejecuta metodo __exit__')
        if exception_value:
            self.__conn.rollback
            logger.debug(f'Ocurrio una excepcion: {exception_value}')
        else:
            self.__cursor.close()
            self.__conn.commit()
            logger.debug(f'Commit de la transaccion')
        Conexion.liberarConexion(self.__conn)
