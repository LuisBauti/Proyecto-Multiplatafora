# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################

from Bd import Query_municipio
from PySide2.QtWidgets import QMessageBox, QTableWidgetItem

# Ingreso Municipio con sus restricciones
def ingreso_municipio(self):
    if self.ui.nombre_municipio.text() == "":
        QMessageBox.about(self, "INFORMACION", "No ingresaste municipio")
    else:
        municipio = self.ui.nombre_municipio.text()
        Query_municipio.ingreso_municipio(municipio)

# Funcion para buscar el municipio
def obtener_municipio(self):
    resultado_municipio = Query_municipio.obtener_municipio_bd()
    if resultado_municipio == []:
        QMessageBox.about(self, "INFORMACION", "Aun no has ingresado ningun municipio")
    elif resultado_municipio != []:
        self.ui.lista_municipio.clear()
        self.ui.lista_municipio.setRowCount(len(resultado_municipio))
        self.ui.lista_municipio.setColumnCount(1)
        for filas in range(len(resultado_municipio)):
            item = QTableWidgetItem()
            item.setText(resultado_municipio[filas][0])
            self.ui.lista_municipio.setItem(filas, 0, item)
