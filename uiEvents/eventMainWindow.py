#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from uiEvents.AWindowBase import *
from uiDefines.Ui_MainWindow import *
from uiEvents.eventDownloadListItemWidget import *
from uiEvents.eventSpiderWindow import *
from uiEvents.eventSpiderManageWindow import *
from uiUtil.downloadList import *
from uiUtil.globaltool import *
from uiUtil.envs import *
import os
import sys
import pathlib
import datetime
import time

'''
    这是MainWindow窗体的事件实现类
'''
class FMainWindow(IWindowImplM):
    '''
       初始化所有数据(抽象函数)
    '''
    def initUIAndData(self):
        #屏蔽最大化按钮
        self.windowObj.setFixedSize(960, 570)
        #清空下载列表
        self.uiObj.lwFileList.clear()
        #初始化事件
        self.initEvents()
        #启动下载器
        self.dWorker = DownloadWorker()
        self.dWorker.start()
        self.uiObj.btnStartAll.setEnabled(False)
        self.uiObj.btnStopAll.setEnabled(True)
        #创建下载目录
        try:
            os.makedirs(cfenv.configObj['downloadDir'])
        except Exception as ex:
            pass
        #载入下载列表
        self.loadDownloadList()
        #载入插件列表
        self.loadPluginList()

    '''
        初始化事件
    '''
    def initEvents(self):
        self.uiObj.btnManage.clicked.connect(self.btnManageClicked)
        self.uiObj.btnOpenPlugin.clicked.connect(self.btnOpenPluginClicked)
        self.uiObj.btnStopAll.clicked.connect(self.btnStopAllClicked)
        self.uiObj.btnStartAll.clicked.connect(self.btnStartAllClicked)
        self.uiObj.btnAboutMe.clicked.connect(self.btnAboutMeClicked)

    '''
       返回UI定义类的实例(例如uiDefines/Ui_MainWindow.py的实例,抽象函数)
    '''
    def getUIDefineObject(self):
        return Ui_MainWindow()
    
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
        try:
            QApplication.processEvents()
        except Exception as ex:
            print(ex)

    '''
        Invoke实现
    '''
    def runUIImpl(self, uiArgs):
        if uiArgs.command == 'log':
            self.displayLog(uiArgs.content)
        else:
            self.addDownloadTask(uiArgs.content, uiArgs.tag, False)

    '''
        添加下载任务
    '''
    def addDownloadTask(self, url, local, isFinished):
        if url != None and local != None:
            item = FDownloadListItemWidget()
            item.dWorker = self.dWorker
            item.appendToList(self.uiObj.lwFileList)
            taskInfo = DownloadTaskInfo(url,local,item)
            taskInfo.isFinished = isFinished
            item.setText(item.getDisplayText())            
            if (taskInfo.isFinished == False):
                self.dWorker.addTask(taskInfo)

    '''
        载入下载列表
    '''
    def loadDownloadList(self):
        jd = jsondict()
        jd.loadFile(cfenv.configFilePath)
        downloadList = jd.getValue('downloadList',[])
        if downloadList != None:
            for kv in downloadList:
                remoteUrl = kv['url']
                localPath = kv['local']
                isFinished = kv['finished']
                self.addDownloadTask(remoteUrl,localPath,isFinished)

    '''
        载入插件列表
    '''
    def loadPluginList(self):
        if cfenv.configObj.get('plugins') == None:
            pass
        else:
            pluginData = cfenv.configObj['plugins']
            for k, v in pluginData.items():
                self.uiObj.cbPlugins.addItem(v['name'], v)

    '''
        窗体关闭事件
    '''
    def closeEvent(self, e):
        self.dWorker.isRunning = False
        self.saveDownloadList()
        e.accept()

    '''
        管理
    '''
    def btnManageClicked(self, e):
        window, ui, event = WindowBuilder.buildWindow(None, FSpiderManageWindow())
        window.show()

    '''
        打开分析界面
    '''
    def btnOpenPluginClicked(self, e):
        window, ui, event = WindowBuilder.buildWindow(None, FSpiderWindow())
        event.setDownloadList(self)
        event.setPlugin(self.uiObj.cbPlugins.currentData())
        window.show()

    '''
        停止所有
    '''
    def btnStopAllClicked(self, e):
        #关闭线程
        self.tempQueue = self.dWorker.queue
        self.dWorker.isRunning = False
        self.uiObj.btnStartAll.setEnabled(True)
        self.uiObj.btnStopAll.setEnabled(False)
        #保存任务列表
        self.saveDownloadList()

    '''
        保存下载任务列表
    '''
    def saveDownloadList(self):
        try:
            jd = jsondict()
            jd.loadFile(cfenv.configFilePath)
            downloadList = []
            for k in range(0,self.uiObj.lwFileList.count()):
                item = self.uiObj.lwFileList.item(k)
                eventObj = item.data(0)
                kvv = {}
                kvv['url'] = eventObj.taskInfo.sourceUrl
                kvv['local'] = eventObj.taskInfo.localPath
                kvv['finished'] = eventObj.taskInfo.isFinished
                downloadList.append(kvv)
            jd.addOrUpdate('downloadList',downloadList)
            jd.saveFile(cfenv.configFilePath)
        except Exception as ex:
            pass

    '''
        开始所有
    '''
    def btnStartAllClicked(self, e):
        #启动线程
        self.dWorker = DownloadWorker()
        self.dWorker.queue = self.tempQueue
        self.dWorker.start()
        self.uiObj.btnStartAll.setEnabled(False)
        self.uiObj.btnStopAll.setEnabled(True)

    '''
        关于我
    '''
    def btnAboutMeClicked(self, e):
        QMessageBox.information(self, '关于我', '资源搜索下载器 \n 本程序基于Python3.7 + PyQT + Scrapy + Js2py编写！')
