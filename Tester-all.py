import numpy as np
import cv2 as cv
import random

width = 1000
height = 650
w_trees = 40
ground_level = height-150

# color, light_color, color = (30, 120, 30), (20, 200, 1), (40, 60, 100)
########################## Or ###############
color = (60, 10, 60)
light_color = (20, 0, 1)
color = (50, 60, 100)

bg = np.zeros((height, width, 4), dtype=np.uint8)

cv.rectangle(bg,(width,0), (0, ground_level), (255, 225, 95), -1)
cv.rectangle(bg, (width, ground_level), (0, height), color, -1)

cv.imshow('forest of object', bg)

cv.waitKey(0)

# cv.destroyAllWindow()

#########################################################################

image = np.zeros((200, 700, 2), dtype=np.uint8)

cv.rectangle(image, (0,0), (900))