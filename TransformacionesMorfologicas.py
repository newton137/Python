import cv2
import numpy as np

imagen = cv2.imread("creator.png",0)
kernel = np.ones((7,7),np.uint8)
erosion = cv2.erode(imagen,kernel,iterations=1)
dilatacion = cv2.dilate(imagen,kernel,iterations=1)
apertura = cv2.morphologyEx(imagen,cv2.MORPH_OPEN,kernel)
cierre = cv2.morphologyEx(imagen,cv2.MORPH_CLOSE,kernel)
gradiente = cv2.morphologyEx(imagen,cv2.MORPH_GRADIENT,kernel)
blackHat = cv2.morphologyEx(imagen,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow("Erosión", erosion)
cv2.imshow("Dilatación", dilatacion)
cv2.imshow("Apertura", apertura)
cv2.imshow("Cierre", cierre)
cv2.imshow("Gradiente", gradiente)
cv2.imshow("BlackHat", blackHat)
cv2.waitKey(0)
cv2.destroyAllWindows()