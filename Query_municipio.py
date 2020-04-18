# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################


# Llamamos la conexion
from Bd import Conexion_DB

# Query Para ingresar el nombre del municipio a la base 
def ingreso_municipio(informacion):
    query = ("INSERT INTO Municipio(Municipio) VALUES(\"{0}\")").format(informacion)
    Conexion_DB.conexion(query)

# Por medio del Query obtenemos el nombre municipio de la base
def obtener_municipio_bd():
    query = ("SELECT Municipio FROM Municipio")
    resultado = Conexion_DB.conexion(query)
    return resultado

