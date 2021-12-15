
import cv2
import matplotlib.pyplot as plt
import numpy
import imutils

image1 = cv2.imread('dark1.jpg')
image2 = cv2.imread('medium.jpg')
image3 = cv2.imread('bright1.jpg')

resize_img1 = cv2.resize(image1,(720, 720))
#resize_img2 = cv2.resize(image2,(720, 720))
resize_img3= cv2.resize(image3,(720, 720))

gray_image1 = cv2.cvtColor(resize_img1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray_image3 = cv2.cvtColor(resize_img3, cv2.COLOR_BGR2HSV)


cv2.imshow("dark",gray_image1)
cv2.imshow("mid",gray_image2)
cv2.imshow("light",gray_image3)
cv2.waitKey(0)
histogram1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
histogram2= cv2.calcHist([gray_image2], [0], None, [256], [0, 256])
histogram3 = cv2.calcHist([gray_image3], [0], None, [256], [0, 256])

plt.plot(histogram1, color='k')
plt.show()
plt.plot(histogram2, color='k')
plt.show()
plt.plot(histogram3, color='k')
plt.show()


