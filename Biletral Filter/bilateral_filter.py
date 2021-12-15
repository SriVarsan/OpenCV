#Bilateral Filter- uses a Gaussian filter in the space domain, but it also uses one more (multiplicative) Gaussian
#filter component which is a function of pixel intensity differences
import cv2
i=cv2.imread("statue.jpeg")
bblur=cv2.bilateralFilter(i,200,200,0)
cv2.imshow("BILATERAL FILTER", bblur)
cv2.imwrite("girl_bilated.png", bblur)
cv2.waitKey(0)
#APPLICATIONS: Highly effective at noise removal while preserving edges,in previous filtering edges will be blured
