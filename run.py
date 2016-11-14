import sys
import cv2 as opencv
import numpy as np
from PyQt4 import QtGui, QtCore, Qt
from gui.train import Ui_MainWindow
import process_video 
import scipy.misc
from gui.menu import Ui_Menu
from gui.start import Ui_Start
from gui.settings import Ui_Settings
import algorithm.create_DB as create_DB

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
        self.video = process_video.Video(opencv.VideoCapture(0),0)
        self.ui.pushButton.clicked.connect(self.capture_action)
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)
        self.update()

    def capture_action(self):
        self.ui.flag=1    
 
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
                opencv.imshow("capture",saveGesture)
                fileName = QtGui.QFileDialog.getSaveFileName(self, 'Save Gesture', 'templates',selectedFilter='*.jpg')
                convert_to_jpg(saveGesture,fileName)
        except TypeError:
            print "No frame"


class Start(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Start()
        self.ui.setupUi(self)
        self.video = process_video.Video(opencv.VideoCapture(0),1)
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
        create_DB.generate()
        self.ui.LogReport.setPlainText(create_DB.file_running)
        create_DB.file_running_clear()



def convert_to_jpg(saveGesture,fileName):
    fileName = fileName.replace('/','\\')
    scipy.misc.toimage(saveGesture).save(str(fileName))

 
def main():
    app = QtGui.QApplication(sys.argv)
    ex = MenuScreen()
    ex.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()