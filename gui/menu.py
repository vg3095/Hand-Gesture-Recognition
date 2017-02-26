# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
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

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName(_fromUtf8("Menu"))
        Menu.resize(234, 258)
        Menu.setMinimumSize(QtCore.QSize(234, 258))
        Menu.setMaximumSize(QtCore.QSize(234, 258))
        self.centralwidget = QtGui.QWidget(Menu)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 30, 81, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 90, 81, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 150, 81, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        Menu.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 234, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Menu.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Menu)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(_translate("Menu", "Menu", None))
        self.pushButton.setText(_translate("Menu", "Start", None))
        self.pushButton_2.setText(_translate("Menu", "Train ", None))
        self.pushButton_3.setText(_translate("Menu", "Settings", None))


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     Menu = QtGui.QMainWindow()
#     ui = Ui_Menu()
#     ui.setupUi(Menu)
#     Menu.show()
#     sys.exit(app.exec_())

