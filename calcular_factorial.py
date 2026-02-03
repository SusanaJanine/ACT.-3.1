numero = int(input("Ingrese un número para calcular su factorial: "))
def calcular_factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es: {resultado}")