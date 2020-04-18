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
import os
# Verificando si la base ya existe (sino entonces crear)
if os.path.exists("DB_CV.db"):
    print("La base de datos ya existe")
else:
    # Creamos la base de dato
    conexion = sqlite3.connect("DB_CV.db")
    # Esta linea nos permite leer tildes y ñ paraque los votantes puedan 
    # colocar su nombre tal y como es
    conexion.text_factory = str
    # Creamos el cursor
    cursor = conexion.cursor()
    # Crendo  las tablas  

    # Creando la tabla Usuarios 
    cursor.execute('CREATE TABLE Usuarios '
                   '(Id_usuarios INTEGER PRIMARY KEY AUTOINCREMENT,'
                   ' Nombre VARCHAR (20) UNIQUE NOT NULL,'
                   ' Password VARCHAR (200) NOT NULL,'
                   ' Permisos INTEGER NOT NULL)')

     # Creando la tabla Municipio
    cursor.execute('CREATE TABLE Municipio'
                   '(Id_municipio INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'Municipio VARCHAR (30) UNIQUE NOT NULL)')

     # Creando la tabla Candidatos
    cursor.execute('CREATE TABLE Candidatos'
                    '(Id_Candidato INTEGER PRIMARY KEY AUTOINCREMENT,'
                    ' Candidato VARCHAR (30) NOT NULL,'
                    ' Id_municipio INTEGER NOT NULL,'
                    ' FOREIGN KEY(Id_municipio)REFERENCES Municipio(Id_municipio))')

     # Creando la tabla Informacion
    cursor.execute('CREATE TABLE  Informacion'
                   '(Id INTEGER PRIMARY KEY AUTOINCREMENT,'
                   ' Nombres VARCHAR (50) NOT NULL,'
                   ' Ap VARCHAR (50) NOT NULL,'
                   ' Am VARCHAR (50) NOT NULL,'
                   ' Calle VARCHAR (70) NOT NULL,'
                   ' Numero VARCHAR (10) NOT NULL,'
                   ' Id_municipio INTEGER NOT NULL,'
                   ' Id_Candidato INTEGER NOT NULL,'
                   ' Curp VARCHAR (50) NOT NULL,'
                   ' Foto_delantera BLOB,'
                   ' Foto_trasera BLOB)')

     # Insertando por defecto a la tabla Usuario con un nombre, una contraseña y el tipo de permiso 
    cursor.execute('INSERT INTO Usuarios(Nombre, Password, Permisos)'
                   'VALUES("root", "99adc231b045331e514a516b4b7680f588e3823213abe901738bc3ad67b2f6fcb3c64efb93d18002588d3ccc1a49efbae1ce20cb43df36b38651f11fa75678e8", 1)')
    # Guardamos cambios
    conexion.commit()
    # Cerramos conexion
    conexion.close()
