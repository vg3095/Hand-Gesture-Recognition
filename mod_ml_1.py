import cv2
import numpy as np 
import mod_2 as image_analysis
from matplotlib import pyplot as plt
import cPickle

def threshold_otsu(frame):
	
	#value = (35,35)
	#blur = cv2.GaussianBlur(gray,value,0)
	ret,thresh1 = cv2.threshold(frame,75,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	return thresh1

def threshold_normal(frame):
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	retval, threshold = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY_INV)
	return threshold



def region_filling(frame):
	#Have to Tune structuring element 
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
	dilation = cv2.dilate(frame,kernel,iterations = 1)
	img_bw = 255*(frame> 5).astype('uint8')
	#cv2.imshow("dilate",dilation)	
	return dilation

def canny_edge_detection(frame):
	edges = cv2.Canny(frame,70,200)
	cv2.imshow("edges",edges)
	return edges


def operations(frame):
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# gray = cv2.medianBlur(gray,15)
	# thresh1 = threshold_otsu(gray)

	# dilation = region_filling(thresh1)
	dilation = region_filling(gray)
	return dilation


def show_image(frame):
	while(True):
		cv2.imshow("im",frame)
		if cv2.waitKey(10) & 0xFF == ord('q'):
			break


def find_largest_contour(contours):
    maxarea = 0
    pos = -1
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if area > maxarea:
            maxarea = area
            pos = i
    return pos

def store_HU(img,s):
	#show_image(img)
	#print cv2.moments(img)
	HU_Moments = cv2.HuMoments(cv2.moments(img)).flatten()
	filename = "HU/" + s + ".txt"
	f = open(filename, "w")
	f.write(cPickle.dumps(HU_Moments))
	f.close()

def store_contours(img,s):
	#show_image(img)
	#print cv2.moments(img)
	contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	pos = find_largest_contour(contours)
	cnt = contours[pos]
	filename = "database_contour/" + s + ".txt"
	f = open(filename, "w")
	f.write(cPickle.dumps(cnt))
	f.close()

	hull1 = cv2.convexHull(cnt, returnPoints=True)
	pts = np.array(hull1, np.int32)
	pts = pts.reshape((-1, 1, 2))
	poly = cv2.approxPolyDP(pts, 20, True)	
	
	filename = "database_poly/" + s + ".txt"
	f = open(filename, "w")
	f.write(cPickle.dumps(poly))
	f.close()


def create_HU():
	letters = [1,2,3,4,5]
	
	for l in letters:
	    imageName = "templates/" + str(l) + ".JPG"
	    print imageName
	    image = cv2.imread(imageName)
	    image=operations(image)
	    #print image
	    store_HU(image, str(l))
	    store_contours(image, str(l))

#create_HU()


