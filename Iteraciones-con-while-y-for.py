# Iteraciones con while y for en python

cadena = "Hola Mundo"
                            # Con while es necesario declarar la variable iteradora
i = 0

while i < len(cadena):
    temp = cadena[i]
    print(temp, end=(" "))
    i+=1

"""
for i in cadena:
    print(i, end=(" "))
"""