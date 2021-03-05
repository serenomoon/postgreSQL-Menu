from logger_base import logger

class Usuario:
    def __init__(self, id_usuario=None, usuario=None, password=None):
        self.__id_usuario = id_usuario
        self.__usuario = usuario
        self.__password = password

    def __str__(self):
        return(
            f'Id Usuario: {self.__id_usuario}, '
            f'Usuario: {self.__usuario}, '
            f'Password: {self.__password}'
        )

    def get_id_usuario(self):
        return self.__id_usuario
    def set_id_usuario(self,id_usuario):
        self.__id_usuario = id_usuario

    def get_usuario(self):
        return self.__usuario
    def set_usuario(self,usuario):
        self.__usuario = usuario

    def get_password(self):
        return self.__password
    def set_password(self,password):
        self.__password = password
