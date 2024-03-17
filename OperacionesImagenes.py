import cv2
import numpy as np
from matplotlib import pyplot as plt
imagen = cv2.imread("creator.png")
pixel = imagen[100,100]#[fila,columna]
print(pixel)
blue = imagen[100,100,0]
print(blue)
imagen[100,100] = [255,255,255]
print(imagen[100,100])
imagen.item(10,10,2)
imagen.itemset((10,10,2),100)
imagen.item(10,10,2)
print(imagen.shape,imagen.size,imagen.dtype)#(filas,columnas,canales),numeropixeles,tipodatos
b,g,r = cv2.split(imagen)#r,g,b los cambia a b,g,r
imagen = cv2.merge((b,g,r))
#imagen,top,bottom,left,right,bordertype
reflect = cv2.copyMakeBorder(imagen,10,10,10,10,cv2.BORDER_REFLECT)
plt.imshow(reflect,"gray")