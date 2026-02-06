def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
resultado = fahrenheit_a_celsius(fahrenheit)
print(f"La temperatura en grados Celsius es: {resultado:.2f} °C")
