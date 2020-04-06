# Ejercicio 3:
# Crea un programa que pida introducir una dirección de email por teclado. El programa
# debe imprimir en consola si la dirección de email es correcta o no en función de si esta
# tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o
# ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de la dirección de email
# o al final, la dirección también será errónea


TIENE_ARROBA = False
NUMERO_ARROBAS = 0

email = input("Introduce tu dirección de email: ")

for i in email:
    if (i == "@"):
        TIENE_ARROBA = True
        NUMERO_ARROBAS = NUMERO_ARROBAS + 1

if (TIENE_ARROBA and NUMERO_ARROBAS == 1 and email[0] != "@" and email[-1] != "@"):
    print("El email introducido es correcto")
else:
    print("El email introducido no es correcto")

