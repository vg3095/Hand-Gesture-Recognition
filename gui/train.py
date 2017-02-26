# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trainWindow.ui'
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

class Ui_Train(object):
    def setupUi(self, Train):
        Train.setObjectName(_fromUtf8("Train"))
        Train.resize(1032, 602)
        Train.setMinimumSize(QtCore.QSize(1032, 602))
        Train.setMaximumSize(QtCore.QSize(1032, 602))
        self.centralwidget = QtGui.QWidget(Train)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.videoFrame = QtGui.QLabel(self.centralwidget)
        self.videoFrame.setGeometry(QtCore.QRect(40, 32, 640, 480))
        self.videoFrame.setObjectName(_fromUtf8("videoFrame"))
        self.processed_frame = QtGui.QLabel(self.centralwidget)
        self.processed_frame.setGeometry(QtCore.QRect(800, 330, 200, 200))
        self.processed_frame.setObjectName(_fromUtf8("processed_frame"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(850, 70, 81, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        Train.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Train)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Train.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Train)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Train.setStatusBar(self.statusbar)
        self.flag=0

        self.retranslateUi(Train)
        QtCore.QMetaObject.connectSlotsByName(Train)

    def retranslateUi(self, Train):
        Train.setWindowTitle(_translate("Train", "Train", None))
        self.videoFrame.setText(_translate("Train", "TextLabel", None))
        self.processed_frame.setText(_translate("Train", "TextLabel", None))
        self.pushButton.setText(_translate("Train", "Capture", None))


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     Train = QtGui.QTrain()
#     ui = Ui_Train()
#     ui.setupUi(Train)
#     Train.show()
#     sys.exit(app.exec_())

