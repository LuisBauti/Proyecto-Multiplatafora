# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################

# Llamando la conexion 
from Bd import Conexion_DB

# Seleccionamos el municipio de la base de datos, para cargarla en el reporte 
def reporte_municipio():
    query = ("SELECT Municipio FROM Municipio")
    resultado = Conexion_DB.conexion(query)
    return resultado

# Seleccionamos el Id_municipio de la base de datos, para cargarla en el reporte
def reporte_id_municipio(informacion):
    query = ("SELECT Id_municipio FROM Municipio WHERE Municipio == \"{0}\" ").format(informacion)
    resultado = Conexion_DB.conexion(query)
    return resultado

# Seleccionamos el Id_Candidato de la base de datos, para cargarla en el reporte
def reporte_id_candidato(informacion):
    query = ("SELECT Id_Candidato FROM Candidatos WHERE Candidato == \"{0}\" ").format(informacion)
    resultado = Conexion_DB.conexion(query)
    return resultado

# Seleccionamos el candidato  de la base de datos, para cargarla en el reporte
def reporte_candidato(informacion):
    query = ("SELECT Candidato FROM Candidatos WHERE Id_municipio == {0} ").format(informacion)
    resultado = Conexion_DB.conexion(query)
    return resultado

# Buscamos el municipio y la info. en la tabla informacion por medio de Id_municipio
def busqueda_municipio(informacion):
    query =("SELECT * FROM Informacion WHERE Id_municipio == {0} ").format(informacion)
    resultado = Conexion_DB.conexion(query)
    return resultado

# Seleccionamos el municipio de la base de datos, para cargarla en el reporte, solo municipio
def busqueda_solo_municipio(informacion):
    query = ("SELECT * FROM Informacion WHERE Id_municipio = {}").format(informacion)
    resultado = Conexion_DB.conexion(query)
    return resultado

# Seleccionamos de la tabla informacion el Id_Municipio y el Id_Candidato
def busqueda_municipio_candidato(mun, col):
    query = ("SELECT * FROM Informacion WHERE Id_municipio == {0} AND Id_Candidato == {1}").format(mun, col)
    resultado = Conexion_DB.conexion(query)
    return resultado
