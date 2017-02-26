# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Start(object):
    def setupUi(self, Start):
        Start.setObjectName(_fromUtf8("Start"))
        Start.resize(1032, 602)
        Start.setMinimumSize(QtCore.QSize(1032, 602))
        Start.setMaximumSize(QtCore.QSize(1032, 602))
        self.centralwidget = QtGui.QWidget(Start)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.videoFrame = QtGui.QLabel(self.centralwidget)
        self.videoFrame.setGeometry(QtCore.QRect(40, 32, 640, 480))
        self.videoFrame.setObjectName(_fromUtf8("videoFrame"))
        self.processed_frame = QtGui.QLabel(self.centralwidget)
        self.processed_frame.setGeometry(QtCore.QRect(800, 330, 200, 200))
        self.processed_frame.setObjectName(_fromUtf8("processed_frame"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(750, 50, 256, 131))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.debug = QtGui.QCheckBox(self.centralwidget)
        self.debug.setGeometry(QtCore.QRect(770, 200, 70, 17))
        self.debug.setObjectName(_fromUtf8("debug"))
        self.clear = QtGui.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(930, 200, 71, 21))
        self.clear.setObjectName(_fromUtf8("clear"))
        self.Convertedlabel = QtGui.QLabel(self.centralwidget)
        self.Convertedlabel.setGeometry(QtCore.QRect(750, 30, 81, 16))
        self.Convertedlabel.setObjectName(_fromUtf8("Convertedlabel"))
        self.processedImageLabel = QtGui.QLabel(self.centralwidget)
        self.processedImageLabel.setGeometry(QtCore.QRect(800, 300, 91, 16))
        self.processedImageLabel.setObjectName(_fromUtf8("processedImageLabel"))
        self.Convertedlabel_3 = QtGui.QLabel(self.centralwidget)
        self.Convertedlabel_3.setGeometry(QtCore.QRect(40, 10, 91, 16))
        self.Convertedlabel_3.setObjectName(_fromUtf8("Convertedlabel_3"))
        Start.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Start)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Start.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Start)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Start.setStatusBar(self.statusbar)

        self.retranslateUi(Start)
        QtCore.QMetaObject.connectSlotsByName(Start)

    def retranslateUi(self, Start):
        Start.setWindowTitle(_translate("Start", "Start", None))
        self.videoFrame.setText(_translate("Start", "TextLabel", None))
        self.processed_frame.setText(_translate("Start", "TextLabel", None))
        self.debug.setText(_translate("Start", "Debug", None))
        self.clear.setText(_translate("Start", "Clear", None))
        self.Convertedlabel.setText(_translate("Start", "Converted Text", None))
        self.processedImageLabel.setText(_translate("Start", "Processed Image", None))
        self.Convertedlabel_3.setText(_translate("Start", "Camera Feed", None))


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     Start = QtGui.QMainWindow()
#     ui = Ui_Start()
#     ui.setupUi(Start)
#     Start.show()
#     sys.exit(app.exec_())

