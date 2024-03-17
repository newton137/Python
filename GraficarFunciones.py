import matplotlib.pyplot as mpl
import numpy as np
x = np.linspace(-10,5,100)#inicio,fin,división del rango
y = (x**3+5*(x**2)+2*x-8)#calcular y
mpl.plot(x,y,"m-",linewidth = 2)
mpl.show()
for i in range(-10,10,):
    print(i,i**3+3.5*(i**2)+3.5*i+1)