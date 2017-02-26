import cv2 as opencv
import numpy as np
from math import sqrt
import math

iter = 0


def contour_operation(img,frame):

    contours, hierarchy = opencv.findContours(frame.copy(),opencv.RETR_TREE, opencv.CHAIN_APPROX_NONE)

    cnt = max(contours, key = lambda x: opencv.contourArea(x))
    drawing = np.zeros(img.shape,np.uint8)
    hull = opencv.convexHull(cnt)
    opencv.drawContours(drawing,[cnt],0,(0,255,0),2)
    opencv.drawContours(drawing,[hull],0,(0,0,255),2)   
    hull = opencv.convexHull(cnt,returnPoints = False)
    defects = opencv.convexityDefects(cnt,hull)
    #poly = correction_poly(hull)
    count_defects = 0
    global iter 
    iter = 0
    if defects is not None:
        for i in range(defects.shape[0]):
                    iter = iter+1
                    s,e,f,d = defects[i,0]
                    start = tuple(cnt[s][0])
                    end = tuple(cnt[e][0])
                    far = tuple(cnt[f][0])
                    a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                    b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                    c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
                    angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
                    if angle <= 90:
                        count_defects += 1
                        opencv.circle(drawing,far,1,[0,0,255],-1)
                    #dist = opencv.pointPolygonTest(cnt,far,True)
                    opencv.line(drawing,start,end,[0,255,0],2)
                    opencv.circle(drawing,far,5,[0,0,255],-1)
	    #print iter
    return cnt,drawing
	
