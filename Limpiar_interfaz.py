# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################

from Metodos import Metodos_principal

def limpieza_ingreso_nuevo_usuario(self):
    self.ui.nuevo_usuario.setText("")
    self.ui.nuevo_contra.setText("")
    self.ui.permiso_usuario.setChecked(True)
    self.ui.nuevo_usuario.setFocus()

def limpieza_ingreso_informacion(self):
    self.ui.ingreso_nombre.setText("")
    self.ui.ingreso_ap.setText("")
    self.ui.ingreso_am.setText("")
    self.ui.ingreso_calle.setText("")
    self.ui.ingreso_numero.setText("")
    self.ui.ingreso_curp.setText("")
    self.ui.foto_delantera.clear()
    self.ui.foto_trasera.clear()
    Metodos_principal.llenar_combo_municipio(self)
