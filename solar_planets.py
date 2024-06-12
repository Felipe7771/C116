import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sol",(100,80),cv2.FONT_HERSHEY_TRIPLEX,2,(0,0,255))
cv2.putText(img,"Mercurio",(120,250),cv2.FONT_HERSHEY_TRIPLEX,0.35,(100,100,100))
cv2.putText(img,"Venus",(200,260),cv2.FONT_HERSHEY_TRIPLEX,0.4,(0,255,255))
cv2.putText(img,"Terra",(290,270),cv2.FONT_HERSHEY_TRIPLEX,0.5,(255,0,0))
cv2.putText(img,"Lua",(330,150),cv2.FONT_HERSHEY_TRIPLEX,0.3,(100,100,100))
cv2.putText(img,"Marte",(390,260),cv2.FONT_HERSHEY_TRIPLEX,0.4,(107,35,142))
cv2.putText(img,"Jupiter",(550,370),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,100,255))
cv2.putText(img,"Saturno",(750,310),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,100,100))
cv2.putText(img,"Urano",(970,285),cv2.FONT_HERSHEY_TRIPLEX,0.5,(220,255,255))
cv2.putText(img,"Netuno",(1120,280),cv2.FONT_HERSHEY_TRIPLEX,0.5,(255,0,0))

cv2.imshow("Sistema",img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)