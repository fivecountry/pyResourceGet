#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from uiEvents.AWindowBase import *
from uiDefines.Ui_ListItemWidget import *
from uiUtil.downloadList import *
from uiUtil.globaltool import *
import os
import sys
import pathlib

'''
    这是DownloadListItemWidget的事件实现类
'''
class FDownloadListItemWidget(IWindowImplW, IDownloadReporter):
    '''
       初始化所有数据(抽象函数)
    '''
    def initUIAndData(self):
        self.initEvents()

    '''
        初始化事件
    '''
    def initEvents(self):
        self.uiObj.btnDownloadAgain.clicked.connect(self.btnDownloadAgainClicked)
        self.uiObj.btnDelete.clicked.connect(self.btnDeleteClicked)
        self.uiObj.btnOpenDir.clicked.connect(self.btnOpenDirClicked)
        self.uiObj.btnOpenFile.clicked.connect(self.btnOpenFileClicked)

    '''
       返回UI定义类的实例(例如uiDefines/Ui_MainWindow.py的实例,抽象函数)
    '''
    def getUIDefineObject(self):
        return Ui_ListItemWidget()

    '''
        重新下载按钮
    '''
    def btnDownloadAgainClicked(self, e):
        try:
            if (self.taskInfo != None):
                self.dWorker.addTask(self.taskInfo)
        except Exception as ex:
            pass

    '''
        删除按钮
    '''
    def btnDeleteClicked(self, e):
        if QMessageBox.question(self,'提示','真的要删除吗？',QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            if self.listObj != None:
                self.listObj.takeItem(self.listObj.row(self.itemObj))
            if self.taskInfo != None:
                self.taskInfo.isDeleted = True
                if os.path.exists(self.taskInfo.localPath):
                    try:
                        os.remove(self.taskInfo.localPath)
                    except Exception as ex:
                        pass

    '''
        打开目录
    '''
    def btnOpenDirClicked(self, e):
        try:
            iotool.shellExecute(pathlib.Path(self.taskInfo.localPath).parent)
        except Exception as ex:
            pass

    '''
        打开文件
    '''
    def btnOpenFileClicked(self, e):
        try:
            iotool.shellExecute(self.taskInfo.localPath)
        except Exception as ex:
            pass
    
    '''
        添加项到列表
    '''
    def appendToList(self, listUI):
        self.listObj = listUI
        widgetObj,ui,event = WindowBuilder.buildWindow(None,self)
        widgetObj.setFixedWidth(1025)
        widgetObj.setFixedHeight(89)
        self.itemObj = QListWidgetItem()
        self.itemObj.setSizeHint(QSize(1025,89))
        self.itemObj.setData(0,event)
        self.listObj.addItem(self.itemObj)
        self.listObj.setItemWidget(self.itemObj,widgetObj)

    '''
        设置文本
    '''
    def setText(self, content):
        self.uiObj.lblTitle.setText(content)

    '''
        获得显示文本
    '''    
    def getDisplayText(self):
        if self.taskInfo != None:
            sb = stringbuffer()
            sb.appendLine(self.taskInfo.sourceUrl)
            sb.append('当前进度:')
            try:
                if self.taskInfo.percent != None:
                    sb.append(str(self.taskInfo.percent)).append('%')
            except Exception as ex:
                if self.taskInfo.isFinished == True:
                    sb.append('100%')
                else:
                    sb.append('未知')
            sb.append(' 本地路径:').appendLine(self.taskInfo.localPath)
            try:
                if (self.taskInfo.error != None):
                    sb.appendLine(self.taskInfo.error)
            except Exception as ex:
                pass
            return sb.toString()
        else:
            return '错误！！'

    '''
        刷新数据(在UI线程中执行的)
    '''
    def runUIImpl(self, uiArgs):
        self.setText(self.getDisplayText())

    '''
        报告错误
    '''
    def error(self, txt):
        self.taskInfo.error = txt
        self.invokeUI(QTObjectInvokeArgs(None))
    
    '''
        报告进度
    '''
    def progress(self, percent):
        self.taskInfo.percent = percent
        self.invokeUI(QTObjectInvokeArgs(None))

    '''
        报告完成
    '''
    def finish(self):
        self.taskInfo.isFinished = True
        self.invokeUI(QTObjectInvokeArgs(None))
