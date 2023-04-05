import cv2
img = cv2.imread("Reseources/deneme.jpg")

#cv2.imshow("deneme",img)
print(img.shape)
width ,height = 1000 , 1000
imgResize = cv2.resize(img,(width,height))
print(imgResize.shape)

imgCropped = img[300:570,430:754]
imCropResize= cv2.resize(imgCropped,(img.shape[1],img.shape[0]))

cv2.imshow("image",img)
cv2.imshow("cropped",imgCropped)
cv2.imshow("resized",imCropResize)




cv2.waitKey(0)
