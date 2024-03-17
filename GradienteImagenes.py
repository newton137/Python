import cv2
import numpy as np
from matplotlib import pyplot as plt

imagen = cv2.imread("creator.png",0)
laplacian = cv2.Laplacian(imagen,cv2.CV_8U)
sobelx = cv2.Sobel(imagen,cv2.CV_8U,1,0,ksize=3)#se eliminan lineas horizontales
sobely = cv2.Sobel(imagen,cv2.CV_8U,0,1,ksize=3)#se eliminan lineas verticales

plt.subplot(2,2,1), plt.imshow(imagen,cmap="gray")
plt.title("Original"), plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2), plt.imshow(laplacian,cmap="gray")
plt.title("Laplaciano"), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3), plt.imshow(sobelx,cmap="gray")
plt.title("Sobel x"), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4), plt.imshow(sobely, cmap="gray")
plt.title("Sobel y"), plt.xticks([]), plt.yticks([])
plt.show()   