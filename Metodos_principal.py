# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################

from Bd import Query_principal
import sqlite3
from PySide2.QtWidgets import QMessageBox
from Pantallas import Limpiar_interfaz

from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import QByteArray, QIODevice, QBuffer

# Llenar combo municipio
def llenar_combo_municipio(self):
    self.ui.combo_municipio.clear()
    self.ui.combo_municipio.addItem("Selecciona un municipio")
    resultado = Query_principal.obtener_municipio()
    for i in range(len(resultado)):
        self.ui.combo_municipio.addItem(resultado[i][0])

# Llenar combo candidato
def llenar_combo_candidato(self):
    try:
        self.ui.combo_candidato.clear()
        self.ui.combo_candidato.addItem("Selecciona un candidato")
        id_municipio = self.ui.combo_municipio.currentIndex()
        if id_municipio == 0:
            pass
        else:
            combo_text = self.ui.combo_municipio.currentText()
            resultado = Query_principal.obtener_id_municipio(combo_text)
            resultado_candidato = Query_principal.obtener_candidato(resultado[0][0])
            for i in range(len(resultado_candidato)):
                self.ui.combo_candidato.addItem(resultado_candidato[i][0])
    except IndexError:
        pass

# funcion nuevo ingreso de un votante
def nuevo_ingreso(self,delantera, trasera):
    nom = self.ui.ingreso_nombre.text()
    ap = self.ui.ingreso_ap.text()
    am = self.ui.ingreso_am.text()
    calle = self.ui.ingreso_calle.text()
    num = self.ui.ingreso_numero.text()
    col = self.ui.combo_candidato.currentText()
    curp = self.ui.ingreso_curp.text()
    img_delantera = self.ui.foto_delantera.pixmap()
    img_trasera = self.ui.foto_trasera.pixmap()
    if nom == "":
        QMessageBox.about(self,"INFORMACION", "No ingresaste nombre")
    elif ap == "":
        QMessageBox.about(self, "INFORMACION", "No ingresaste A. paterno")
    elif am == "":
        QMessageBox.about(self, "INFORMACION", "No ingresaste A. materno")
    elif calle == "":
        QMessageBox.about(self, "INFORMACION", "No ingresaste Domicilio")
    elif num == "":
        QMessageBox.about(self, "INFORMACION", "No ingresaste Numero de casa")
    elif self.ui.combo_municipio.currentIndex == 0:
        QMessageBox.about(self, "INFORMACION", "No Seleccionaste Municipio")
    elif col == "":
        QMessageBox.about(self, "INFORMACION", "No Seleccionaste candidato")
    elif curp == "":
        QMessageBox.about(self, "INFORMACION", "No ingresaste curp")
    else:
        if img_delantera == None:
            QMessageBox.about(self, "INFORMACION", "No hay foto delantera")
        else:
            foto_delantera = open(delantera, 'rb').read()
            buff =sqlite3.Binary(foto_delantera)
        if img_trasera == None:
            QMessageBox.about(self, 'INFORMACION', "No hay foto trasera")
        else:
            foto_trasera = open(trasera, 'rb').read()
            buff_2 = sqlite3.Binary(foto_trasera)
            id_municipio = Query_principal.obtener_id_municipio(self.ui.combo_municipio.currentText())
            id_candidato = Query_principal.obtener_id_candidato(self.ui.combo_candidato.currentText())
            conexion = sqlite3.connect("DB_CV.db")
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO Informacion(Nombres, Ap, Am, Calle, Numero, Id_municipio, Id_Candidato, Curp, Foto_delantera, Foto_trasera) VALUES(?,?,?,?,?,?,?,?,?,?)',(nom,ap,am,calle,num,id_municipio[0][0],id_candidato[0][0],curp,buff,buff_2))
            conexion.commit()
            cursor.close()
            conexion.close()
            Limpiar_interfaz.limpieza_ingreso_informacion(self)
