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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Central de Votos")
        MainWindow.resize(794, 491)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget_principal = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_principal.setGeometry(QtCore.QRect(0, 0, 740, 450))
        self.stackedWidget_principal.setObjectName("stackedWidget_principal")
        self.Ingreso = QtWidgets.QWidget()

        # Diseño de la parte de los votantes
        self.Ingreso.setObjectName("Votantes")
        self.ine_frontal = QtWidgets.QPushButton(self.Ingreso)
        self.ine_frontal.setGeometry(QtCore.QRect(320, 100, 100, 30))
        self.ine_frontal.setObjectName("imagen_frontal")

        self.ine_trasera = QtWidgets.QPushButton(self.Ingreso)
        self.ine_trasera.setGeometry(QtCore.QRect(320, 230, 100, 30))
        self.ine_trasera.setObjectName("imagen_trasera")

        self.label_2 = QtWidgets.QLabel(self.Ingreso)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 90, 30))
        self.label_2.setObjectName("label_2")

        self.label_8 = QtWidgets.QLabel(self.Ingreso)
        self.label_8.setGeometry(QtCore.QRect(10, 300, 62, 30))
        self.label_8.setObjectName("label_8")
        
        #Diseño del caudro que enviaremos la imagen
        self.foto_delantera = QtWidgets.QLabel(self.Ingreso)
        self.foto_delantera.setGeometry(QtCore.QRect(440, 20, 240, 110))
        self.foto_delantera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.foto_delantera.setText("")
        self.foto_delantera.setScaledContents(True)
        self.foto_delantera.setObjectName("foto_delantera")


        self.ingreso_ap = QtWidgets.QLineEdit(self.Ingreso)
        self.ingreso_ap.setGeometry(QtCore.QRect(100, 60, 190, 25))
        self.ingreso_ap.setObjectName("ingreso_ap")

        # Diseño del combo de municipio
        self.combo_municipio = QtWidgets.QComboBox(self.Ingreso)
        self.combo_municipio.setGeometry(QtCore.QRect(100, 220, 190, 25))
        self.combo_municipio.setStyleSheet("")
        self.combo_municipio.setCurrentText("")
        self.combo_municipio.setObjectName("combo_municipio")

        # Text de ingreso de la calle o barrio
        self.ingreso_calle = QtWidgets.QLineEdit(self.Ingreso)
        self.ingreso_calle.setGeometry(QtCore.QRect(100, 140, 190, 25))
        self.ingreso_calle.setObjectName("ingreso_calle")

        # Text de ingreso dee numero de telefono
        self.ingreso_numero = QtWidgets.QLineEdit(self.Ingreso)
        self.ingreso_numero.setGeometry(QtCore.QRect(100, 180, 190, 25))
        self.ingreso_numero.setObjectName("ingreso_numero")

        # Text de ingreso de el numero de identidad
        self.ingreso_curp = QtWidgets.QLineEdit(self.Ingreso)
        self.ingreso_curp.setGeometry(QtCore.QRect(100, 300, 190, 25))
        self.ingreso_curp.setObjectName("ingreso_identidad")

        # Boton del comando cancelar
        self.ingreso_cancelar = QtWidgets.QPushButton(self.Ingreso)
        self.ingreso_cancelar.setGeometry(QtCore.QRect(320, 300, 150, 25))
        self.ingreso_cancelar.setObjectName("ingreso_cancelar")

        # Text de ingreso Apellido materno
        self.ingreso_am = QtWidgets.QLineEdit(self.Ingreso)
        self.ingreso_am.setGeometry(QtCore.QRect(100, 100, 190, 25))
        self.ingreso_am.setObjectName("ingreso_am")

        # Label de los text de votantes
        self.label_6 = QtWidgets.QLabel(self.Ingreso)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 62, 30))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.Ingreso)
        self.label.setGeometry(QtCore.QRect(10, 20, 80, 30))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.Ingreso)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 80, 30))
        self.label_3.setObjectName("label_3")

        #Text de ingreso nombre
        self.ingreso_nombre = QtWidgets.QLineEdit(self.Ingreso)
        self.ingreso_nombre.setGeometry(QtCore.QRect(100, 20, 190, 25))
        self.ingreso_nombre.setObjectName("ingreso_nombre")
        #Label de ingreso nombre
        self.label_4 = QtWidgets.QLabel(self.Ingreso)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 62, 30))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Ingreso)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 62, 30))
        self.label_5.setObjectName("label_5")

        #Boton aceptar
        self.ingreso_aceptar = QtWidgets.QPushButton(self.Ingreso)
        self.ingreso_aceptar.setGeometry(QtCore.QRect(490, 300, 150, 25))
        self.ingreso_aceptar.setObjectName("ingreso_aceptar")

        #Label foto trasera
        self.foto_trasera = QtWidgets.QLabel(self.Ingreso)
        self.foto_trasera.setGeometry(QtCore.QRect(440, 150, 240, 110))
        self.foto_trasera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.foto_trasera.setText("")
        self.foto_trasera.setScaledContents(True)
        self.foto_trasera.setObjectName("foto_trasera")

        #Combobox para cargar candidatos
        self.combo_candidato = QtWidgets.QComboBox(self.Ingreso)
        self.combo_candidato.setGeometry(QtCore.QRect(100, 260, 190, 25))
        self.combo_candidato.setStyleSheet("")
        self.combo_candidato.setCurrentText("")
        self.combo_candidato.setObjectName("combo_candidato")
        #Label para el combo candidato
        self.label_15 = QtWidgets.QLabel(self.Ingreso)
        self.label_15.setGeometry(QtCore.QRect(10, 260, 62, 30))
        self.label_15.setObjectName("label_15")
        self.stackedWidget_principal.addWidget(self.Ingreso)

        #Boton reportes de la barrra de proceso inicail
        self.Reportes = QtWidgets.QWidget()
        self.Reportes.setObjectName("Reportes")
        self.reporte_generar = QtWidgets.QPushButton(self.Reportes)
        self.reporte_generar.setGeometry(QtCore.QRect(10, 230, 140, 30))
        self.reporte_generar.setObjectName("reporte_generar")
        #label reportes
        self.label_16 = QtWidgets.QLabel(self.Reportes)
        self.label_16.setGeometry(QtCore.QRect(10, 0, 160, 70))
        self.label_16.setObjectName("label_16")

        #Combo para reporte de municipio
        self.combo_reporte_municipio = QtWidgets.QComboBox(self.Reportes)
        self.combo_reporte_municipio.setGeometry(QtCore.QRect(10, 110, 140, 23))
        self.combo_reporte_municipio.setObjectName("combo_reporte_municipio")
        #Label de municipio
        self.label_17 = QtWidgets.QLabel(self.Reportes)
        self.label_17.setGeometry(QtCore.QRect(10, 70, 80, 30))
        self.label_17.setObjectName("label_17")

        #Label candidato
        self.label_18 = QtWidgets.QLabel(self.Reportes)
        self.label_18.setGeometry(QtCore.QRect(10, 140, 100, 30))
        self.label_18.setObjectName("label_18")

        #Combo dee reporte candidato
        self.combo_reporte_candidato = QtWidgets.QComboBox(self.Reportes)
        self.combo_reporte_candidato.setGeometry(QtCore.QRect(10, 180, 140, 23))
        self.combo_reporte_candidato.setObjectName("combo_reporte_candidato")

        #Tabla de reportes(Grid) 
        self.tabla_reportes = QtWidgets.QTableWidget(self.Reportes)
        self.tabla_reportes.setGeometry(QtCore.QRect(170, 10, 560, 390))
        self.tabla_reportes.setObjectName("tabla_reportes")
        self.tabla_reportes.setColumnCount(10)
        self.tabla_reportes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(9, item)

        #Label de total de registros
        self.label_19 = QtWidgets.QLabel(self.Reportes)
        self.label_19.setGeometry(QtCore.QRect(540, 410, 110, 30))
        self.label_19.setObjectName("label_19")
        self.total_registros = QtWidgets.QLabel(self.Reportes)
        self.total_registros.setGeometry(QtCore.QRect(660, 410, 60, 30))
        self.total_registros.setText("")
        self.total_registros.setObjectName("total_registros")
        self.stackedWidget_principal.addWidget(self.Reportes)

        #Interfaz de ajustes para crear un nuevo usuario, tabajuste es la que aprece en la barra izquierda
        self.Ajustes = QtWidgets.QWidget()
        self.Ajustes.setObjectName("Ajustes")
        self.tab_ajustes = QtWidgets.QTabWidget(self.Ajustes)
        self.tab_ajustes.setGeometry(QtCore.QRect(0, 0, 721, 431))
        self.tab_ajustes.setObjectName("tab_ajustes")

        #Ingreso un nuevo usuario
        self.Ingreso_usuario = QtWidgets.QWidget()
        self.Ingreso_usuario.setObjectName("Ingreso_usuario")

        #Boton aceptar
        self.nuevo_aceptar = QtWidgets.QPushButton(self.Ingreso_usuario)
        self.nuevo_aceptar.setGeometry(QtCore.QRect(230, 210, 160, 40))
        self.nuevo_aceptar.setObjectName("nuevo_aceptar")

        #Label del boton aceptar
        self.label_11 = QtWidgets.QLabel(self.Ingreso_usuario)
        self.label_11.setGeometry(QtCore.QRect(20, 20, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(15)

        #Label de nuevo usuario
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        #Text de nuevo usuario
        self.nuevo_usuario = QtWidgets.QLineEdit(self.Ingreso_usuario)
        self.nuevo_usuario.setGeometry(QtCore.QRect(170, 14, 220, 30))
        self.nuevo_usuario.setObjectName("nuevo_usuario")

        #Permiso del usuario(Administrador, usuario(Solo permitira votar))
        self.permisos = QtWidgets.QGroupBox(self.Ingreso_usuario)
        self.permisos.setGeometry(QtCore.QRect(170, 100, 220, 90))
        self.permisos.setAlignment(QtCore.Qt.AlignCenter)
        self.permisos.setCheckable(False)
        self.permisos.setObjectName("permisos")

        #Permiso al radio button usuario
        self.permiso_usuario = QtWidgets.QRadioButton(self.permisos)
        self.permiso_usuario.setGeometry(QtCore.QRect(10, 30, 99, 21))
        self.permiso_usuario.setObjectName("permiso_usuario")
 
        #Boton permiso usurio
        self.permiso_admin = QtWidgets.QRadioButton(self.permisos)
        self.permiso_admin.setGeometry(QtCore.QRect(10, 60, 130, 21))
        self.permiso_admin.setObjectName("permiso_admin")

        #Label usuario
        self.label_12 = QtWidgets.QLabel(self.Ingreso_usuario)
        self.label_12.setGeometry(QtCore.QRect(20, 60, 130, 40))
        #Tipo de fuente
        font = QtGui.QFont()
        font.setPointSize(15)

        #Label de nueva contraseña
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        # Text de nueva contraseña
        self.nuevo_contra = QtWidgets.QLineEdit(self.Ingreso_usuario)
        self.nuevo_contra.setGeometry(QtCore.QRect(170, 60, 220, 30))
        self.nuevo_contra.setObjectName("nuevo_contra")

        #Boton de cancelar 
        self.nuevo_cancelar = QtWidgets.QPushButton(self.Ingreso_usuario)
        self.nuevo_cancelar.setGeometry(QtCore.QRect(50, 210, 160, 40))
        self.nuevo_cancelar.setObjectName("nuevo_cancelar")
        self.tab_ajustes.addTab(self.Ingreso_usuario, "")

        #Text de ingreso municipio
        self.Ingreso_municipio = QtWidgets.QWidget()
        self.Ingreso_municipio.setObjectName("Ingreso_municipio")

        #Boton de agreagar municipio
        self.agregar_municipio = QtWidgets.QPushButton(self.Ingreso_municipio)
        self.agregar_municipio.setGeometry(QtCore.QRect(10, 80, 220, 30))
        self.agregar_municipio.setObjectName("agregar_municipio")

        #Grid de municipios para mostrar los municipios guardados 
        self.lista_municipio = QtWidgets.QTableWidget(self.Ingreso_municipio)
        self.lista_municipio.setGeometry(QtCore.QRect(250, 40, 291, 320))
        self.lista_municipio.setObjectName("lista_municipio")
        self.lista_municipio.setColumnCount(0)
        self.lista_municipio.setRowCount(0)

        #Text de agregar nombre municipio
        self.nombre_municipio = QtWidgets.QLineEdit(self.Ingreso_municipio)
        self.nombre_municipio.setGeometry(QtCore.QRect(10, 40, 220, 30))
        self.nombre_municipio.setObjectName("nombre_municipio")

        #Label de nommbre municipio
        self.label_7 = QtWidgets.QLabel(self.Ingreso_municipio)
        self.label_7.setGeometry(QtCore.QRect(290, 10, 220, 30))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        #Label de ingreso municipio
        self.label_9 = QtWidgets.QLabel(self.Ingreso_municipio)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 220, 30))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        #Ajustarlo a la tabla de tareas
        self.tab_ajustes.addTab(self.Ingreso_municipio, "")

        #Text de ingreso candidato
        self.Ingreso_candidato = QtWidgets.QWidget()
        self.Ingreso_candidato.setObjectName("Ingreso_candidato")

        #Label de ingreso candidato
        self.label_10 = QtWidgets.QLabel(self.Ingreso_candidato)
        self.label_10.setGeometry(QtCore.QRect(290, 10, 220, 30))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

        #Grid de la tabla de candidatos, la cual muestra los candidatos de cada municipio
        self.lista_candidato = QtWidgets.QTableWidget(self.Ingreso_candidato)
        self.lista_candidato.setGeometry(QtCore.QRect(250, 50, 291, 330))
        self.lista_candidato.setObjectName("listas_candidato")
        self.lista_candidato.setColumnCount(0)
        self.lista_candidato.setRowCount(0)

        #Boton ingreso candidato
        self.candidato_ingreso = QtWidgets.QPushButton(self.Ingreso_candidato)
        self.candidato_ingreso.setGeometry(QtCore.QRect(10, 180, 220, 30))
        self.candidato_ingreso.setObjectName("candidato_ingreso")

        #Combo de municipios para traer los resultados de este 
        self.combo_municipios = QtWidgets.QComboBox(self.Ingreso_candidato)
        self.combo_municipios.setGeometry(QtCore.QRect(10, 50, 220, 30))
        self.combo_municipios.setObjectName("combo_municipios")

        #Text de ingreso a un candidato
        self.ingreso_candidato = QtWidgets.QLineEdit(self.Ingreso_candidato)
        self.ingreso_candidato.setGeometry(QtCore.QRect(10, 140, 220, 30))
        self.ingreso_candidato.setObjectName("ingreso_candidato")

        #Label de ingreso candidato
        self.label_13 = QtWidgets.QLabel(self.Ingreso_candidato)
        self.label_13.setGeometry(QtCore.QRect(10, 100, 220, 30))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")

        #Label del combobox ingreso candidato
        self.label_14 = QtWidgets.QLabel(self.Ingreso_candidato)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 220, 30))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        #Ajustar la opcion candidatos a la barra de tareas 
        self.tab_ajustes.addTab(self.Ingreso_candidato, "Candidatos")

        self.stackedWidget_principal.addWidget(self.Ajustes)
        MainWindow.setCentralWidget(self.centralwidget)

        #Barra de tareas
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setOrientation(QtCore.Qt.Vertical)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)

        #Si se preciona la barra en registro   
        self.Barra_Registro = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Registro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Barra_Registro.setIcon(icon)
        self.Barra_Registro.setObjectName("Barra_Registro")
        self.Barra_Configuracion = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/ajustes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        #Si se preciona la barra  de configuracion
        self.Barra_Configuracion.setIcon(icon1)
        self.Barra_Configuracion.setObjectName("Barra_Configuracion")
        self.Barra_Salir = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/Salir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Barra_Salir.setIcon(icon2)
        self.Barra_Salir.setObjectName("Barra_Salir")

        #Si se preciona barra reportes
        self.Barra_Reportes = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/document_report_16751.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Barra_Reportes.setIcon(icon3)
        self.Barra_Reportes.setObjectName("Barra_Reportes")

        #Barra de herramientas la izquierdo
        self.toolBar.addAction(self.Barra_Registro)
        self.toolBar.addAction(self.Barra_Configuracion)
        self.toolBar.addAction(self.Barra_Reportes)
        self.toolBar.addAction(self.Barra_Salir)
        self.retranslateUi(MainWindow)
        self.stackedWidget_principal.setCurrentIndex(1)
        self.tab_ajustes.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Esto ayuda a poder utilizar el tabulador a la hora de realizar un registro
        MainWindow.setTabOrder(self.ingreso_nombre, self.ingreso_ap)
        MainWindow.setTabOrder(self.ingreso_ap, self.ingreso_am)
        MainWindow.setTabOrder(self.ingreso_am, self.ingreso_calle)
        MainWindow.setTabOrder(self.ingreso_calle, self.ingreso_numero)
        MainWindow.setTabOrder(self.ingreso_numero, self.combo_municipio)
        MainWindow.setTabOrder(self.combo_municipio, self.combo_candidato)
        MainWindow.setTabOrder(self.combo_candidato, self.ingreso_curp)
        MainWindow.setTabOrder(self.ingreso_curp, self.ine_frontal)
        MainWindow.setTabOrder(self.ine_frontal, self.ine_trasera)
        MainWindow.setTabOrder(self.ine_trasera, self.ingreso_aceptar)
        MainWindow.setTabOrder(self.ingreso_aceptar, self.ingreso_cancelar)
        MainWindow.setTabOrder(self.ingreso_cancelar, self.lista_municipio)
        MainWindow.setTabOrder(self.lista_municipio, self.nombre_municipio)
        MainWindow.setTabOrder(self.nombre_municipio, self.lista_candidato)
        MainWindow.setTabOrder(self.lista_candidato, self.candidato_ingreso)
        MainWindow.setTabOrder(self.candidato_ingreso, self.combo_municipios)
        MainWindow.setTabOrder(self.combo_municipios, self.ingreso_candidato)
        MainWindow.setTabOrder(self.candidato_ingreso, self.tab_ajustes)
        MainWindow.setTabOrder(self.tab_ajustes, self.agregar_municipio)


   # Labels de registro votos
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("Votante", "Votante", None, -1))
        self.ine_frontal.setText(QtWidgets.QApplication.translate("Votante", "Foto frontal", None, -1))
        self.ine_trasera.setText(QtWidgets.QApplication.translate("Votante", "Foto trasera", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Votante", "A. paterno", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Votante", "Identidad", None, -1))
        self.ingreso_cancelar.setText(QtWidgets.QApplication.translate("Votante", "Cancelar", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Votante", "Numero", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Votante", "Nombre(s)", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Votante", "A. materno", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Votante", "Calle", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Votante", "Municipio", None, -1))
        self.ingreso_aceptar.setText(QtWidgets.QApplication.translate("Votante", "Ingresar", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("Votante", "Candidatos", None, -1))
        self.reporte_generar.setText(QtWidgets.QApplication.translate("Votante", "Generar", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("Votante", "Elige los elementos para, generar el reporte", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("Votante", "Municipio", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("Votante", "Candidato", None, -1))

        #Registro a llamar en la tabla reportes en su encabezado
        self.tabla_reportes.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Votante", "Nombre", None, -1))
        self.tabla_reportes.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Votante", "P.Apellido", None, -1))
        self.tabla_reportes.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("Votante", "S.Apellido", None, -1))
        self.tabla_reportes.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("Votante", "Calle", None, -1))
        self.tabla_reportes.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("Votante", "Numero", None, -1))
        self.tabla_reportes.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("Votante", "Municipio", None, -1))
        self.tabla_reportes.horizontalHeaderItem(6).setText(QtWidgets.QApplication.translate("Votante", "Cadidato", None, -1))
        self.tabla_reportes.horizontalHeaderItem(7).setText(QtWidgets.QApplication.translate("Votante", "Identidad", None, -1))
        self.tabla_reportes.horizontalHeaderItem(8).setText(QtWidgets.QApplication.translate("Votante", "Frontal", None, -1))
        self.tabla_reportes.horizontalHeaderItem(9).setText(QtWidgets.QApplication.translate("Votante", "Tracera", None, -1))


        #Labels de la tabla configuracion
        self.label_19.setText(QtWidgets.QApplication.translate("Votante", "Total de registros", None, -1))
        self.nuevo_aceptar.setText(QtWidgets.QApplication.translate("Ingreso", "Aceptar", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("Ingreso", "Usuario", None, -1))
        self.permisos.setTitle(QtWidgets.QApplication.translate("Ingreso", "Permisos", None, -1))
        self.permiso_usuario.setText(QtWidgets.QApplication.translate("Ingreso", "Usuario", None, -1))
        self.permiso_admin.setText(QtWidgets.QApplication.translate("Ingreso", "Administrador", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("Ingreso", "Contraseña", None, -1))
        self.nuevo_cancelar.setText(QtWidgets.QApplication.translate("Ingreso", "Cancelar", None, -1))
        self.tab_ajustes.setTabText(self.tab_ajustes.indexOf(self.Ingreso_usuario), QtWidgets.QApplication.translate("Ingreso", "Usuarios", None, -1))
        self.agregar_municipio.setText(QtWidgets.QApplication.translate("Municipios_Votantes", "Agregar", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Municipios_Votantes", "Municipios existentes", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("Municipios_Votantes", "Nombre del municipio", None, -1))
        self.tab_ajustes.setTabText(self.tab_ajustes.indexOf(self.Ingreso_municipio), QtWidgets.QApplication.translate("Municipios_Votantes", "Municipio", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("Mostrar_Candidatos", "Candidatos", None, -1))
        self.candidato_ingreso.setText(QtWidgets.QApplication.translate("Mostrar_Candidatos", "Candidato", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("Mostrar_Candidatos", "Agrega el candidato", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("Mostrar_Candidatos", "Elige el municipio", None, -1))
      
        #Labels de la parte de principal
        self.tab_ajustes.setTabText(self.tab_ajustes.indexOf(self.candidato_ingreso), QtWidgets.QApplication.translate("Mostrar_Candidatos", "Candidatos", None, -1))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("Principal", "toolBar", None, -1))
        self.Barra_Registro.setText(QtWidgets.QApplication.translate("Principal", "Registro", None, -1))
        self.Barra_Registro.setToolTip(QtWidgets.QApplication.translate("Principal", "Nuevo ingreso", None, -1))
        self.Barra_Configuracion.setText(QtWidgets.QApplication.translate("Principal", "Configuracion", None, -1))
        self.Barra_Salir.setText(QtWidgets.QApplication.translate("Principal", "Salir", None, -1))
        self.Barra_Reportes.setText(QtWidgets.QApplication.translate("Principal", "Reportes", None, -1))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

