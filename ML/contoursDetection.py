import cv2
import numpy as np
import utils

framewidth = 500
framehight = 320
cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, framehight)


def empty(a):
    pass


def getcontour(img, imgcontour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:  # Corrected loop structure to iterate through contours
        area = cv2.contourArea(cnt)
        areamin = cv2.getTrackbarPos("area", "parameter")

        if area > areamin:
            cv2.drawContours(imgcontour, cnt, -1, (225, 0, 225), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgcontour, (x, y), (x + w, y + h), (0, 225, 0), 5)
            cv2.putText(imgcontour, "points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 225, 0), 2)
            cv2.putText(imgcontour, "area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 225, 0), 2)


cv2.namedWindow("parameter")
cv2.resizeWindow("parameter", 640, 420)

cv2.createTrackbar("Threshold1", "parameter", 150, 255, empty)
cv2.createTrackbar("Threshold2", "parameter", 20, 255, empty)
cv2.createTrackbar("area", "parameter", 5000, 30000, empty)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    imgcontour = img.copy()

    blurimg = cv2.GaussianBlur(img, (7, 7), 1)
    grayimg = cv2.cvtColor(blurimg, cv2.COLOR_BGR2GRAY)  # Corrected color conversion
    Threshold1 = cv2.getTrackbarPos("Threshold1", "parameter")
    Threshold2 = cv2.getTrackbarPos("Threshold2", "parameter")
    cannyimg = cv2.Canny(grayimg, Threshold1, Threshold2)
    kernel = np.ones((5, 5))
    dilimg = cv2.dilate(cannyimg, kernel, iterations=1)

    getcontour(dilimg, imgcontour)  # Added function call to getcontour

    imgstack = utils.StackImages(0.8, ([img, blurimg, grayimg], [dilimg, imgcontour, dilimg]))
    cv2.imshow("stack", imgstack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()