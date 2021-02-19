import cv2 

img = cv2.imread('Samples/RGB.png')
# loads an image (formats including jpg and png are supported)
# relative or absolute file path could be provided

print(img.shape)
# dimensions of image

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# conversion from BGR to RGB colour schemes

# Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.rectangle(img1, (55,15), (470,405) , (0,0,0) , 3)

# Syntax: cv2.circle(image, center_coordinates, radius, color, thickness)
cv2.circle(img1, (175,282), 120, (0,0,0) , 2)

# Syntax : cv2.putText(img, text, org, font, fontScale, color, int thickness)
text = '(Transformed)'
font = cv2.FONT_HERSHEY_SIMPLEX 
cv2.putText(img1, text , (160,480), font, 1 , (0,0,0), 2)

cv2.imshow('Original image',img)
cv2.imshow('Transformed image',img1)

cv2.waitKey(10000)
# displays windows for 10s

