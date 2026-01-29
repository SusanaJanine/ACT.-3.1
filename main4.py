Numero = int(input("Ingrese un numero: ")) # Se solicita al usuario que ingrese un numero

if Numero > 0: # Se determina si el numero ingresado es mayor a cero entonces se imprime que es un numero positivo
    print("El numero es positivo")
elif Numero < 0: # Pero si el numero que se ingreso es menor a cero entonces se imprime que es un numero negativo
    print("El numero es negativo")
else: # Si no se cumple ninguna de las dos condiciones anteriores entonces el numero debera ser cero
    print("El numero es cero")