# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
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

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(556, 398)
        self.centralwidget = QtGui.QWidget(Settings)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ContoursButton = QtGui.QPushButton(self.centralwidget)
        self.ContoursButton.setGeometry(QtCore.QRect(210, 50, 91, 21))
        self.ContoursButton.setObjectName(_fromUtf8("ContoursButton"))
        self.LogReport = QtGui.QTextBrowser(self.centralwidget)
        self.LogReport.setGeometry(QtCore.QRect(20, 90, 491, 261))
        self.LogReport.setObjectName(_fromUtf8("LogReport"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        Settings.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Settings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 556, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Settings.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Settings)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Settings.setStatusBar(self.statusbar)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(_translate("Settings", "Settings", None))
        self.ContoursButton.setText(_translate("Settings", "Rebuild Contours", None))
        self.label.setText(_translate("Settings", "Log Report", None))


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     Settings = QtGui.QMainWindow()
#     ui = Ui_Settings()
#     ui.setupUi(Settings)
#     Settings.show()
#     sys.exit(app.exec_())

