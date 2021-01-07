import numpy as np
import cv2

# https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('Data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Data/haarcascade_eye.xml')
# loading pre - trained classifiers

img = cv2.imread('Samples/sample_face.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# reading image anc converting to grayscale to facillitate detection

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# detects faces within image
# parameters are fine - tuned

for (x,y,w,h) in faces:
	# accessing top left coordinate, height, width
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    # extracts the ROI (Region of Interest)

    eyes = eye_cascade.detectMultiScale(roi_gray)
    # detects eyes within the region of the face

    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
# displays window until user presses 'esc' key
cv2.destroyAllWindows()