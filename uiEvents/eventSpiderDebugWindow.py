#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from uiEvents.AWindowBase import *
from uiDefines.Ui_SpiderDebugWindow import *
import os
import sys
import pathlib
import datetime

'''
    这是SpiderDebugWindow窗体的实现类
'''
class FSpiderDebugWindow(IWindowImplM):
    '''
       初始化所有数据(抽象函数)
    '''
    def initUIAndData(self):
        self.initEvents()
        self.msgWorker = QTInvokeQueueWorkerWithProcess(self)
        self.msgWorker.start()

    '''
        初始化事件
    '''
    def initEvents(self):
        self.uiObj.btnTest.clicked.connect(self.btnTestClicked)

    '''
       返回UI定义类的实例(例如uiDefines/Ui_MainWindow.py的实例,抽象函数)
    '''
    def getUIDefineObject(self):
        return Ui_SpiderDebugWindow()

    '''
        显示日志
    '''
    def displayLog(self, content):
        oldContent =  self.uiObj.txtLogs.toPlainText()
        oldContent = oldContent + datetime.datetime.now().__str__()+ ':' + content + '\n'
        self.uiObj.txtLogs.setText(oldContent)
        cursor = self.uiObj.txtLogs.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.uiObj.txtLogs.setTextCursor(cursor)
        #try:
        #    QApplication.processEvents()
        #except Exception as ex:
        #    print(ex)

    '''
        InvokeUI的实现(用于跨线程操作UI内容)
    '''
    def runUIImpl(self, uiArgs):
        pass

    '''
        按钮测试
    '''
    def btnTestClicked(self, e):
        pass
