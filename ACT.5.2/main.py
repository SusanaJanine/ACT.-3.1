from calculadora import suma, resta, multiplicacion, division
from menu import menu
from utilidades import fahrenheit_celsius, km_millas
from datetime import datetime
from math import sqrt, pow, log, exp

if __name__ == "__main__":
    date= datetime.now() # Se obtiene la fecha y hora actual
    print("Fecha y hora actual:", date.strftime("%d/%m/%Y %H:%M:%S")) # Se muestra la fecha y hora actual

    opcion = 0
    while opcion != 11:
        menu() # Se manda a llamar la funcion "menu" para mostrarle las opciones al usuario
        opcion = int(input("Ingresar opcion: ")) # Solicitar al usuario una opcion
        
        if opcion < 1 or opcion > 11: # Verificar que la opcion elegida sea valida
            print("Opcion incorrecta, seleccione otra opcion")

        elif opcion == 1:
            print("Has elegido el camino de la suma")
            n1 = int(input("Favor de ingresar el primer numero a sumar: "))
            n2 = int(input("Favor de ingresar el segundo numero a sumar: "))
            print(f"El resultado de la suma es: {suma(n1, n2)}")
            
        elif opcion == 2:
            print("Has elegido el camino de la resta")
            n1 = int(input("Favor de ingresar el primer numero a restar: "))
            n2 = int(input("Favor de ingresar el segundo numero a restar: "))
            print(f"El resultado de la resta es: {resta(n1, n2)}")

        elif opcion == 3:
            print("Has elegido el camino de la multiplicacion")
            n1 = int(input("Favor de ingresar el primer numero a multiplicar: "))
            n2 = int(input("Favor de ingresar el segundo numero a multiplicar: "))
            print(f"El resultado de la multiplicacion es: {multiplicacion(n1, n2)}")
            
        elif opcion == 4:
            print("Has elegido el camino de la division")
            n1 = float(input("Favor de ingresar el primer numero a dividir: "))
            n2 = float(input("Favor de ingresar el segundo numero a dividir: "))
            print(f"El resultado de la division es: {division(n1, n2)}")
        
        elif opcion == 5:
            print("Has elegido el camino de la raiz cuadrada")
            n1 = float(input("Favor de ingresar el numero para sacar su raiz cuadrada: "))
            print(f"El resultado de la raiz cuadrada es: {sqrt(n1)}")
        
        elif opcion == 6:
            print("Has elegido el camino de la potencia")
            n1 = float(input("Favor de ingresar el numero base: "))
            n2 = float(input("Favor de ingresar el numero exponente: "))
            print(f"El resultado de la potencia es: {pow(n1, n2)}")
        
        elif opcion == 7:
            print("Has elegido el camino del logaritmo")
            n1 = float(input("Favor de ingresar el numero para sacar su logaritmo: "))
            print(f"El resultado del logaritmo es: {log(n1)}")
        
        elif opcion == 8:
            print("Has elegido el camino de la exponencial")
            n1 = float(input("Favor de ingresar el numero para sacar su exponencial: "))
            print(f"El resultado de la exponencial es: {exp(n1)}")
            
        elif opcion == 9:
            print("Has elegido la conversion de km a millas: ")
            n1 = float(input("Favor de ingresar los km: "))
            print(f"El resultado de los km a millas es: {km_millas(n1)}")

        elif opcion == 10:
            print("Has elegido la conversion de fahrenheit a celsius")
            n1 = float(input("Favor de ingresar el numero de los fahrenheit: "))
            print(f"El resultado de los fahrenheit a celsius es: {fahrenheit_celsius(n1)}")
            
        elif opcion == 11: # Si el usuario elige la opcion 7, el programa se termina.
            print("Has elegido salir")