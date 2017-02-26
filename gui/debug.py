# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debug.ui'
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

class Ui_Debug(object):
    def setupUi(self, Debug):
        Debug.setObjectName(_fromUtf8("Debug"))
        Debug.resize(614, 307)
        Debug.setMinimumSize(QtCore.QSize(614, 307))
        Debug.setMaximumSize(QtCore.QSize(614, 307))
        self.centralwidget = QtGui.QWidget(Debug)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.CannyEdgeLabel = QtGui.QLabel(self.centralwidget)
        self.CannyEdgeLabel.setGeometry(QtCore.QRect(20, 50, 200, 200))
        self.CannyEdgeLabel.setObjectName(_fromUtf8("CannyEdgeLabel"))
        self.ConvexityLabel = QtGui.QLabel(self.centralwidget)
        self.ConvexityLabel.setGeometry(QtCore.QRect(340, 50, 200, 200))
        self.ConvexityLabel.setObjectName(_fromUtf8("ConvexityLabel"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 10, 151, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        Debug.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Debug)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Debug.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Debug)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Debug.setStatusBar(self.statusbar)

        self.retranslateUi(Debug)
        QtCore.QMetaObject.connectSlotsByName(Debug)

    def retranslateUi(self, Debug):
        Debug.setWindowTitle(_translate("Debug", "Debug", None))
        self.CannyEdgeLabel.setText(_translate("Debug", "TextLabel", None))
        self.ConvexityLabel.setText(_translate("Debug", "TextLabel", None))
        self.label.setText(_translate("Debug", "Canny Edge Detection", None))
        self.label_3.setText(_translate("Debug", "Contours & Convexity Defects", None))


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     Debug = QtGui.QMainWindow()
#     ui = Ui_Debug()
#     ui.setupUi(Debug)
#     Debug.show()
#     sys.exit(app.exec_())

