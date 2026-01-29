Tabla = int(input("Ingrese un numero para multiplicar: ")) # Se solicita al usuario que ingrese un numero para generar su tabla de multiplicar

for i in range(1, 11): # El bucle for solo puede recorrer valores del 1 al 10 para generar la tabla de multiplicar
    resultado = Tabla * i # Se realiza la operacion de multiplicacion entre el numero ingresado y el valor actual de i
    print(f"{Tabla} x {i} = {resultado}") # Se imprime la multiplicacion de forma legible y el resultado obtenido