# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/flyss/myData/myCode/pythonWorkSpace/pyDownloader/pyResourceGet/uiDefines/SpiderManage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SpiderManage(object):
    def setupUi(self, SpiderManage):
        SpiderManage.setObjectName("SpiderManage")
        SpiderManage.resize(812, 499)
        self.centralwidget = QtWidgets.QWidget(SpiderManage)
        self.centralwidget.setObjectName("centralwidget")
        self.lvPluginList = QtWidgets.QListWidget(self.centralwidget)
        self.lvPluginList.setGeometry(QtCore.QRect(10, 20, 281, 421))
        self.lvPluginList.setObjectName("lvPluginList")
        item = QtWidgets.QListWidgetItem()
        self.lvPluginList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lvPluginList.addItem(item)
        self.btnNew = QtWidgets.QPushButton(self.centralwidget)
        self.btnNew.setGeometry(QtCore.QRect(10, 450, 98, 40))
        self.btnNew.setObjectName("btnNew")
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(190, 450, 98, 40))
        self.btnDelete.setObjectName("btnDelete")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(300, 20, 501, 421))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 81, 30))
        self.label.setObjectName("label")
        self.txtPluginName = QtWidgets.QTextEdit(self.groupBox)
        self.txtPluginName.setGeometry(QtCore.QRect(110, 40, 381, 31))
        self.txtPluginName.setObjectName("txtPluginName")
        self.txtDirName = QtWidgets.QTextEdit(self.groupBox)
        self.txtDirName.setGeometry(QtCore.QRect(110, 80, 381, 31))
        self.txtDirName.setObjectName("txtDirName")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 81, 30))
        self.label_2.setObjectName("label_2")
        self.txtReadme = QtWidgets.QTextEdit(self.groupBox)
        self.txtReadme.setGeometry(QtCore.QRect(110, 120, 381, 240))
        self.txtReadme.setObjectName("txtReadme")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 81, 30))
        self.label_3.setObjectName("label_3")
        self.btnSave = QtWidgets.QPushButton(self.groupBox)
        self.btnSave.setGeometry(QtCore.QRect(390, 370, 98, 40))
        self.btnSave.setObjectName("btnSave")
        SpiderManage.setCentralWidget(self.centralwidget)

        self.retranslateUi(SpiderManage)
        QtCore.QMetaObject.connectSlotsByName(SpiderManage)

    def retranslateUi(self, SpiderManage):
        _translate = QtCore.QCoreApplication.translate
        SpiderManage.setWindowTitle(_translate("SpiderManage", "插件管理"))
        __sortingEnabled = self.lvPluginList.isSortingEnabled()
        self.lvPluginList.setSortingEnabled(False)
        item = self.lvPluginList.item(0)
        item.setText(_translate("SpiderManage", "新建项目"))
        item = self.lvPluginList.item(1)
        item.setText(_translate("SpiderManage", "新建项目"))
        self.lvPluginList.setSortingEnabled(__sortingEnabled)
        self.btnNew.setText(_translate("SpiderManage", "新增"))
        self.btnDelete.setText(_translate("SpiderManage", "删除"))
        self.groupBox.setTitle(_translate("SpiderManage", "编辑区"))
        self.label.setText(_translate("SpiderManage", "插件名称："))
        self.txtPluginName.setHtml(_translate("SpiderManage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'文泉驿等宽微米黑\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">空</p></body></html>"))
        self.txtDirName.setHtml(_translate("SpiderManage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'文泉驿等宽微米黑\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">空</p></body></html>"))
        self.label_2.setText(_translate("SpiderManage", "目录名称："))
        self.txtReadme.setHtml(_translate("SpiderManage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'文泉驿等宽微米黑\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">空</p></body></html>"))
        self.label_3.setText(_translate("SpiderManage", "插件说明："))
        self.btnSave.setText(_translate("SpiderManage", "保存"))

