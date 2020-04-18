# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################

# Llamamos a conexion
from Bd import Conexion_DB

# Obtenemos el nombre municipio de la base 
def obtener_municipio():
    query = ("SELECT Municipio FROM Municipio")
    resultado = Conexion_DB.conexion(query)
    return resultado

# Obtenemos el nombre Id_municipio de la base 
def obtener_id_municipio(informacion):
    query = ("SELECT Id_municipio from Municipio WHERE Municipio = \"{0}\" ").format(informacion)
    resultado = Conexion_DB.conexion(query)
    return resultado

# Obtenemos el nombrecandidato de la base 
def obtener_candidato(informacion):
    query = ("SELECT Candidato FROM Candidatos WHERE Id_municipio = {0} ").format(informacion)
    resultado = Conexion_DB.conexion(query)
    return resultado

# Obtenemos el Id_Candidato de la base 
def ingresar_candidato(informacion , id):
    query = ("INSERT INTO Candidatos(Candidato, Id_municipio) VALUES (\"{0}\", {1})").format(informacion, id[0][0])
    Conexion_DB.conexion(query)