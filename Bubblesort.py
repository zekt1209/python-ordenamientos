# Bubblesorth

array = [8,6,7,1,4,9,2,3,5]
bandera = False

while bandera == False:
    bandera = True                  # Va a indicar que la lista ya esta ordenada porque ya no se cumple la condicional de la linea 9
    for i in range(len(array)-1):   # Recorre el arreglo hasta el penultimo numero del arreglo
        if array[i] > array[i+1]:
            aux = array[i]          # Guarda la posicion [i] del arreglo en aux
            array[i] = array[i+1]   # Le asignamos a la posicion [i] el valor de [i + 1]
            array[i+1] = aux        # Le asignamos a [i+1] el valor inicial de [i] guardado en aux
            bandera = False         # Indica que la lista sigue desordenada

print(array)