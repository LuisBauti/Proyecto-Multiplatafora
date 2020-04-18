# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################

import hashlib
from Bd import Query_ingreso_usuario
from PySide2.QtWidgets import QMessageBox

# Funcion para ingresar un nuevo usuario
def nuevo_ingreso(self):
    if self.ui.nuevo_usuario == "":
        QMessageBox.about(self,"INFORMACION", "No ingresaste el nombre")
    else:
        nombre = self.ui.nuevo_usuario.text()
        nuevo_ingreso_contra(self, nombre)

# Funcion para ingresar una contraseña
def nuevo_ingreso_contra(self, nombre):
    if self.ui.nuevo_contra == "":
        QMessageBox.about(self, "INFORMACION", "No ingresaste la contraseña")
    else:
        contra = self.ui.nuevo_contra.text()
        contra_enc = hashlib.sha512(contra.encode())
        contra_des = contra_enc.hexdigest()
        nuevo_ingreso_permisos(self, nombre, contra_des)

# Funcion para ingresar el permiso que tendra el nuevo usuario
def nuevo_ingreso_permisos(self, nombre, contra_des ):
    if self.ui.permiso_usuario.isChecked():
        permisos = 0
    elif self.ui.permiso_admin.isChecked():
        permisos = 1
    informacion = []
    informacion.append(nombre)
    informacion.append(contra_des)
    informacion.append(permisos)
    Query_ingreso_usuario.ingreso_usuario_nuevo(informacion)


