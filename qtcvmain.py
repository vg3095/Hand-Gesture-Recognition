import sys
import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, Qt
from train import Ui_MainWindow
import video_mod 
import video_mod_2 
import scipy.misc
from menu import Ui_Menu
from start import Ui_Start
from settings import Ui_Settings
import mod_data_create

class MenuScreen(QtGui.QMainWindow, Ui_Menu):
    def __init__(self, parent=None):
        super(MenuScreen, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.handleCaptureButton)
        self.pushButton.clicked.connect(self.handleStartButton)
        self.pushButton_3.clicked.connect(self.handleSettingsButton)
        self.window2 = None
        self.startWindow = None
        self.settingsWindow = None
        #self.converted_text = ''

    def handleCaptureButton(self):
        if self.window2 is None:
            self.window2 = Gui(self)
        self.window2.show()

    def handleStartButton(self):
        if self.startWindow is None:
            self.startWindow = Start(self)
        self.startWindow.show()        

    def handleSettingsButton(self):
        if self.settingsWindow is None:
            self.settingsWindow = Settings(self)
        self.settingsWindow.show() 

class Gui(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.video = video_mod.Video(cv2.VideoCapture(0))

        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)
        self.update()
 
    def play(self):
        try:
            self.video.captureNextFrame()
            img,thresh1 = self.video.convertFrame()
            self.ui.videoFrame.setPixmap(img)
            #print thresh1
            self.ui.processed_frame.setPixmap(thresh1)
            self.ui.videoFrame.setScaledContents(True)
            if self.ui.flag:
                self.ui.flag=0
                saveGesture = self.video.capture_frame_action()
                cv2.imshow("capture",saveGesture)
                fileName = QtGui.QFileDialog.getSaveFileName(self, 'Save Gesture', 'templates/',selectedFilter='*.jpg')
                #print saveGesture
                convert_to_jpg(saveGesture,fileName)
            #self.ui.processed_frame.setScaledContents(True)
        except TypeError:
            print "No frame"


class Start(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Start()
        self.ui.setupUi(self)
        self.video = video_mod_2.Video(cv2.VideoCapture(0))
        self.ui.clear.clicked.connect(self.clear_action)
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)
        self.converted_text = ''
        self.update()
 
    def play(self):
        try:
            self.video.captureNextFrame()
            img,thresh1 = self.video.convertFrame()
            self.ui.videoFrame.setPixmap(img)
            #print thresh1
            self.ui.processed_frame.setPixmap(thresh1)
            self.ui.videoFrame.setScaledContents(True)

            if self.video.flag_text:
                self.video.flag_text=0
                letter = self.video.sent_text_action()
                self.converted_text = self.converted_text+str(letter)
                self.ui.textBrowser.setPlainText(self.converted_text) 
            #self.ui.processed_frame.setScaledContents(True)
        except TypeError:
            print "No frame"

    def clear_action(self):
        self.ui.textBrowser.setPlainText('')
        self.converted_text=''



class Settings(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.ui.ContoursButton.clicked.connect(self.contours_button_action)

    def contours_button_action(self):
        mod_data_create.generate()
        self.ui.LogReport.setPlainText(mod_data_create.file_running)
        mod_data_create.file_running_clear()






def convert_to_jpg(saveGesture,fileName):
    #print saveGesture
    fileName = fileName.replace('/','\\')
    #print fileName
    scipy.misc.toimage(saveGesture).save(str(fileName))

 
def main():
    app = QtGui.QApplication(sys.argv)
    ex = MenuScreen()
    ex.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()