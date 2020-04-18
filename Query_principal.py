# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################

from Bd import Conexion_DB
import sqlite3
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import QByteArray, QIODevice, QBuffer

# Creando El Query Para obtener el nombre municipio 
def obtener_municipio():
    query = ("""SELECT Municipio
                FROM Municipio""")
    resultado = Conexion_DB.conexion(query)
    return resultado

#Creando El Query Para obtener el Id_municipio 
def obtener_id_municipio(informacion):
    query = ("""SELECT Id_municipio
                FROM Municipio
                WHERE Municipio = \"{0}\" """).format(informacion)
    resultado = Conexion_DB.conexion(query)
    return resultado

# Creando El Query Para obtener el Id_candidato 
def obtener_id_candidato(informacion):
    query = ("""SELECT Id_Candidato
                FROM Candidatos
                WHERE Candidato = \"{0}\" """).format(informacion)
    resultado = Conexion_DB.conexion(query)
    return resultado

#Creando El Query Para obtener elnombre candidato
def obtener_candidato(informacion):
    query = ("""SELECT Candidato
                FROM Candidatos 
                WHERE Id_municipio = {0}""").format(informacion)
    resultado = Conexion_DB.conexion(query)

    return resultado