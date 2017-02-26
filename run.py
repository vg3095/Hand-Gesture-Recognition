import sys
import cv2 as opencv
import numpy as np
from PyQt4 import QtGui, QtCore, Qt
from gui.train import Ui_Train
import process_video 
import scipy.misc
from gui.menu import Ui_Menu
from gui.start import Ui_Start
from gui.settings import Ui_Settings
from gui.debug import Ui_Debug
from gui.calibration import Ui_Calibration
import algorithm.create_DB as create_DB
import algorithm.match_DB as match_DB
import algorithm.debugMode as debugMode

frame_t = None
frame_c = None
check_box = None
# len_cont_par = 800
# sim_par = 0.025
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
        #if self.window2 is None:
        self.window2 = Gui(self)
        self.window2.show()

    def handleStartButton(self):
        #if self.startWindow is None:
        self.startWindow = Start(self)
        self.startWindow.show()        

    def handleSettingsButton(self):
        if self.settingsWindow is None:
            self.settingsWindow = Settings(self)
        self.settingsWindow.show() 

class Gui(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Train()
        self.ui.setupUi(self)
        self.feed = opencv.VideoCapture(0)
        self.video = process_video.Video(self.feed,0)
        self.ui.pushButton.clicked.connect(self.capture_action)
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)
        self.update()


    def closeEvent(self, evnt):
        self.feed.release()

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
                if fileName:
                    convert_to_jpg(saveGesture,fileName)
                opencv.destroyAllWindows()
        except TypeError:
            print "No frame"


class Debug(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Debug()
        self.ui.setupUi(self)
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(0)
        self.update()


    def play(self):
        try:
            global frame_t,frame_c
            cannyFrame = debugMode.captureNextFrame(frame_t,1)
            contoursFrame = debugMode.captureNextFrame(frame_t,2,frame_c)
            #self.video.convertFrame()
            if cannyFrame is not None:
                self.ui.CannyEdgeLabel.setPixmap(cannyFrame)
            if contoursFrame is not None:
                self.ui.ConvexityLabel.setPixmap(contoursFrame)    
            #self.ui.ConvexityLabel.setPixmap(contoursFrame)
            

        except TypeError:
            print "No frame"

    def closeEvent(self, evnt):
        global check_box
        check_box.setChecked(False)





class Start(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Start()
        self.ui.setupUi(self)
        self.thresh = None
        self.debugWindow = None
        global check_box
        check_box = self.ui.debug
        self.feed = opencv.VideoCapture(0)
        self.video = process_video.Video(self.feed,1)
        self.ui.clear.clicked.connect(self.clear_action)
        self.ui.debug.setChecked(False)
        self.ui.debug.stateChanged.connect(self.handleDebugButton)
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)
        self.debugState = False
        self.converted_text = ''
        self.update()

    def closeEvent(self, evnt):
        self.feed.release()
 
    def play(self):
        try:
            global frame_t,frame_c
            self.video.captureNextFrame()
            img,thresh1 = self.video.convertFrame()
            self.ui.videoFrame.setPixmap(img)
            #print thresh1
            self.thresh = self.video.threshold
            frame_t = self.thresh
            frame_c = self.video.frame_c
            self.ui.processed_frame.setPixmap(thresh1)
            self.ui.videoFrame.setScaledContents(True)

            if self.video.flag_text==1:
                self.video.flag_text=0
                letter = self.video.sent_text_action()
                if letter is not None:
                    self.converted_text = self.converted_text+str(letter)
                    #print letter
                    self.ui.textBrowser.setPlainText(self.converted_text) 
        except TypeError:
            print "No frame"

    def clear_action(self):
        self.ui.textBrowser.setPlainText('')
        self.converted_text=''

    def handleDebugButton(self):
        
        if self.debugWindow is None and self.ui.debug.isChecked()==True:
            self.debugState = True
            self.debugWindow = Debug(self)
            self.debugWindow.show()
        self.debugWindow = None

        
       



class Calibration(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Calibration()
        self.ui.setupUi(self)
        self.ui.doubleSpinBox.setMinimum(0.001)
        self.ui.doubleSpinBox.setValue(match_DB.cont_param)
        self.ui.doubleSpinBox.setDecimals(3)
        #self.ui.doubleSpinBox.singleStep(0.01)
        self.ui.doubleSpinBox.setMaximum(1)
        self.ui.spinBox.setMinimum(100)
        self.ui.spinBox.setMaximum(2000)
        self.ui.spinBox.setValue(process_video.cnt_param)
        self.ui.doubleSpinBox.valueChanged.connect(self.button_action)
        self.ui.spinBox.valueChanged.connect(self.button_action)

    def button_action(self):
        #global len_cont_par,sim_par
        process_video.cnt_param = self.ui.spinBox.value()
        match_DB.cont_param = self.ui.doubleSpinBox.value()








class Settings(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.calibrationWindow = None
        self.ui.ContoursButton.clicked.connect(self.contours_button_action)
        self.ui.ContoursButton_2.clicked.connect(self.calibration_action)

    def contours_button_action(self):
        create_DB.generate()
        self.ui.LogReport.setPlainText(create_DB.file_running)
        create_DB.file_running_clear()

    def calibration_action(self):
        if self.calibrationWindow is None:
            self.calibrationWindow = Calibration(self)
        self.calibrationWindow.show() 
        



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