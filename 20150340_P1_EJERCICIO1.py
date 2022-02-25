from html.entities import name2codepoint
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

    
    SQL = 'SELECT*FROM ejercicio1;'
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
            
            1) lanzar los dados           
            2) regresar a menu principal
            """)

            opcion = int(input("Elige una opción: ") )     

            if opcion == 1:
                print(" ")
                try:
                    dado1 = random.randint(1,6)
                    print("el dado numero 1 cayo:",dado1)   

                    dado2 = random.randint(1,6)
                    print("el dado numero 2 cayo:",dado2)

                    suma=dado1+dado2

                      


                    if suma ==8:

                        print("""********************************************************************
                         FELICIDADES GANASTE: La suma del dado1""",dado1,"+ el dado 2",dado2,"es igual a",suma,)
                        print("********************************************************************")
                        cursor.execute("INSERT INTO ejercicio1(numero1,numero2,resultado,rul) VALUES(%s,%s,%s,'GANADOR');",(dado1,dado2,suma))
                        conexion.commit()

                    elif suma ==7:
                        print("""********************************************************************
                         OOHHH PERDISTE :( : La suma de dado1""",dado1,"+ el dado2",dado2,"es igual a",suma,)
                        print("********************************************************************")
                        cursor.execute("INSERT INTO ejercicio1(numero1,numero2,resultado,rul) VALUES(%s,%s,%s,'PERDEDOR');",(dado1,dado2,suma))
                        conexion.commit()

                    elif suma <7:
                        print("""******************************************************************************
                         TIENES OTRA OPORTUNIDAD VUELVE A TIRAR LOS DADOS""")
                        print("******************************************************************************")
                        cursor.execute("INSERT INTO ejercicio1(numero1,numero2,resultado,rul) VALUES(%s,%s,%s,'N/A');",(dado1,dado2,suma))
                        break


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
    print ("1. Ingresar al JUEGO SIMULADO EL GRAN8" )
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