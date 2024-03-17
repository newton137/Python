import time
def sumatoria(n):
    inicio = time.time()
    suma = 0
    for x in range(1,n+1):
        suma += x
    final = time.time()
    return suma,final-inicio
print("La suma es de %d y requirió %10.10f segundos"%sumatoria(100000000))