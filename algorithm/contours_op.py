import cv2
import numpy as np 
import image_analysis
import process_image
from matplotlib import pyplot as plt
import cPickle

def threshold_otsu(frame):
	ret,thresh1 = cv2.threshold(frame,75,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	return thresh1


def operations(frame):
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	dilation = process_image.region_filling(gray)
	return dilation



def find_largest_contour(contours):
    maxarea = 0
    pos = -1
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if area > maxarea:
            maxarea = area
            pos = i
    return pos
