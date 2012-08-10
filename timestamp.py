#!/usr/bin/python
import cv #Import functions from OpenCV
import time
cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE)
image=cv.LoadImage('coffee.jpeg', cv.CV_LOAD_IMAGE_COLOR) #Load the image
font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8) #Creates a font
x = 100
y = 100
t = time.asctime()
cv.PutText(image,t, (x,y),font, 255) #Draw the text
cv.SaveImage('coffee.png', image) #Saves the image

