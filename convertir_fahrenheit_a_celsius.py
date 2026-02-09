def fahrenheit_a_celsius(fahrenheit): # Se define la función que convierte Fahrenheit a Celsius
    celsius = (fahrenheit - 32) * 5 / 9 # Se realiza la conversión utilizando la fórmula (F - 32) * 5/9
    return celsius # Se devuelve el resultado de la conversión

fahrenheit = float(input("Ingrese el numero de grados Fahrenheit: ")) # Se solicita al usuario que ingrese la temperatura en grados Fahrenheit
resultado = fahrenheit_a_celsius(fahrenheit) # Se llama a la función para convertir la temperatura
print(f"La temperatura en grados Celsius es: {resultado:.2f} °C") # Se imprime el resultado
