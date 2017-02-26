import cv2 as opencv
import numpy as np 
import image_analysis
import cPickle
import contours_op
import glob
import os

cont_param = 0.03

def calculate_contours(img):
	contours, hierarchy = opencv.findContours(img,opencv.RETR_TREE,opencv.CHAIN_APPROX_SIMPLE)
	pos = contours_op.find_largest_contour(contours)
	cnt = contours[pos]
	return cnt


def all_templates():
	path_old = current_path() 
	path = current_path()+"/templates/"
	#os.chdir(path)
	grp = []
	for file in glob.glob(path+"*.jpg"):
		t=file
		t = t.replace(path_old,'')
		t=t.replace('/templates','')
		t=t.replace('\\','')
		#print t
		grp.append(t)
	#os.chdir(path_old)
	#print path_old	
	return grp


def check(l):
	imageName = "test/" + str(l) + ".JPG"
	image = opencv.imread(imageName)
	image=contours_op.operations(image)
	cnt = calculate_contours(image)
	return cnt


def find_closest_match(cnt):
	grp =all_templates()
	path = current_path() + "/database_contour/"
	minimum =1000
	l = None
	for letter in grp:
		s = letter.replace('.JPG','')
		s = s.replace('.jpg','')
		cnt1 = cPickle.loads(open(path+ s+".txt").read())
		temp = opencv.matchShapes(cnt, cnt1, 1, 0.0)
		#print letter,temp
		if temp < minimum:
		    minimum = temp
		    l = letter
	print l,minimum
	global cont_param    
	if l is not None and minimum<cont_param:
		#print l,minimum
		#print cont_param
		l = l[0]
		#print l
		return l

def current_path():
	path = str(os.getcwd())
	path = path.replace('\\','/')
	return path

