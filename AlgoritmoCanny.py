import cv2
import numpy as np
from matplotlib import pyplot as plt

imagen = cv2.imread("creator.png")
bordes = cv2.Canny(imagen,100,150)

plt.subplot(121), plt.imshow(imagen,cmap="Greens")
plt.title("Original"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(bordes,cmap="Purples")
plt.title("Bordes"), plt.xticks([]), plt.yticks([])
plt.show()