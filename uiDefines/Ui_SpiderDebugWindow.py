# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/flywcs/myData/myCode/pythonApp-workspace/pyResourceGet/uiDefines/SpiderDebugWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SpiderDebugWindow(object):
    def setupUi(self, SpiderDebugWindow):
        SpiderDebugWindow.setObjectName("SpiderDebugWindow")
        SpiderDebugWindow.resize(893, 600)
        self.centralwidget = QtWidgets.QWidget(SpiderDebugWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 871, 151))
        self.groupBox.setObjectName("groupBox")
        self.txtUrl = QtWidgets.QLineEdit(self.groupBox)
        self.txtUrl.setGeometry(QtCore.QRect(10, 30, 851, 27))
        self.txtUrl.setObjectName("txtUrl")
        self.btnXPathText = QtWidgets.QTextEdit(self.groupBox)
        self.btnXPathText.setGeometry(QtCore.QRect(10, 60, 771, 81))
        self.btnXPathText.setObjectName("btnXPathText")
        self.btnTest = QtWidgets.QPushButton(self.groupBox)
        self.btnTest.setGeometry(QtCore.QRect(790, 60, 71, 81))
        self.btnTest.setObjectName("btnTest")
        self.txtLogs = QtWidgets.QTextEdit(self.centralwidget)
        self.txtLogs.setGeometry(QtCore.QRect(10, 170, 871, 411))
        self.txtLogs.setReadOnly(True)
        self.txtLogs.setObjectName("txtLogs")
        SpiderDebugWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SpiderDebugWindow)
        QtCore.QMetaObject.connectSlotsByName(SpiderDebugWindow)

    def retranslateUi(self, SpiderDebugWindow):
        _translate = QtCore.QCoreApplication.translate
        SpiderDebugWindow.setWindowTitle(_translate("SpiderDebugWindow", "XPath测试"))
        self.groupBox.setTitle(_translate("SpiderDebugWindow", "工具栏"))
        self.txtUrl.setText(_translate("SpiderDebugWindow", "http://***"))
        self.btnXPathText.setHtml(_translate("SpiderDebugWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'文泉驿等宽微米黑\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">//div[contains(@name,&quot;&quot;]***************</p></body></html>"))
        self.btnTest.setText(_translate("SpiderDebugWindow", "测试"))
