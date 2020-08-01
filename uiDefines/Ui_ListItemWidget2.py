# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/flyss/myData/myCode/pythonWorkSpace/pyDownloader/pyResourceGet/uiDefines/ListItemWidget2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ListItemWidget2(object):
    def setupUi(self, ListItemWidget2):
        ListItemWidget2.setObjectName("ListItemWidget2")
        ListItemWidget2.resize(281, 35)
        self.lblContent = QtWidgets.QLabel(ListItemWidget2)
        self.lblContent.setGeometry(QtCore.QRect(10, 10, 260, 20))
        self.lblContent.setObjectName("lblContent")

        self.retranslateUi(ListItemWidget2)
        QtCore.QMetaObject.connectSlotsByName(ListItemWidget2)

    def retranslateUi(self, ListItemWidget2):
        _translate = QtCore.QCoreApplication.translate
        ListItemWidget2.setWindowTitle(_translate("ListItemWidget2", "Form"))
        self.lblContent.setText(_translate("ListItemWidget2", "XXX"))

