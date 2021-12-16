#Gaussian blur-instead of a box filter consisting of equal filter coefficients, a Gaussian kernel is used 
# A Gaussian kernel is a kernel with the shape of a Gaussian (normal distribution) curve.
import cv2
img=cv2.imread("DiscoveryMuseum.jpg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gaussian_blur=cv2.GaussianBlur(gray_image,(3,3),55)
cv2.imshow("GAUSSIAN BLUR",gaussian_blur)
cv2.waitKey(0)
#APPLICATION:Gaussian filtering is highly effective in removing Gaussian noise from the image.
