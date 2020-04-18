# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################

from Pantallas import Limpiar_interfaz
from Bd import Query_candidato
from PySide2.QtWidgets import QTableWidgetItem, QMessageBox

# Funcion para llenar los combobox  
def llenado_combobox(self):
    self.ui.combo_municipios.clear()
    self.ui.combo_municipios.addItem("Selecciona un municipio")
    resultado = Query_candidato.obtener_municipio()
    for i in range(len(resultado)):
        self.ui.combo_municipios.addItem(resultado[i][0])

# Funcion para agregar candidato
def agregar_candidato(self):
    municipio_seleccionado = self.ui.combo_municipios.currentIndex()
    if municipio_seleccionado == 0:
        QMessageBox.about(self, "INFORMACION", "No seleccionaste ningun municipio")
    else:
        municipio_seleccionado = self.ui.combo_municipios.currentText()
        col = self.ui.ingreso_candidato.text()
        if  col == "":
            QMessageBox.about(self, "INFORMACION", "No ingresaste Candidato")
        else:
            resultado_id = Query_candidato.obtener_id_municipio(municipio_seleccionado)
            Query_candidato.ingresar_candidato(col, resultado_id)
            buscar_candidato(self)                                           
            self.ui.combo_municipios.setCurrentIndex(0)
            self.ui.ingreso_candidato.setText("")

# Funcion para buscar candidato
def buscar_candidato(self):
    self.ui.lista_candidato.setRowCount(0)
    self.ui.lista_candidato.setColumnCount(0)
    self.ui.lista_candidato.clear()
    self.ui.lista_candidato.clearContents()
    index = self.ui.combo_municipios.currentIndex()
    if index == 0:
        pass
    else:
        mun = self.ui.combo_municipios.currentText()
        resultado = Query_candidato.obtener_id_municipio(mun)
        if resultado == []:
            pass
        else:
            resultado = Query_candidato.obtener_candidato(resultado[0][0])
            if resultado == []:
                pass
            else:
                self.ui.lista_candidato.setRowCount(len(resultado))
                self.ui.lista_candidato.setColumnCount(1)
                for i in range(len(resultado)):
                    item = QTableWidgetItem()
                    item.setText(resultado[i][0])
                    self.ui.lista_candidato.setItem(i, 0, item)
