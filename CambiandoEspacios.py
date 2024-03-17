import cv2
banderas = [i for i in dir(cv2) if i.startswith("COLOR_")]
print(banderas)
cv2.cvtColor("creator.png",banderas)