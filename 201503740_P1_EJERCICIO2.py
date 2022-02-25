from html.entities import name2codepoint
from msilib.schema import Media
import string
import psycopg2
from contextlib import nullcontext
from multiprocessing import connection
from sqlite3 import Cursor
from ast import Return
from cmath import exp, sqrt
from logging import raiseExceptions
import math
import random
import numpy as np
import statistics as stat

try:  
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "marito",
        password = "hola",
        dbname = "PARCIAL_1"
    )
    print("conexion exitosa")

except psycopg2.Error as ERROR:
    print("OCURRIO UN ERROR EN LA CONEXION")
    print("VERIQUE LOS PARAMETROS")


cursor = conexion.cursor()


correcto = False    
def verHistorial():

    
    SQL = 'SELECT*FROM ejercicio2;'
    cursor.execute(SQL)
    valores = cursor.fetchall()
    print(valores)

def main():

    correcto = False
    opcion = 0
    while True:
        try:
            print("""
            Elige la operacion que quieras realizar
            
            1) Ingresar datos          
            2) regresar a menu principal
            """)

            opcion = int(input("Elige una opción: ") )     

            if opcion == 1:
                print(" ")
                try:
                    n1 = float(input("Introduce tu primer número: "))
                    n2 = float(input("Introduce tu segundo número: "))
                    n3 = float(input("Introduce tu segundo número: "))
                    n4 = float(input("Introduce tu segundo número: "))
                    n5 = float(input("Introduce tu segundo número: "))
                    lista = [n1,n2,n4,n5,n3]
                    suma = n1+n2+n3+n4+n5
                    grande = max(lista)
                    pequeño = min(lista)
                    rango = grande - pequeño
                    moda=stat.mode(lista)

                    media=np.mean(lista)
                    mediana= np.median(lista)
                    DesvE=np.std(lista)
                    varianza=np.var(lista)

                    print("La media es:",media )
                    print("La mediana es:",mediana )
                    print("La Desviacion Estandar es:",DesvE )
                    print("La Varianza es:",varianza )
                    print("La Moda es",moda)
                    print("El Rango es:",rango )
                    
                    cursor.execute("INSERT INTO ejercicio2(nota_1,nota_2,nota_3,nota_4,nota_5,media,mediana,desviacionE,varianza,moda,rango) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(n1,n2,n3,n4,n5,media,mediana,DesvE,varianza,moda,rango))
                    conexion.commit()



                except ValueError as ERROR:
                        print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                        print (ERROR)
                        print ("\n --------INTENTE DE NUEVO--------")
                        Return
                 


            elif opcion == 2:
                break

            else:
                try:
                    print("Opción incorrecta")
                    
                except ValueError as ERROR:
                        print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                        print (ERROR)
                        print ("\n --------INTENTE DE NUEVO--------")
                        Return

        except ValueError as ERROR:
                    print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero del menu<<<<<<<< \n ")
                    print (ERROR)
                    print ("\n --------INTENTE DE NUEVO--------")
                    Return



  


def pedirNumero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            correcto=True
            num = int(input("ingrese una opcion "))
        except ValueError:
            print("seleccione una opcion valida")
        
    return num

salir = False
while not salir:
    print ("1. ingresar al programa Calculadora de Promedio" )
    print("2. Ver historial de base de datos")
    print("3. Salir")

    opcion = pedirNumero()

    if opcion ==1:
        main()
    elif opcion ==2:
        verHistorial()

    elif opcion ==3:
        salir = True

    else:

        print("ingrese una opcion valida")

print("gracias por utilizar el programa")
cursor.close()
conexion.close()