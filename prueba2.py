from matplotlib import  pyplot as plt
import cv2
img = cv2.imread("creator.png", 1)
plt.imshow(img, cmap="gray", interpolation = "bicubic")
plt.xticks([]), plt.yticks([])
plt.show()
