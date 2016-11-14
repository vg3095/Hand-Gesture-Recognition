import cv2
import cPickle
import numpy as np
import glob
import os


file_running = ''


def find_largest_contour(contours):
    maxarea = 0
    pos = -1
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if area > maxarea:
            maxarea = area
            pos = i
    return pos


def store_contour_and_poly(img, s):
    #_, thresh = cv2.threshold(img, 100, 255, 0)
    #print thresh
    thresh = img
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    s =s.replace('.JPG','')
    s =s.replace('.jpg','')
    pos = find_largest_contour(contours)
    cnt = contours[pos]

    hull1 = cv2.convexHull(cnt, returnPoints=True)
    pts = np.array(hull1, np.int32)
    pts = pts.reshape((-1, 1, 2))
    poly = cv2.approxPolyDP(pts, 20, True)

    filename = "C:/Users/Vaibhav Gupta/Desktop/implementation/gui/modified/database_contour/" + s + ".txt"
    f = open(filename, "w")
    f.write(cPickle.dumps(cnt))
    f.close()

    filename = "C:/Users/Vaibhav Gupta/Desktop/implementation/gui/modified/database_poly/" + s + ".txt"
    f = open(filename, "w")
    f.write(cPickle.dumps(poly))
    f.close()

    filename = "C:/Users/Vaibhav Gupta/Desktop/implementation/gui/modified/HU/" + s + ".txt"
    f = open(filename, "w")
    f.write(cPickle.dumps(poly))
    f.close()

def all_templates():
    os.chdir("C:/Users/Vaibhav Gupta/Desktop/implementation/gui/modified/templates")
    grp = []
    for file in glob.glob("*.JPG"):
        grp.append(file)
    return grp

def file_running_clear():
    global file_running
    file_running = ''

def generate():
    global file_running
    #letters = [chr(i) for i in range(65, 90) if i != 74]
    grp = all_templates()
    #print grp



    #for x in range(10):
    #    letters.append(str(x))
    for l in grp:
        imageName = "C:/Users/Vaibhav Gupta/Desktop/implementation/gui/modified/templates/" + l
        file_running= file_running + '\n' + imageName
        image = cv2.imread(imageName)
        #print image
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        store_contour_and_poly(image, l)

    



