
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
