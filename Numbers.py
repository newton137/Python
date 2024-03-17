import numpy as np

matriz = np.arange(0,10,2)
print(type(matriz))
print(matriz)
dimensiones = matriz.ndim
tipo = matriz.dtype
dimension = matriz.shape
buffer = matriz.data
tamano = matriz.itemsize
elementos = matriz.size
print(dimensiones, tipo, dimension, buffer, tamano, elementos) 
print(np.identity(5,int))
ceros = np.zeros((3,4))
print(ceros)
inicial = np.linspace(1,5,5)
print(inicial)
print(np.empty(10,int))
print(np.meshgrid([1,2,3]))
x,y = np.meshgrid([1,2,3],[4,5,6])
print(x)
print(y)

a = np.array([[8,2],[8,4]])
b = a + a
print(b)
c = a * b
print(c)
b = np.dot(a,a)
print(b)
c = a*a
print(c)
d = np.multiply(a,a)
print(d)

x = np.linspace(0,90,90)
y = np.sin(x)
print(y)

import matplotlib.pyplot as mpl
a = np.linspace(0, 20, 50)
b = np.sin(a)
mpl.plot(a,b,'m-.', linewidth = 2)
mpl.plot(a+0.5,b+0.5,'y-o', linewidth = 3)
mpl.xlabel("Tiempo(s)", fontsize = 15)
mpl.ylabel("Eje Y",fontsize = 15, color = "black")
mpl.text(1,1, "texto", fontsize = 10)
mpl.title("Velocidad", fontsize = 18)
mpl.savefig("primerMatplotlib.png", dpi= 500)
mpl.show()

mpl.figure(1, [50, 75], 30, "b", "k", "true")
mpl.figure()
x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)
X,Y = np.meshgrid(x,y)
cosxy = np.cos(X**5 + Y**10)
mpl.imshow(cosxy)
mpl.colorbar()

from mpl_toolkits.mplot3d import Axes3D
figura = mpl.figure()
axe = Axes3D(figura)
x = np.arange(-10,10,0.2)
y = np.arange(-10,10,0.2)
X,Y = np.meshgrid(x,y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
axe.plot_surface(X,Y,Z,rstride = 1, cstride = 1, cmap = "jet")


