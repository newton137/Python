import cv2
import numpy as np
img = cv2.imread('creator.png',0)
cv2.imshow("imagen2", img)
key = cv2.waitKey(0)
if key == ord("d"):
    cv2.destroyAllWindows()
elif key == ord("g"):
    cv2.imwrite("creatorGray.png", img)
    cv2.destroyAllWindows()
       