from logger_base import logger
from usuariodao import UsuarioDao
from usuario import Usuario

def menu():
    eleccion = ''
    while eleccion != "5":
        print('''
Bienvenido al Menu de Usuarios
1-Ver lista de usuarios
2-Agregar usuario
3-Actualizar usuario
4-Eliminar usuario
5-Salir
-------------------------------------------------------
        ''')
        eleccion = input("Seleccione que accion desea ejecutar: ")
        #VER USUARIOS
        if eleccion == "1":
            usuarios = UsuarioDao.seleccionar()
            for usuario in usuarios:
                logger.info(usuario)

        #INSERTAR USUARIO
        if eleccion == "2":
            nombre = input("Escriba el nombre de usuario: ")
            password = input("Escriba su contraseña: ")
            usuario = Usuario(usuario= nombre, password= password)
            usuarios_insertados = UsuarioDao.insertar(usuario)
            print("Usuario ingresado con exito.")
            print("---------------------------------------------")

        #ACTUALIZAR USUARIO
        if eleccion == "3":
            id = input("Ingrese el id del usuario a actualizar: ")
            nombre = input("Ingrese el nuevo nombre de usuario: ")
            password = input("Ingrese el nuevo password: ")
            usuario = Usuario(id,nombre,password)
            usuario_actualizado = UsuarioDao.actualizar(usuario)
            print("Usuario actualizado con exito.")
            print("---------------------------------------------")

        #ELIMINAR USUARIO
        if eleccion == "4":
            id = input("Ingrese el ID del usuario a eliminar: ")
            usuario = Usuario(id)
            usuario_eliminado = UsuarioDao.eliminar(usuario)
            print("Usuario eliminado con exito.")
            print("---------------------------------------------")

        else:
            print("Esa opcion no esta disponible")
            ("---------------------------------------------")

menu()
