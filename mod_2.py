import cv2
import numpy as np
from math import sqrt
import math


def distance(point1, point2):
    return sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def calculate_radius(cnt,centr):
	radius = 0
	cx=centr[0]
	cy=centr[1]
	for i in range(len(cnt)):
	    radius += distance((cx, cy), cnt[i][0])
	radius /= len(cnt)
	return radius


def correction_poly(hull1):
	pts = np.array(hull1, np.int32)
	pts = pts.reshape((-1, 1, 2))
	cv2.polylines(im, [pts], True, (255, 0, 0))
	poly = cv2.approxPolyDP(pts, 20, True)
	return poly

def contour_operation(img,frame):

    contours, hierarchy = cv2.findContours(frame.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cnt = max(contours, key = lambda x: cv2.contourArea(x))
    hull = cv2.convexHull(cnt)
    #poly = correction_poly(hull)
    drawing = np.zeros(img.shape,np.uint8)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
    cv2.drawContours(drawing,[hull],0,(0,0,255),2)
    #cv2.imshow("contours",drawing)
    return cnt,drawing


def convexity_defects(cnt,drawing):
	hull = cv2.convexHull(cnt,returnPoints = False)
	defects = cv2.convexityDefects(cnt,hull)
	moments = cv2.moments(cnt)
	if moments['m00']!=0:
	            cx = int(moments['m10']/moments['m00']) # cx = M10/M00
	            cy = int(moments['m01']/moments['m00']) # cy = M01/M00
	          
	centr=(cx,cy)
	mind=0
	maxd=0
	i=0
	validPoints=[]

	radius = calculate_radius(cnt,centr)
	if defects is not None:
		count_defects = 0

		for i in range(defects.shape[0]):
		        s, e, f, d = defects[i, 0]
		        start = tuple(cnt[s][0])
		        end = tuple(cnt[e][0])
		        far = tuple(cnt[f][0])
		        dis = distance(far, (cx,cy))
		        # a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
		        # b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
		        # c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
		        # angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
		        # if angle <= 90:
		        # 	count_defects += 1
		        # if dis < 1.25*radius:
		        #     validPoints.append(far)
		        #     cv2.circle(drawing, far, 20, [255, 255, 0], 1)
		    #print(i)
		#print count_defects    
	#cv2.imshow("convex defects",drawing)
	cxNew = 0
	cyNew = 0
	radiusNew = 0
	for point in validPoints:
	    cxNew += point[0]
	    cyNew += point[1]

	if len(validPoints) > 0:
	    cxNew /= len(validPoints)
	    cyNew /= len(validPoints)

	    radiusNew = 0
	    for point in validPoints:
	        radiusNew += distance((cxNew, cyNew), point)
	if len(validPoints):
	    radiusNew /= len(validPoints)
	return (cxNew,cyNew),radiusNew,drawing