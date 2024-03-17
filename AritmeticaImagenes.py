import numpy as np
import cv2

x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x,y))
print(x + y)

imagen1 = cv2.imread("creator.png")
imagen2 = cv2.imread("grafo.png")

filas,columnas,canales = imagen2.shape
roi = imagen1[0:filas,0:columnas]
imagen2Gray = cv2.cvtColor(imagen2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(imagen2Gray, 250, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
imagen1_bg = cv2.bitwise_and(roi,roi,mask = mask)
imagen2_fg = cv2.bitwise_and(imagen2,imagen2,mask = mask)
dst = cv2.add(imagen1_bg, imagen2_fg)
imagen1[0:filas,0:columnas] = dst
cv2.imshow("imagen1", imagen1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

imagen1 = imagen1[1:568,1:1001,:]
imagen2 = imagen2[1:568,1:1001,:]
fusion = cv2.addWeighted(imagen1, 0.7, imagen2, 0.3, 0)
cv2.imshow("fusion", fusion)
cv2.waitKey(0)
cv2.destroyAllWindows()