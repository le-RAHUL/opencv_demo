import cv2
import imutils

img=cv2.imread("car.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gauss_blur=cv2.GaussianBlur(gray_img,(11,11),25)

thresh,threshold_img=cv2.threshold(gauss_blur,170,255,cv2.THRESH_BINARY)

cv2.imshow("thresholded image",threshold_img)
cv2.waitKey()

cnt = cv2.findContours(threshold_img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = imutils.grab_contours(cnt)

for i in cnt:
	cnt_draw = cv2.drawContours(img.copy(),[i], -1, (0, 255, 0), 5)
	cv2.imshow("Contours",cnt_draw)
	cv2.waitKey()
	
	

