#Averaging-done by convolving the image with a normalized box filter. It simply takes the average of all the pixels
#under kernel area and replaces the central element with this average.
import cv2

img=cv2.imread("DiscoveryMuseum.jpg")
avg_blur=cv2.blur(img,(5,5))
cv2.imshow("AVERAGING",avg_blur)
cv2.waitKey(0)
#APPLICATION:we can blur the area we want to by specifying width and height of the kernel
