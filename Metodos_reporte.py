# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################

from Bd import Query_reporte
from PySide2.QtWidgets import QTableWidgetItem, QLabel
from PySide2.QtGui import QPixmap
from fpdf import FPDF
import getpass
from datetime import datetime

# Datos del combobox de municipio en reporte
def combo_reporte_municipio(self):
    self.ui.combo_reporte_municipio.clear()
    self.ui.combo_reporte_municipio.addItem("Selecciona municipio")
    resultado = Query_reporte.reporte_municipio()
    for i in range(len(resultado)):
        self.ui.combo_reporte_municipio.addItem(resultado[i][0])

# Datos del combobox de reporte candidato en reportes
def combo_reporte_candidato(self):
    self.ui.combo_reporte_candidato.clear()
    self.ui.combo_reporte_candidato.addItem("Selecciona candidato")
    if self.ui.combo_reporte_municipio.currentIndex == 0:
        self.ui.combo_reporte_candidato.clear()
    else:
        mun = self.ui.combo_reporte_municipio.currentText()
        resultado = Query_reporte.reporte_id_municipio(mun)
        if resultado == []:
            pass
        else:
            resultado = Query_reporte.reporte_candidato(resultado[0][0])
            for i in range(len(resultado)):
                self.ui.combo_reporte_candidato.addItem(resultado[i][0])

# Generar los reportes de votos
def reporte_generar(self):
    self.ui.total_registros.setText("")
    if self.ui.combo_reporte_municipio.currentIndex() == 0:
        pass
    elif (self.ui.combo_reporte_municipio.currentIndex() != 0) and (self.ui.combo_reporte_candidato.currentIndex() == 0):
        self.ui.tabla_reportes.clearContents()
        self.ui.tabla_reportes.setRowCount(0)
        mun = self.ui.combo_reporte_municipio.currentText()
        resultado = Query_reporte.reporte_id_municipio(mun)
        resultado_2 = Query_reporte.busqueda_solo_municipio(resultado[0][0])
        self.ui.tabla_reportes.setRowCount(len(resultado_2))
        for filas in range(len(resultado_2)):
            for columnas in range(10):
                if columnas <= 7:
                    item = QTableWidgetItem()
                    item.setText(str(resultado_2[filas][columnas+1]))
                    self.ui.tabla_reportes.setItem(filas, columnas, item)
                else:
                    f = QPixmap()
                    f.loadFromData(resultado_2[filas][columnas+1])
                    label = QLabel()
                    label.setPixmap(f)
                    label.setScaledContents(True)
                    label.setMaximumHeight(50)
                    label.setMaximumWidth(100)
                    self.ui.tabla_reportes.setCellWidget(filas, columnas, label)

    elif (self.ui.combo_reporte_municipio.currentIndex() != 0) and (self.ui.combo_reporte_candidato.currentIndex() != 0 ):
        self.ui.tabla_reportes.clearContents()
        self.ui.tabla_reportes.setRowCount(0)
        mun = self.ui.combo_reporte_municipio.currentText()
        col = self.ui.combo_reporte_candidato.currentText()
        resultado_mun = Query_reporte.reporte_id_municipio(mun)
        resultado_col = Query_reporte.reporte_id_candidato(col)
        resultado = Query_reporte.busqueda_municipio_candidato(resultado_mun[0][0], resultado_col[0][0])
        self.ui.tabla_reportes.setRowCount(len(resultado))
        for filas in range(len(resultado)):
            for columnas in range(10):
                if columnas <= 7 :
                    item = QTableWidgetItem()
                    item.setText(str(resultado[filas][columnas+1]))
                    self.ui.tabla_reportes.setItem(filas, columnas, item)
                else:
                    label = QLabel()
                    f = QPixmap()
                    f.loadFromData(resultado[filas][columnas+1])
                    label.setPixmap(f)
                    label.setScaledContents(True)
                    label.setMaximumHeight(50)
                    label.setMaximumWidth(100)
                    self.ui.tabla_reportes.setCellWidget(filas, columnas, label)

    filas_mostradas = self.ui.tabla_reportes.rowCount()
    self.ui.total_registros.setText(str(filas_mostradas))