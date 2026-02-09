def factorial(n): # Se define la función que calcula el factorial de un número
    if n < 0: # Se verifica si el número es negativo, ya que el factorial no funciona para números negativos
        return 1 # Se devuelve 1 para el caso de números negativos, aunque en realidad el factorial no está definido para ellos
    else:
        return n * factorial(n - 1) # Se realiza la recursión multiplicando el número por el factorial del número anterior hasta llegar a 0.
    
numero = int(input("Escriba un numero para calcular su factorial: ")) # Se solicita al usuario que ingrese un número para calcular su factorial
if numero < 0: # Se verifica si el número es negativo o positivo, ya que el factorial no se puede calcular para números negativos
    print("El factorial no se puede calcular en números negativos.") # Se muestra un mensaje de error indicando que el factorial no se puede calcular para números negativos.
else:
    print(f"El factorial de {numero} es: {factorial(numero)}") # Se imprime el resultado del factorial utilizando una f-string para mostrar el número ingresado y su factorial.