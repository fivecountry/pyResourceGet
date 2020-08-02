# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/flyss/myData/myCode/pythonWorkSpace/pyDownloader/pyResourceGet/uiDefines/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(959, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gbToolBar = QtWidgets.QGroupBox(self.centralwidget)
        self.gbToolBar.setGeometry(QtCore.QRect(10, 10, 940, 70))
        self.gbToolBar.setObjectName("gbToolBar")
        self.btnManage = QtWidgets.QPushButton(self.gbToolBar)
        self.btnManage.setGeometry(QtCore.QRect(480, 30, 61, 30))
        self.btnManage.setObjectName("btnManage")
        self.cbPlugins = QtWidgets.QComboBox(self.gbToolBar)
        self.cbPlugins.setGeometry(QtCore.QRect(10, 30, 371, 27))
        self.cbPlugins.setObjectName("cbPlugins")
        self.btnOpenPlugin = QtWidgets.QPushButton(self.gbToolBar)
        self.btnOpenPlugin.setGeometry(QtCore.QRect(390, 30, 81, 30))
        self.btnOpenPlugin.setObjectName("btnOpenPlugin")
        self.btnStopAll = QtWidgets.QPushButton(self.gbToolBar)
        self.btnStopAll.setGeometry(QtCore.QRect(680, 30, 81, 30))
        self.btnStopAll.setObjectName("btnStopAll")
        self.btnStartAll = QtWidgets.QPushButton(self.gbToolBar)
        self.btnStartAll.setGeometry(QtCore.QRect(770, 30, 81, 30))
        self.btnStartAll.setObjectName("btnStartAll")
        self.btnAboutMe = QtWidgets.QPushButton(self.gbToolBar)
        self.btnAboutMe.setGeometry(QtCore.QRect(860, 30, 71, 27))
        self.btnAboutMe.setObjectName("btnAboutMe")
        self.btnDownloadDir = QtWidgets.QPushButton(self.gbToolBar)
        self.btnDownloadDir.setGeometry(QtCore.QRect(550, 30, 120, 31))
        self.btnDownloadDir.setObjectName("btnDownloadDir")
        self.lwFileList = QtWidgets.QListWidget(self.centralwidget)
        self.lwFileList.setGeometry(QtCore.QRect(10, 90, 941, 381))
        self.lwFileList.setObjectName("lwFileList")
        item = QtWidgets.QListWidgetItem()
        self.lwFileList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwFileList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwFileList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwFileList.addItem(item)
        self.txtLogs = QtWidgets.QTextEdit(self.centralwidget)
        self.txtLogs.setGeometry(QtCore.QRect(10, 480, 941, 81))
        self.txtLogs.setReadOnly(True)
        self.txtLogs.setObjectName("txtLogs")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "资源搜索下载器V1.0 项目地址：https://github.com/fivecountry/pyResourceGet"))
        self.gbToolBar.setTitle(_translate("MainWindow", "控制栏"))
        self.btnManage.setText(_translate("MainWindow", "管理"))
        self.btnOpenPlugin.setText(_translate("MainWindow", "打开插件"))
        self.btnStopAll.setText(_translate("MainWindow", "停止所有"))
        self.btnStartAll.setText(_translate("MainWindow", "启动所有"))
        self.btnAboutMe.setText(_translate("MainWindow", "关于我"))
        self.btnDownloadDir.setText(_translate("MainWindow", "打开下载目录"))
        __sortingEnabled = self.lwFileList.isSortingEnabled()
        self.lwFileList.setSortingEnabled(False)
        item = self.lwFileList.item(0)
        item.setText(_translate("MainWindow", "新建项目"))
        item = self.lwFileList.item(1)
        item.setText(_translate("MainWindow", "新建项目"))
        item = self.lwFileList.item(2)
        item.setText(_translate("MainWindow", "新建项目"))
        item = self.lwFileList.item(3)
        item.setText(_translate("MainWindow", "新建项目"))
        self.lwFileList.setSortingEnabled(__sortingEnabled)

