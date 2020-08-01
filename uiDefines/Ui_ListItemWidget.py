# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/flyss/myData/myCode/pythonWorkSpace/pyDownloader/pyResourceGet/uiDefines/ListItemWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ListItemWidget(object):
    def setupUi(self, ListItemWidget):
        ListItemWidget.setObjectName("ListItemWidget")
        ListItemWidget.resize(941, 89)
        self.lblTitle = QtWidgets.QLabel(ListItemWidget)
        self.lblTitle.setGeometry(QtCore.QRect(10, 10, 731, 71))
        self.lblTitle.setTextFormat(QtCore.Qt.AutoText)
        self.lblTitle.setObjectName("lblTitle")
        self.btnDelete = QtWidgets.QPushButton(ListItemWidget)
        self.btnDelete.setGeometry(QtCore.QRect(840, 20, 81, 51))
        self.btnDelete.setObjectName("btnDelete")
        self.btnOpen = QtWidgets.QPushButton(ListItemWidget)
        self.btnOpen.setGeometry(QtCore.QRect(750, 20, 81, 51))
        self.btnOpen.setObjectName("btnOpen")

        self.retranslateUi(ListItemWidget)
        QtCore.QMetaObject.connectSlotsByName(ListItemWidget)

    def retranslateUi(self, ListItemWidget):
        _translate = QtCore.QCoreApplication.translate
        ListItemWidget.setWindowTitle(_translate("ListItemWidget", "Form"))
        self.lblTitle.setText(_translate("ListItemWidget", "1\n"
"2\n"
"3"))
        self.btnDelete.setText(_translate("ListItemWidget", "删除"))
        self.btnOpen.setText(_translate("ListItemWidget", "重新下载"))

