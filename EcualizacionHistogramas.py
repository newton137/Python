import numpy as np
import cv2
from matplotlib import pyplot as plt

imagen = cv2.imread("creator.png")
histograma, bins = np.histogram(imagen.flatten(),256,[0,256])#genera histograma
funDisAc = histograma.cumsum()#genera la funcion de distribucion acumulada
funDisAcNor = funDisAc * histograma.max()/funDisAc.max()
#genera graficos del histograma y de la funcion de distribucion acumulada
plt.plot(funDisAcNor, color = "b")
plt.hist(imagen.flatten(),256,[0,256],color = "r")
plt.xlim([0,256])
plt.legend(("funDisAc","Función de distribución acumulada"),loc ="upper right")
plt.show()
enmascarar = np.ma.masked_equal(funDisAc,0)#enmascaran valores igual a 0
enmascarar = (enmascarar - enmascarar.min())*255/(enmascarar.max() - enmascarar.min())#transformacion de ecualizacion
cdf = np.ma.filled(enmascarar, 0).astype("uint8")#se rellenan valores enmascarados con 0
img = cdf[imagen]#se aplica ecualización de pixeles a la imagen original
cv2.imshow("Original",imagen)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.plot(cdf, color = "b")
plt.hist(img.flatten(),256,[0,256],color = "r")
plt.xlim([0,256])
plt.legend(("funDisAc","Función de distribución acumulada"),loc ="upper right")
plt.show()