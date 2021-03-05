from usuario import Usuario
from cursor_pool import CursorDelPool
from logger_base import logger

class UsuarioDao:
    __SELECCIONAR = 'SELECT * FROM usuarios ORDER BY id_usuario'
    __INSERTAR = 'INSERT INTO usuarios(usuario,password) VALUES(%s,%s)'
    __ACTUALIZAR = 'UPDATE usuarios SET usuario=%s, password=%s WHERE id_usuario = %s'
    __ELIMINAR = 'DELETE FROM usuarios WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls,usuario):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.get_usuario(),usuario.get_password())
            cursor.execute(cls.__INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.get_usuario(),usuario.get_password(),usuario.get_id_usuario())
            cursor.execute(cls.__ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls,usuario):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.get_id_usuario(),)
            cursor.execute(cls.__ELIMINAR, valores)
            return cursor.rowcount


#if __name__ == '__main__':
    #Listado de usuarios
    #usuarios = UsuarioDao.seleccionar()
    #for usuario in usuarios:
    #    logger.debug(usuario)

    #insertamos nuevo registro
    #usuario = Usuario(usuario= 'Saulo', password= '456')
    #usuarios_insertados = UsuarioDao.insertar(usuario)
    #logger.debug(f'Usuarios insertados: {usuarios_insertados}')

    #actualizar un registro
    #persona = Usuario(3,'Jorgelina1','321')
    #personas_actualizadas = UsuarioDao.actualizar(persona)
    #logger.debug(f'personas actualizadas: {personas_actualizadas}')

    #eliminar un registro
    #persona = Persona(12)
    #personas_eliminadas = PersonaDao.eliminar(persona)
    #logger.debug(f'personas eliminadas: {personas_eliminadas}')
