# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################

# Mnadsamos a llamar a conexion
from Bd import Conexion_DB

# Seleccionamos el nombre del usuario de la tabla usuario
def datos_usuarios(informacion):
    query = ("SELECT * FROM Usuarios WHERE Nombre = \"{0}\" ").format(informacion)
    resultado = Conexion_DB.conexion(query)
    return resultado