import cv2
import numpy as np


circles =np.zeros((4,2),np.int_)
counter =0

def mousePoints(event,x,y,flag,params):
    global counter
    if event==cv2.EVENT_LBUTTONDOWN:
        circles[counter]=x,y
        counter=counter+1
        print(circles)


img=cv2.imread("Resources/card.png")
cv2.imshow("img",img)

while True:
    if counter==4:
       hight, width = 250, 250
       pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
       pts2 = np.float32([[0, 0], [width, 0], [0, hight], [width, hight]])
       matrix = cv2.getPerspectiveTransform(pts1, pts2)
       out = cv2.warpPerspective(img, matrix, (width, hight))
       cv2.imshow("out", out)

    for x in range(0,4):
      cv2.circle(img,(circles[x][0],circles[x][1]),3,(255,0,0),cv2.FILLED)

    cv2.setMouseCallback("img", mousePoints)
    cv2.waitKey(1)