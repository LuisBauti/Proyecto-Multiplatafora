# -*- coding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    # Diseño del setup inicial.
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ingreso")
        MainWindow.resize(361, 167)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Boton Acepatr
        self.Aceptar = QtWidgets.QPushButton(self.centralwidget)
        self.Aceptar.setGeometry(QtCore.QRect(230, 100, 110, 25))
        self.Aceptar.setAutoDefault(True)
        self.Aceptar.setObjectName("Aceptar")

        # Boton Salir
        self.Salir = QtWidgets.QPushButton(self.centralwidget)
        self.Salir.setGeometry(QtCore.QRect(110, 100, 110, 25))
        self.Salir.setAutoDefault(True)
        self.Salir.setObjectName("Salir")

        #Label 1 y label 2 para el usuario y password
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(31, 10, 90, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 140, 30))
        self.label_2.setObjectName("label_2")

        #Text de usuario
        self.Usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.Usuario.setGeometry(QtCore.QRect(125, 10, 210, 25))
        self.Usuario.setText("")
        self.Usuario.setObjectName("Usuario")

        #Text de Contraseña
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(125, 50, 210, 25))
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        MainWindow.setCentralWidget(self.centralwidget)

        #Menu principal despues de ingresar el usuario
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusBar.setStyleSheet("")
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.VolverLoginUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Retranslate vuelve al login inicial al dar boton salir, llamamos al diseño del login.
    def VolverLoginUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("Ingreso", "Ingreso", None, -1))
        self.Aceptar.setText(QtWidgets.QApplication.translate("Ingreso", "Aceptar", None, -1))
        self.Salir.setText(QtWidgets.QApplication.translate("Ingreso", "Salir", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Ingreso", "Usuario", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Ingreso", "Contraseña", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

