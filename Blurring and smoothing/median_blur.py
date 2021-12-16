#Median blur-Here, the function cv2.medianBlur() computes the median of all the pixels under the kernel window and the central
#pixel is replaced with this median value.
import cv2
i=cv2.imread("DiscoveryMuseum.jpg")
median=cv2.medianBlur(i,5)      
cv2.imshow("MEDIAN BLUR",median)
cv2.waitKey(0)
#APPLICATIONS:This is highly effective in removing salt-and-pepper noise,, since the central element is always
#replaced by some pixel value in the image. This reduces the noise effectively.
