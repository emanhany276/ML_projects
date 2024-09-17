from tkinter.constants import CASCADE

import cv2



mypath ="data\haarcascade_frontalface_alt.xml"
camerano=0
camerabrightness=190
objectname="face"
framewidth=640
framehight=480
color=(225,0,225)


cap=cv2.VideoCapture(camerano)
cap.set(3,640)
cap.set(4,480)

def empty(a):
    pass

cv2.namedWindow("result")
cv2.resizeWindow("result",(framewidth,framehight+100))
cv2.createTrackbar("scale","result",400,1000,empty)
cv2.createTrackbar("Neig","result",0,20,empty)
cv2.createTrackbar("Minarea","result",0,100000,empty)
cv2.createTrackbar("Brightness","result",180,255,empty)


cascade=cv2.CascadeClassifier(mypath)

while True:
    camerabrightness=cv2.getTrackbarPos("Brightness","result")
    cap.set(10,camerabrightness)

    success,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)

    scaleval=1+(cv2.getTrackbarPos("scale","result")/1000)
    neig=cv2.getTrackbarPos("Neig","result")

    objects= cascade.detectMultiScale(gray,scaleval,neig)

    for(x,y,w,h) in objects:
        area=w*h
        minarea=cv2.getTrackbarPos("Minarea","result")
        if area>minarea:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
            cv2.putText(img,objectname,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            roi_color=img[y:y+h,x:x+w]

        cv2.imshow("result",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break