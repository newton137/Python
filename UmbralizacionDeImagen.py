import cv2
import numpy as np
from matplotlib import pyplot as plt

imagen = cv2.imread("creator.png")
ret,umbral1 = cv2.threshold(imagen,125,255,cv2.THRESH_BINARY)
ret,umbral2 = cv2.threshold(imagen,125,255,cv2.THRESH_BINARY_INV)
ret,umbral3 = cv2.threshold(imagen,125,255,cv2.THRESH_TRUNC)
ret,umbral4 = cv2.threshold(imagen,125,255,cv2.THRESH_TOZERO)
ret,umbral5 = cv2.threshold(imagen,125,255,cv2.THRESH_TOZERO_INV)
imagenes = [imagen,umbral1,umbral2,umbral3,umbral4,umbral5]
arreglo = np.arange(6)
for a in arreglo:
    plt.subplot(2,3,a+1),plt.imshow(imagenes[a],"gray")
    plt.xticks([]),plt.yticks([])
plt.imshow()