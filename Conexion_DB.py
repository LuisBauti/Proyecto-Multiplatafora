# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Elecciones                                                       #
# Proposito: Conteo de votos                                                 #
# Autores: Owen Ariel Valle, Patrick David Soto, Luis Consuegra,             #
#          Klisban Rodiney Morales                                           #
# Fecha: 17/04/2020                                                          #
#               PROYECTO FINAL                                               #
##############################################################################

import sqlite3

# Metodo que utilizamos para la conexion a la DB
def conexion(consulta):
    # Creamos la conexion
    conexion = sqlite3.connect("DB_CV.db")
    # Creamos el cursor de la conexion
    cursor = conexion.cursor()
    # Ejecutamos la consulta
    cursor.execute(consulta)
    # Verificamos si la primera palabra de la consulta es SELECT o select
    if consulta.startswith("SELECT") or consulta.startswith("select"):
        # Se obtienen los datos de la consulta
        datos = cursor.fetchall()
    else:
        # Cargamos los datos
        conexion.commit()
        # Asignamos a la variable datos como vacia
        datos = None
    # Cerramos el cursor
    cursor.close()
    # Cerramos la conexion a la DB
    conexion.close()
    # Regresamos la informacion obtenida en la variable datos para ser utilizada
    return datos