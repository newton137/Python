import timeit,random
for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i,"from __main__ import random,x")
    x = list(range(i))
    tiempoLista = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    tiempoDiccionario = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f"%(i,tiempoLista,tiempoDiccionario))