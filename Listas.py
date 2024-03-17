from timeit import Timer
def lista1():
    lista = []
    for i in range(1000):
        lista.append(i)
def lista2():
    lista = [i for i in range(1000)]
def lista3():
    lista = list(range(1000))
tiempo1 = Timer("lista1()","from __main__ import lista1")
print("append ",tiempo1.timeit(number=1000)," milisegundos")
tiempo2 = Timer("lista2()","from __main__ import lista2")
print("compresion ",tiempo2.timeit(number=1000)," milisegundos")
tiempo3 = Timer("lista3()","from __main__ import lista3")
print("range ",tiempo3.timeit(number=1000)," milisegundos")