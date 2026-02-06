def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    try:
        numero = int(input("Ingrese un número entero para calcular su factorial: "))
        resultado = factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")

main()
