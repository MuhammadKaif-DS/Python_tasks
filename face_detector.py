# First import OpenCV library
import cv2
# Load the haar cascade classifier
a = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Capture vedio from webcam
b = cv2.VideoCapture(0)
# Read vedio frames in a loop
while True:
    c_rec,d_image = b.read()
# Convert to grayscale
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
# Detect faces
    f = a.detectMultiScale(e,1.3,6)
# Draw rectangles around faces
    for (x1,y1,w1,h1) in f:
        cv2.rectangle(d_image, (x1,y1), (x1+w1, y1+h1), (0,255,0), 10)
# Display the vedio
    cv2.imshow('img', d_image)
# Break the Loop with a key
    h = cv2.waitKey(40) & 0xff
    if h == ord('q'):
        break
# Release resources
b.release()
cv2.destroyAllWindows()