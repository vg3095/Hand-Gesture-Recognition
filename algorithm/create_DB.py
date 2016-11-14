import cv2 as opencv
import cPickle
import numpy as np
import glob
import os
import contours_op

file_running = ''

def current_path():
    path = str(os.getcwd())
    path = path.replace('\\','/')
    return path

def store_contour_and_poly(img, s):
    thresh = img
    contours, hierarchy = opencv.findContours(thresh,opencv.RETR_TREE,opencv.CHAIN_APPROX_SIMPLE)
    s =s.replace('.JPG','')
    s =s.replace('.jpg','')
    pos = contours_op.find_largest_contour(contours)
    cnt = contours[pos]
    path = current_path()+ "/database_contour/"
    filename = path + s + ".txt"
    f = open(filename, "w")
    f.write(cPickle.dumps(cnt))
    f.close()

def all_templates():
    path_old = current_path() 
    path = current_path()+ "/templates/"
    #os.chdir(path)
    grp = []
    for file in glob.glob(path+"*.jpg"):
        t=file
        t = t.replace(path_old,'')
        t=t.replace('/templates','')
        t=t.replace('\\','')
        grp.append(t)
    return grp

def file_running_clear():
    global file_running
    file_running = ''

def generate():
    global file_running
    path = current_path()+ "/templates/"
    grp = all_templates()
    for l in grp:
        imageName = path + l
        file_running= file_running + '\n' + imageName
        image = opencv.imread(imageName)
        image = opencv.cvtColor(image,opencv.COLOR_BGR2GRAY)
        store_contour_and_poly(image, l)

    



