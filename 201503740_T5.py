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


try:  
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "marito",
        password = "hola",
        dbname = "calculadora"
    )
    print("conexion exitosa")

except psycopg2.Error as ERROR:
    print("OCURRIO UN ERROR EN LA CONEXION")
    print("VERIQUE LOS PARAMETROS")

cursor = conexion.cursor()

correcto = False

def verHistorial():

    
    SQL = 'SELECT*FROM prueba3;'
    cursor.execute(SQL)
    valores = cursor.fetchall()
    print(valores)


def busar():

    sal = False

    while not sal:
        print ("1. buscar las sumas" )
        print("2. buscar las restas")
        print("3. buscar las multiplicaciones ")
        print("4. buscar las divisiones")
        print("5. buscar las raices")
        print("6. buscar las potencias")
        print("7. regresar al menu principal")

        opcion = pedirNumero()

        if opcion ==1:
            buscar = "select * from prueba3 where operacion ILIKE '%suma%';"
            cursor.execute(buscar)
            valores = cursor.fetchall()
            print(valores)

        elif opcion ==2:
            buscar = "select * from prueba3 where operacion ILIKE '%resta%';"
            cursor.execute(buscar)
            valores = cursor.fetchall()
            print(valores)

        elif opcion ==3:
            buscar = "select * from prueba3 where operacion ILIKE '%multiplicacion%';"
            cursor.execute(buscar)
            valores = cursor.fetchall()
            print(valores)
        elif opcion ==4:
            buscar = "select * from prueba3 where operacion ILIKE '%division%';"
            cursor.execute(buscar)
            valores = cursor.fetchall()
            print(valores)
        elif opcion ==5:
            buscar = "select * from prueba3 where operacion ILIKE '%raiz%';"
            cursor.execute(buscar)
            valores = cursor.fetchall()
            print(valores)
        
        elif opcion ==6:
            buscar = "select * from prueba3 where operacion ILIKE '%potencia%';"
            cursor.execute(buscar)
            valores = cursor.fetchall()
            print(valores)
            
        elif opcion ==7:
            sal = True

        else:

            print("ingrese una opcion valida")
   

def main():
    correcto = False
    opcion = 0
    while True:
        try:
            print("""
            Elige la operacion que quieras realizar
            
            1) Sumar 
            2) Restar 
            3) Multiplicar
            4) Dividir
            5) potencia
            6) Raiz
            7) regresar a menu principal
            """)

            opcion = int(input("Elige una opción: ") )     

            if opcion == 1:
                print(" ")
                try:
                    n1 = float(input("Introduce tu primer número: "))
                    n2 = float(input("Introduce tu segundo número: "))
                

                    print("""********************************************************************
                    RESULTADO: La suma de""",n1,"+",n2,"es igual a",n1+n2)
                    print("********************************************************************")
                    cursor.execute("INSERT INTO prueba3(operacion,n1,n2,resultado) VALUES('suma',%s,%s,%s);",(n1,n2,n1+n2))
                    conexion.commit()

                except ValueError as ERROR:
                        print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                        print (ERROR)
                        print ("\n --------INTENTE DE NUEVO--------")
                        Return

                    
            elif opcion == 2:
                print(" ")
                try:
                    n1 = float(input("Introduce tu primer número: "))
                    n2 = float(input("Introduce tu segundo número: "))

                    print("""********************************************************************
                    RESULTADO: La resta de""",n1,"-",n2,"es igual a",n1-n2)
                    print("********************************************************************")
                    cursor.execute("INSERT INTO prueba3(operacion,n1,n2,resultado) VALUES('resta',%s,%s,%s);",(n1,n2,n1-n2))
                    conexion.commit()

                except ValueError as ERROR:
                        print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                        print (ERROR)
                        print ("\n --------INTENTE DE NUEVO--------")
                        Return


            elif opcion == 3:
                print(" ")
                try:
                    n1 = float(input("Introduce tu primer número: "))
                    n2 = float(input("Introduce tu segundo número: "))

                    print("""********************************************************************
                    RESULTADO: El producto de""",n1,"*",n2,"es igual a",n1*n2)
                    print("********************************************************************")
                    cursor.execute("INSERT INTO prueba3(operacion,n1,n2,resultado) VALUES('multiplicacion',%s,%s,%s);",(n1,n2,n1*n2))
                    conexion.commit()

                except ValueError as ERROR:
                        print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                        print (ERROR)
                        print ("\n --------INTENTE DE NUEVO--------")
                        Return


            elif opcion == 4:
                print(" ")
                try:
                    n1 = float(input("Introduce tu primer número: "))
                    n2 = float(input("Introduce tu segundo número: "))

                    print("""********************************************************************
                    RESULTADO: El producto de""",n1,"/",n2,"es igual a",n1/n2)
                    print("********************************************************************")
                    cursor.execute("INSERT INTO prueba3(operacion,n1,n2,resultado) VALUES('division',%s,%s,%s);",(n1,n2,n1/n2))
                    conexion.commit()

                except ValueError as ERROR:
                        print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                        print (ERROR)
                        print ("\n --------INTENTE DE NUEVO--------")
                        Return
        
                except ZeroDivisionError as ERROR:
                        print ("\n >>>>>>>>>toda division de un numero entre cero (0) su resultado sera indefinido<<<<<<<< \n ")
                        print (ERROR)
                        print ("\n --------INTENTE DE NUEVO--------")
                        Return


            elif opcion == 5:
                print("\n----- X^n-----\n")
                try:
                    n1 = float(input("Introduce el valor de X: "))
                    n2 = float(input("Introduce el valor de n: "))

                    print("""********************************************************************
                    RESULTADO: La potencia de""",n1,"^",n2,"es igual a",n1**n2)
                    print("********************************************************************")
                    cursor.execute("INSERT INTO prueba3(operacion,n1,n2,resultado) VALUES('potencia',%s,%s,%s);",(n1,n2,n1**n2))
                    conexion.commit()

                except ValueError as ERROR:
                        print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                        print (ERROR)
                        print ("\n --------INTENTE DE NUEVO--------")
                        Return


            elif opcion == 6:
                print("\n ----- x √ (y) -----\n")
                try:
                    n1 = float(input("Introduce el valor de indice X : "))
                    n2 = float(input("Introduce el valor del radicando Y: "))

                    print("""********************************************************************
                    RESULTADO: La raiz""",n1,"√",n2,"es igual a",n2**(1/n1))
                    print("********************************************************************")  
                    cursor.execute("INSERT INTO prueba3(operacion,n1,n2,resultado) VALUES('raiz',%s,%s,%s);",(n1,n2,n2**(1/n1)))
                    conexion.commit()

                
                    raise ValueError ("el numero no puede ser negativo")
                    
                except ValueError as ERROR:
                        print ("\n >>>>>>>>>ha ingresado un valor invalido, favor ingresar un numero<<<<<<<< \n ")
                        print (ERROR)
                        print ("\n --------INTENTE DE NUEVO--------")
                        Return
                

                        


            elif opcion == 7:
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
    print ("1. Ingresar a la calculadora" )
    print("2. ver historial de base de datos")
    print("3. buscar por operacion ")
    print("4. salir")

    opcion = pedirNumero()

    if opcion ==1:
        main()
    elif opcion ==2:
        verHistorial()

    elif opcion ==3:
        busar()

    elif opcion ==4:
        salir = True

    else:

        print("ingrese una opcion valida")

print("gracias por utilizar el programa")
cursor.close()
conexion.close()