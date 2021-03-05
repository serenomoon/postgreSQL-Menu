import logging

logger = logging

logger.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S ',
                    handlers=[
                    logging.FileHandler('capa_datos.log'),
                    logging.StreamHandler()
                    ])

if __name__ == '__main__':
    logging.warning('mensaje a nivel warning')
    logging.info('mensaje a nivel info')
    logging.debug('mensaje a nivel debug')
    logging.error('Ocurrio un error en la base de datos')
    logging.debug('Se realizo la conexion con exito')
