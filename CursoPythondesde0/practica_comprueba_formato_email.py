# Ejercicio 3:
# Crea un programa que pida introducir una dirección de email por teclado. El programa
# debe imprimir en consola si la dirección de email es correcta o no en función de si esta
# tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o
# ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de la dirección de email
# o al final, la dirección también será errónea


#contador = 0
#miEmail=input("Introduce tu dirección de email: ")

#for i in miEmail:
#    if (i=="@" or i=="."):
#        contador = contador + 1

#if contador == 2:
#    print("El email es correcto")
#else:
#    print("El email no es correcto")

tiene_arroba = False
tiene_punto = False
miEmail=input("Introduce tu dirección de email: ")

for i in miEmail:
    if (i == "@"): 
        tiene_arroba = True
    elif (i == "."):
        tiene_punto = True

if (tiene_arroba and tiene_punto):
    print("El email es correcto")
else:
    print("El email no es correcto")
