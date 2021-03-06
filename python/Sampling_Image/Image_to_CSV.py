# coding:UTF-8
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

# Read Image File
img = cv.imread("../../data/images/YOASOBI.jpg")

# Sampling
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
ret,img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# Array to Numpy
img_array = np.asarray(img)

# Debug: Show 
#  Image
# plt.imshow(img_array)
# plt.show()

# Print CSV Format
print('x,y')
for y in range(img_array.shape[0]):
  for x in range(img_array.shape[1]):
    if img_array[y][x][0] != 255 and img_array[y][x][1] != 255 or img_array[y][x][2] != 255:
      print('{0},{1}'.format(x, y))
