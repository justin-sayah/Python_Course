import cv2

img = cv2.imread("galaxy.jpg", 1)

resized = cv2.resize(img,(1000,500))
cv2.imshow("Galaxy", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()