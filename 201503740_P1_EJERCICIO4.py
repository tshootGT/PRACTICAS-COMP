from html.entities import name2codepoint
import string
import psycopg2
from contextlib import nullcontext
from multiprocessing import connection
from sqlite3 import Cursor, enable_shared_cache
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

    
    SQL = 'SELECT*FROM ejercicio4;'
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
            
            1) CALCULAR NUMERO      
            2) regresar a menu principal
            """)

            opcion = int(input("Elige una opción: ") )     

            if opcion == 1:
                print(" ")
                
                n1=int(input("ingrese el numero: "))  
                def evaluar_primo(n1):
                    
                    contador=0
                    resultado=True

                    for i in range(1,n1+1):
                        if (n1%i==0):
                            contador+=1
                        if (contador>2):
                            resultado=False
                            break
                    return resultado
                if (evaluar_primo(n1)==True):
                    print("el numero ingrsado es primo")
                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO ejercicio4(numero,resultado) VALUES(%s,'PRIMO');",(n1))
                    conexion.commit()

                else:
                    print("el numero ingresado no es primo")
                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO ejercicio4(numero,resultado) VALUES(%s,'NO PRIMO');",(n1))
                    conexion.commit() 
                
                 


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
    print ("1. Ingresar al programa eleccion de numero" )
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