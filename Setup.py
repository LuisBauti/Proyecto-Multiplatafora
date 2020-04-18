# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################

import sys
import hashlib
import Principal
from Bd import Querys_logueo
from Pantallas import Acceso
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox

# Creamos la clase principal
class Lanzador (QMainWindow):
    def __init__(self, parent=None):
        super(Lanzador, self).__init__(parent)

        # Cargamos la interfaz echa en qt.
        self.ui = Acceso.Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectamos los elementos graficos con los metodos
        self.ui.Salir.clicked.connect(self.salir)
        self.ui.Aceptar.clicked.connect(self.ingresar_usuario)



     #Funcion para ingresar un usuario (Administrador, Usuario)
    def ingresar_usuario(self):
        nombre = self.ui.Usuario.text()
        if nombre == "":
            QMessageBox.about(self, "INFORMACION", "No has introducido ningun usuario")
        else:
            resultado = Querys_logueo.datos_usuarios(nombre)
            if resultado == []:
                QMessageBox.about(self, "INFORMACION", "No existe el usuario en la DB")
            else:
                self.contraseña_usuario(resultado)

    #Funcion para ingresar la contraseña y verificar si esta esta correcta.
    def contraseña_usuario(self, resultado):
        password = self.ui.Password.text()
        if password == "":
            QMessageBox.about(self, "INFORMACION", "No has introducido ninguna contraseña")
        else:
            
            contra = hashlib.sha512(password.encode())
            if contra.hexdigest() != resultado[0][2]:
                QMessageBox.about(self, "INFORMACION", "Contraseña incorrecta")
            else:
                self.permisos_usuario(resultado)


    #Funcion para agregar los permisos que va a tener el usuario(Administrador, Usuario) 
    def permisos_usuario(self, resultado):
        info_usuario = []
        info_usuario.append(resultado[0][1])
        info_usuario.append(resultado[0][2])
        info_usuario.append(resultado[0][3])
        self.close()
        ventana_principal = Principal.Ventana_principal(self, info_usuario)
        ventana_principal.show()

    #Funcion para salir.
    def salir(self):
        self.close()

# Codigo para lanzar la aplicacion
if __name__=="__main__":
    app = QApplication(sys.argv)
    ventana = Lanzador()
    ventana.show()
    sys.exit(app.exec_())