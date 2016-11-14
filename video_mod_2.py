import sys
import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, Qt
from train import Ui_MainWindow
import mod_gui_1
import mod_2 as image_analysis 
import mod_match_HU
class Video():
    def __init__(self,capture):
        self.capture = capture
        self.currentFrame=np.array([])
        self.processedFrame=np.array([])
        self.prev = None
        self.flag_text = 0
 
    def captureNextFrame(self):
        """                           
        capture frame and reverse RBG BGR and return opencv image                                      
        """
        ret, frame=self.capture.read()
        
        if(ret==True):
            frame=cv2.flip(frame,1)
            cv2.rectangle(frame,(300,300),(100,100),(0,255,0),0)
            crop_frame = frame[100:300, 100:300]
            gray = cv2.cvtColor(crop_frame,cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray,15)
            thresh1 = mod_gui_1.threshold_otsu(gray)
            dilation = mod_gui_1.region_filling(thresh1)
            cnt,drawing= image_analysis.contour_operation(crop_frame,dilation)
            if cnt is not None and len(cnt)<=1000:
                letter = mod_match_HU.find_closest_match(cnt)
                if letter is not None and self.prev!=letter:
                    self.prev = letter
                    self.flag_text=1

            self.currentFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            self.processedFrame=dilation
            #print thresh1
 
    def convertFrame(self):
        """     converts frame to format suitable for QtGui            """
        try:
            height,width=self.currentFrame.shape[:2]
            img=QtGui.QImage(self.currentFrame,
                              width,
                              height,
                              QtGui.QImage.Format_RGB888)
            img=QtGui.QPixmap.fromImage(img)
            height,width=self.processedFrame.shape[:2]
            #print height,width
            thresh1=QtGui.QImage(self.processedFrame,
                              width,
                              height,
                              QtGui.QImage.Format_Indexed8)
            thresh1=QtGui.QPixmap.fromImage(thresh1)
            self.previousFrame = self.currentFrame
            self.previousFrame2 = self.processedFrame
            return img,thresh1
        except:
            return None

    def capture_frame_action(self):
        return self.processedFrame

    def sent_text_action(self):
        return self.prev    

