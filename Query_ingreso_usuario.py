# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################

# Llamamos a la conexion 
from Bd import Conexion_DB

# Por medio del Query mandamos a guardar la imformacion del nuevo usuario (Nombre, Contraseña, Permiso)
def ingreso_usuario_nuevo(informacion):
    query = ("INSERT INTO Usuarios(Nombre, Password, Permisos) VALUES (\"{0}\", \"{1}\", {2})").format(informacion[0], informacion[1], informacion[2])
    Conexion_DB.conexion(query)
