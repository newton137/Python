import time
def anagrama(cadena1,cadena2):
    inicio = time.time()
    arreglo1 = list(cadena1)
    arreglo2 = list(cadena2)
    arreglo1.sort()
    arreglo2.sort()
    posicion = 0
    coincide = True
    tamano = len(arreglo1)
    while posicion < tamano and coincide:
        if arreglo1[posicion] == arreglo2[posicion]:
            posicion += 1
        else:
            coincide = False
    fin = time.time()
    return coincide,fin-inicio
print("%d , %10.10f segundos"%anagrama("arroz","zorra"))