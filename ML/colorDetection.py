import cv2
import numpy as np

# Set frame dimensions
frame_height = 500
frame_width = 320

def empty(a):
    pass

# Create a window named "Hsv" with trackbars for tuning HSV values
cv2.namedWindow("Hsv")
cv2.resizeWindow("Hsv", 640, 240)

# Create trackbars for Hue, Saturation, and Value adjustments
cv2.createTrackbar("HUE Min", "Hsv", 0, 179, empty)
cv2.createTrackbar("HUE Max", "Hsv", 179, 179, empty)
cv2.createTrackbar("SAT Min", "Hsv", 0, 255, empty)
cv2.createTrackbar("SAT Max", "Hsv", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "Hsv", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "Hsv", 255, 255, empty)

# Initialize video capture
cap = cv2.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    # Convert the image to HSV color space
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get the current positions of the trackbars
    h_min = cv2.getTrackbarPos("HUE Min", "Hsv")
    h_max = cv2.getTrackbarPos("HUE Max", "Hsv")
    s_min = cv2.getTrackbarPos("SAT Min", "Hsv")
    s_max = cv2.getTrackbarPos("SAT Max", "Hsv")
    v_min = cv2.getTrackbarPos("VALUE Min", "Hsv")
    v_max = cv2.getTrackbarPos("VALUE Max", "Hsv")

    # Define lower and upper bounds for the HSV mask
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    hstack =np.hstack([img,result])

    # Display the original, HSV, mask, and result images

    #cv2.imshow("originalimg", img)
    cv2.imshow("Hsvlimg", imgHsv)
    cv2.imshow("mask", mask)
    #cv2.imshow("result", result)
    cv2.imshow("horz",hstack)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()