# Ejercicio 2:
# Crea un programa que pida números positivos indefinidamente. El programa termina
# cuando se introduce un número negativo. Finalmente el programa muestras la suma de
# todos los números introducidos


suma_total = 0

numero = int(input("Introduce un número positivo: "))
suma_total = suma_total + numero

while (numero >= 0):
    numero = int(input("Introduce un número positivo: "))
    suma_total = suma_total + numero

print("Has introducido un número negativo")
print("La suma total de los números es de " + str(suma_total))
print("Programa finalizado")
