# Ejercicio 1:
# Crea un programa que pida números infinitamente. Los números introducidos deben
# ser cada vez mayores El programa finalizará cuando se introduce un número menor que el anterior


numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce un número mayor que el anterior: "))

while (numero2 > numero1):
    numero1 = numero2
    numero2 = int(input("Introduce un número mayor que el anterior: "))

print("Has introducido un número que no es mayor que el anterior. Programa finalizado")
