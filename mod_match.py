import mod_2
import cv2
import numpy as np
import cPickle
def find_largest_contour(contours):
    maxarea = 0
    pos = -1
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if area > maxarea:
            maxarea = area
            pos = i
    return pos


def find_closest_match(grp, poly):
    minimum = 1000
    for letter in grp:
        cnt1 = cPickle.loads(open("database_poly/" + letter+".txt").read())

        hull1 = cv2.convexHull(cnt1, returnPoints=True)
        pts = np.array(hull1, np.int32)
        pts = pts.reshape((-1, 1, 2))
        poly1 = cv2.approxPolyDP(pts, 20, True)

        temp = cv2.matchShapes(poly, poly1, 2, 0.0)
        if temp < minimum:
            minimum = temp
            l = letter
    print l,
    return l

def cont_exp(thresh):
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    pos = find_largest_contour(contours)
    cnt = contours[pos]

    hull1 = cv2.convexHull(cnt, returnPoints=True)
    pts = np.array(hull1, np.int32)
    pts = pts.reshape((-1, 1, 2))
    poly = cv2.approxPolyDP(pts, 20, True)
    return poly

grp = ["1","2","3","4"]

img = cv2.imread("2.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
poly=cont_exp(gray)
find_closest_match(grp,poly)   