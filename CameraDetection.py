import numpy as np
import cv2

from GravityPhysics import *


def lidarFindObj(pc, x0, x1, y0, y1, z0, z1, dropH):
	#returns average z value of an object (where z is the height dropped in point cloud cordinates)
	zSum = 0
	count = 0
	for x, y, z in zip(pc.pc_data['x'], pc.pc_data['y'], pc.pc_data['z']):
		if (x >= x0 and x <= x1) and (y >= y0 and y <= y1) and (z >= z0 and z <= z1):
		    zSum += (dropH-z)
		    count += 1
	if (count == 0):
		return -1 #returns -1 if no data was found in specified range
	return (zSum/count)

def cameraHueView(image, hue0, hue1, sat0 = 20, sat1 = 220, lum0 = 20, lum1 = 220):
	#takes a image and changes the values with in the hue range specified to white and the rest to black and then shows image
	#Main use is to find best range of values to find a specific object
	avg = 0
	count = 0
	image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	for y in range(image.shape[0]):
		for x in range(image.shape[1]):
		    (h, s, v) = image[y, x]
		    # check for basketball color
		    if (h >= hue0 and h <= hue1 and s >= sat0 and s <= sat1 and v >= lum0 and v <= lum1):
			avg += y
			count += 1
			image[y,x] = (255,255,255)
		    else:
			image[y,x] = (0,0,0)
	cv2.imshow('image', image)
	cv2.waitKey(0)
	if(count == 0):
		return -1 #returns -1 if nothing is found
	return avg / float(count)

def cameraAvgY(image, hue0, hue1, sat0, sat1, lum0, lum1):
	#returns the average y coordinante of pixels in the image which are in the hue range [hue0,hue1]
	avg = 0
	count = 0
	for y in range(image.shape[0]):
		for x in range(image.shape[1]):
		    (h, s, v) = image[y, x]
		    # check for basketball color
		    if (h >= hue0 and h <= hue1): #and s > 10 and s < 220 and v > 20 and v < 200):
			avg += y
			count += 1
	if(count == 0):
		return -1 #returns -1 if nothing is found
	return avg / float(count)

def cameraFindObj(image, groundH, dropH, bHeight, hue0 = 0, hue1 = 10, sat0 = 20, sat1 = 220, lum0 = 20, lum1 = 220):
	width = 1008
	height = 756
	image = cv2.resize(image, (width, height))
	image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	#get average y coord of object based off hue color
	avg = cameraAvgY(image,hue0,hue1, sat0, sat1, lum0, lum1)
	if(avg == -1):
		return -1 #return -1 when nothing was found

	diff = dropH - avg
	pixelHeight = dropH - groundH
	percentage = diff / float(pixelHeight)
	realHeight = bHeight * percentage

	return realHeight
