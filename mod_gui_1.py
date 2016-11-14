import cv2
import numpy as np
import mod_2 as image_analysis
from math import sqrt
import mod_match_HU

def distance(point1, point2):
    return sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)


def threshold_otsu(frame):
	
	#value = (35,35)
	#blur = cv2.GaussianBlur(gray,value,0)
	ret,thresh1 = cv2.threshold(frame,75,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	return thresh1

def threshold_normal(frame):
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	retval, threshold = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY_INV)
	return threshold



def find_fingers(centre, radius, poly_points):
    error_margin = radius*0.25
    finger_points = []
    for i in range(len(poly_points)):
        if distance(centre, poly_points[i][0]) > radius+error_margin:
            finger_points.append(poly_points[i][0])
    print len(finger_points)        
    return finger_points

def find_minimum_ycord(points):
    minimum_y = 480
    output = (0, 0)
    for point in points:
        if point[1] < minimum_y:
            minimum_y = point[1]
            output = point
    return output        


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






# cap = cv2.VideoCapture(0)

# frequency_dict = {}
# frequency_of_finger = [0, 0, 0, 0, 0, 0]
# point_prev = (0, 0)

# l_prev = "none"



# while(True):
# 	ret, frame = cap.read()
# 	#cv2.rectangle(frame,(300,300),(100,100),(0,255,0),0)
# 	#frame=cv2.fliqp(frame,1)
# 	frame=cv2.flip(frame,1)
# 	cv2.rectangle(frame,(300,300),(100,100),(0,255,0),0)
# 	crop_frame = frame[100:300, 100:300]
# 	cv2.imshow("original",frame)
# 	#print frame.shape
# 	gray = cv2.cvtColor(crop_frame,cv2.COLOR_BGR2GRAY)
# 	gray = cv2.medianBlur(gray,15)
# 	thresh1 = threshold_otsu(gray)
# 	#median = cv2.medianBlur(thresh1,15)
# 	#cv2.imshow("threshold",thresh1)
# 	cv2.imshow("thresh1",thresh1)
# 	#blob_frame = focus_hand_blob(gray)
# 	dilation = region_filling(thresh1)
# 	edges = canny_edge_detection(dilation)
# 	#cv2.imshow("dilation2",edges)
# 	#contours = image_analysis.contours(edges)
# 	#largest_contour = image_analysis.max_contour(contours)
# 	cnt,drawing= image_analysis.contour_operation(crop_frame,dilation)
# 	if cnt is not None and len(cnt)<=1000:
# 		#print len(cnt)
# 		mod_match_HU.find_closest_match(cnt)
# 	# else:
# 	# 	print -1
# 	# cnt,drawing = image_analysis.contour_operation(crop_frame,dilation)
# 	centr,radius,drawing=image_analysis.convexity_defects(cnt,drawing)
# 	# #radius = calculate_radius(cnt,centr)
# 	#pointOfFingers = find_fingers(centr, radius, drawing)
	
# 	#print len(pointOfFingers)-2
# 	#cv2.imshow("covex",drawing)
# 	if cv2.waitKey(10) & 0xFF == ord('q'):
# 		break

# cap.release()
# cv2.destroyAllWindows()