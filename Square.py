import cv2
import numpy as np

square = np.zeros(shape=[450, 450])
cv2.rectangle(square, (150, 150), (300, 300), color=(255, 255, 255), thickness=-1)

cv2.imshow("img", square)
cv2.waitKey(0)
