import numpy as np
import cv2
from matplotlib import pyplot as plt

imagen = cv2.imread("creator.png")
histograma = cv2.calcHist([imagen],[1],None,[256],[0,256])#imagen,canales,mascara,tamaño,rango
print(histograma)
histogram,bins = np.histogram(imagen.ravel(),256,[0,256])
print(histogram)
plt.hist(imagen.ravel(),256,[0,256])
plt.show()
color = ("b","g","r")
for i,col in enumerate(color):
    histograma = cv2.calcHist([imagen],[i],None,[256],[0,256])
    plt.plot(histograma,color = col)
    plt.xlim([0,256])
plt.show()
