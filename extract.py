# Paper -> Font and Background Color 
# Independent Text Binarization

# using egde boxes to isolate and identify
# characters; edge boxes with intensity values
# will be stord in one of the intermediate images

import cv2
import numpy as np
import sys
import os.path

# check args
if len(sys.argv) != 3:
	print "%s [input_file] [output_file]" % (sys.argv[0])
	sys.exit()
else:
	input_file = sys.argv[1]
	output_file = sys.argv[2]

if not os.path.isFile(input_file):
	print "%s file not found" % input_file
	sys.exit()

# debug flag
DEBUG = 0


# determine the pixel density
# ref: human eyes register colors differently.
# pixel intensity: 0.30R + 0.59G + 0.11B
# x,y are the coordinates of the image
def pixelIntensity(x, y):
	global img, img_y, img_x
	if y >= img_y or x >= img_x:
		# print "pixel out of bounds ("+str(y)+","+str(x)+")"
		return 0

	pixel = img[y][x]
	return 0.30*pixel[2] + 0.59*pixel[1] + 0.11*pixel[0]


# checks if contour is
# a connected shape
def isConnected(contour):
	first = contour[0][0]
	last = contour[len(contour)-1][0]
	return abs(first[0] - last[0]) <= 1 and abs(first[1] - last[1]) <= 1


# helper function
# gets the contour at a given index
def getContour(index):
	global contours
	return contours[index]

