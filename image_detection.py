import cv2
image=cv2.imread("C:/Users/Kanishk/OneDrive/Pictures/image_human.jpg")
#image=image.resize(image,1.3)
cascade=cv2.CascadeClassifier('FaceFront.xml')
faces=cascade.detectMultiScale(image,1.3)
#print(faces)
for x,y,w,h in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    
cv2.imshow('result',image)
