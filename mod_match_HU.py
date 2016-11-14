import cv2
import numpy as np 
import mod_2 as image_analysis
from matplotlib import pyplot as plt
import cPickle
import mod_ml_1
from skimage.measure import structural_similarity as ssim
import glob
import os

def calculate_contours(img):
	contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	pos = mod_ml_1.find_largest_contour(contours)
	cnt = contours[pos]
	return cnt


def all_templates():
	os.chdir("C:/Users/Vaibhav Gupta/Desktop/implementation/gui/modified/templates")
	grp = []
	for file in glob.glob("*.JPG"):
		grp.append(file)
	return grp


def check(l):
	imageName = "test/" + str(l) + ".JPG"
	image = cv2.imread(imageName)
	image=mod_ml_1.operations(image)
	cnt = calculate_contours(image)
	return cnt
	#HU_Moments = cv2.HuMoments(cv2.moments(image)).flatten()
	#print HU_Moments

def find_closest_match(cnt):
	#grp = ["1","2","3","4","5"]
	grp =all_templates()
	minimum =1000
	for letter in grp:
		s = letter.replace('.JPG','')
		s = s.replace('.jpg','')
		cnt1 = cPickle.loads(open("C:/Users/Vaibhav Gupta/Desktop/implementation/gui/modified/database_contour/" + s+".txt").read())
		temp = cv2.matchShapes(cnt, cnt1, 1, 0.0)
		#print letter,temp
		if temp < minimum:
		    minimum = temp
		    l = letter
	#print minimum
	#print l
	if l and minimum<0.15:
		l = l[0]
	else:
		l= None
		
	return l

def find_closest_match_image():
	#grp = ["1","2","3","4","5"]
	img2 = cv2.imread('test/4.JPG')
	img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	grp =["1","2","3","4"]
	minimum =1000
	for letter in grp:
	    #cnt1 = cPickle.loads(open("database_contour/" + letter+".txt").read())
	    imageName = "templates/" + letter + ".JPG"
	    img1 = cv2.imread(imageName)
	    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	    temp = cv2.matchShapes(img1, img2, 1, 0.0)
	    print temp
	    if temp < minimum:
	        minimum = temp
	        l = letter
	#print minimum
	print l
	return l

def find_closest_match_image_2(img2):
	#grp = ["1","2","3","4","5"]
	grp =["1","2","3","4"]
	minimum =1000
	for letter in grp:
	    #cnt1 = cPickle.loads(open("database_contour/" + letter+".txt").read())
	    imageName = "templates/" + letter + ".JPG"
	    img1 = cv2.imread(imageName)
	    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	    temp = cv2.matchShapes(img1, img2, 2, 0.0)
	    print temp
	    if temp < minimum:
	        minimum = temp
	        l = letter
	#print minimum
	print l
	return l




def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err



def compare_images(imageA, imageB):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	#s = ssim(imageA, imageB)
 	return m

def find_closest_match_image_2(img2):
	grp =["1","2","3","4"]
	minimum =10000000
	for letter in grp:
	    #cnt1 = cPickle.loads(open("database_contour/" + letter+".txt").read())
	    imageName = "templates/" + letter + ".JPG"
	    img1 = cv2.imread(imageName)
	    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	    img1 = cv2.resize(img1, (200,200))
	    img2 = cv2.resize(img2, (200,200))
	    #print img2.shape
	    #print img1.shape 
	    temp = compare_images(img1, img2)
	    #print temp
	    if temp < minimum:
	        minimum = temp
	        l = letter
	#print minimum
	print l
	return l




def test():
	cnt = check('5_2')
	find_closest_match(cnt)

#test()



#test()
#find_closest_match_image_2()
