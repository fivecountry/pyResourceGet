# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/flyss/myData/myCode/pythonWorkSpace/pyDownloader/pyResourceGet/uiDefines/SpiderWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SpiderWindow(object):
    def setupUi(self, SpiderWindow):
        SpiderWindow.setObjectName("SpiderWindow")
        SpiderWindow.resize(937, 658)
        self.centralwidget = QtWidgets.QWidget(SpiderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 921, 80))
        self.groupBox.setObjectName("groupBox")
        self.lblTitle = QtWidgets.QLabel(self.groupBox)
        self.lblTitle.setGeometry(QtCore.QRect(10, 30, 580, 41))
        self.lblTitle.setObjectName("lblTitle")
        self.btnStart = QtWidgets.QPushButton(self.groupBox)
        self.btnStart.setEnabled(False)
        self.btnStart.setGeometry(QtCore.QRect(600, 30, 70, 41))
        self.btnStart.setObjectName("btnStart")
        self.btnStop = QtWidgets.QPushButton(self.groupBox)
        self.btnStop.setEnabled(False)
        self.btnStop.setGeometry(QtCore.QRect(680, 30, 70, 41))
        self.btnStop.setObjectName("btnStop")
        self.btnDownloadAll = QtWidgets.QPushButton(self.groupBox)
        self.btnDownloadAll.setEnabled(False)
        self.btnDownloadAll.setGeometry(QtCore.QRect(760, 30, 70, 41))
        self.btnDownloadAll.setObjectName("btnDownloadAll")
        self.btnClose = QtWidgets.QPushButton(self.groupBox)
        self.btnClose.setGeometry(QtCore.QRect(840, 30, 70, 41))
        self.btnClose.setObjectName("btnClose")
        self.txtLogs = QtWidgets.QTextEdit(self.centralwidget)
        self.txtLogs.setGeometry(QtCore.QRect(10, 100, 921, 541))
        self.txtLogs.setObjectName("txtLogs")
        SpiderWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SpiderWindow)
        QtCore.QMetaObject.connectSlotsByName(SpiderWindow)

    def retranslateUi(self, SpiderWindow):
        _translate = QtCore.QCoreApplication.translate
        SpiderWindow.setWindowTitle(_translate("SpiderWindow", "数据抓取"))
        self.groupBox.setTitle(_translate("SpiderWindow", "工具栏"))
        self.lblTitle.setText(_translate("SpiderWindow", "......"))
        self.btnStart.setText(_translate("SpiderWindow", "启动"))
        self.btnStop.setText(_translate("SpiderWindow", "停止"))
        self.btnDownloadAll.setText(_translate("SpiderWindow", "下载所有"))
        self.btnClose.setText(_translate("SpiderWindow", "关闭"))

