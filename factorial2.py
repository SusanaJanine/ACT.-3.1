def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)
    
numero = int(input("Escriba un numero para calcular su factorial: "))
if numero < 0:
    print("El factorial no se puede calcular en números negativos.")
else:
    print(f"El factorial de {numero} es: {factorial(numero)}")