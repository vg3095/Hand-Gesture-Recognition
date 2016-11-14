import cv2 as opencv
import numpy as np
import image_analysis
from math import sqrt
import match_DB

def distance(point1, point2):
    return sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)


def threshold_otsu(frame):
	ret,thresh1 = opencv.threshold(frame,75,255,opencv.THRESH_BINARY_INV+opencv.THRESH_OTSU)
	return thresh1




def region_filling(frame):
	#Have to Tune structuring element 
	kernel = opencv.getStructuringElement(opencv.MORPH_ELLIPSE, (5, 5))
	dilation = opencv.dilate(frame,kernel,iterations = 1)
	img_bw = 255*(frame> 5).astype('uint8')
	#opencv.imshow("dilate",dilation)	
	return dilation

def canny_edge_detection(frame):
	edges = opencv.Canny(frame,70,200)
	#opencv.imshow("edges",edges)
	return edges


