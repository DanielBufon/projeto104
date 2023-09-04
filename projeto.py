import cv2

image = cv2.imread("projeto 104.jpg")
cv2.putText(image,"sol",(100,80),cv2.FONT_ITALIC,2,(255,255,255))
cv2.putText(image,"mercurio",(110,180),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(image,"venus",(190,270),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(image,"terra",(300,270),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(image,"marte",(400,270),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(image,"jupiter",(500,90),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(image,"saturno",(720,110),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(image,"urano",(950,130),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(image,"netuno",(1080,130),cv2.FONT_ITALIC,0.5,(255,255,255))

cv2.imshow("resultado",image)
cv2.waitKey(0)