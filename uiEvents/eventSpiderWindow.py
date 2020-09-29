#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from uiEvents.AWindowBase import *
from uiDefines.Ui_SpiderWindow import *
from uiEvents.eventSplashWindow import *
from uiUtil.spider import *
import os
import sys
import pathlib
import datetime
import time
from uiUtil.envs import *
from uiUtil.globaltool import *
from w3lib.url import safe_url_string

'''
    这是SpiderWindow窗体的实现类
'''
class FSpiderWindow(IWindowImplM, ILogDisplay):
    '''
       初始化所有数据(抽象函数)
    '''
    def initUIAndData(self):
        self.windowObj.setFixedSize(937,658)
        #初始化事件
        self.initEvents()
        #初始化日志接口
        spidertool.initLogger(self)
        #初始化消息投递器
        self.msgWorker = QTInvokeQueueWorkerWithProcess(self)
        self.msgWorker.start()
        #下载地址列表
        self.downloadList = []        

    '''
        初始化事件
    '''
    def initEvents(self):
        self.uiObj.btnStart.clicked.connect(self.btnStartClicked)
        self.uiObj.btnStop.clicked.connect(self.btnStopClicked)
        self.uiObj.btnDownloadAll.clicked.connect(self.btnDownloadAllClicked)
        self.uiObj.btnClose.clicked.connect(self.btnCloseClicked)

    '''
       返回UI定义类的实例(例如uiDefines/Ui_MainWindow.py的实例,抽象函数)
    '''
    def getUIDefineObject(self):
        return Ui_SpiderWindow()

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
        设置下载列表
    '''
    def setDownloadList(self, mainWindow):
        self.mainWIndow = mainWindow

    '''
        Invoke调用实现
    '''
    def runUIImpl(self, uiArgs):
        try:
            if (uiArgs.command == 'log'):
                self.displayLog(uiArgs.content)
            elif (uiArgs.command == 'download'):
                if isinstance(uiArgs.content, SpiderDownloadItem):
                    self.downloadList.append(uiArgs.content)
                else:
                    for s in uiArgs.content:
                        self.downloadList.append(s)
                self.uiObj.lblStatus.setText('总共找到' + str(len(self.downloadList)) + '个链接!')
            else:
                pass
                #self.btnStopClicked(None)
        except Exception as ex:
            print(ex)

    '''
        显示日志
    '''
    def printLog(self, content):
        self.msgWorker.addMsg(QTCommandInvokeArgs('log', content, None))

    '''
        报告下载地址
    '''
    def reportDownloadUrl(self, objOrList):
        self.msgWorker.addMsg(QTCommandInvokeArgs('download', objOrList, None))

    '''
        报告下载完成
    '''
    def reportFinish(self):
        self.msgWorker.addMsg(QTCommandInvokeArgs('finish', '', None))

    '''
        设置插件信息
    '''
    def setPlugin(self, pluginInfo):
        self.currentPlugin = pluginInfo
        #生成基本目录
        self.downloadTotalDir = cfenv.configObj['downloadDir']
        print('下载总目录：' + self.downloadTotalDir)
        self.downloadCurrentDir = os.path.join(self.downloadTotalDir, self.currentPlugin['dirName'], datetime.datetime.now().strftime("%Y%m%dT%H%M%S"))
        print('本次下载目录：' + self.downloadCurrentDir)
        self.uiObj.lblTitle.setText(self.currentPlugin['readme'] + '\n下载目录：' + self.downloadCurrentDir)
        #设置按钮状态
        self.uiObj.btnStart.setEnabled(True)
        self.uiObj.btnStop.setEnabled(False)
        self.uiObj.btnDownloadAll.setEnabled(False)

    '''
        按钮启动
    '''
    def btnStartClicked(self, e): 
        pluginDir = os.path.join(cfenv.pluginDir, self.currentPlugin['dirName'])
        self.p = spidertool.createSpiderProcess(pluginDir)
        self.p.start()
        self.uiObj.btnStart.setEnabled(False)
        self.uiObj.btnStop.setEnabled(True)
        self.uiObj.btnDownloadAll.setEnabled(False)

    '''
        按钮停止
    '''
    def btnStopClicked(self, e):
        self.p.terminate()
        self.uiObj.btnStart.setEnabled(True)
        self.uiObj.btnStop.setEnabled(False)
        self.uiObj.btnDownloadAll.setEnabled(True)
        self.displayLog('总共找到{0}个可下载的链接！'.format(str(len(self.downloadList))))

    '''
        按钮下载所有
    '''
    def btnDownloadAllClicked(self, e):
        try:
            os.makedirs(self.downloadCurrentDir)
        except Exception as ex:
            pass
        self.uiObj.btnDownloadAll.setEnabled(False)
        FSplashWindow.showWindow("下载所有", SpiderSplashProcess(self.mainWIndow, self, self.downloadList))

    '''
        按钮关闭
    '''
    def btnCloseClicked(self, e):
        self.windowObj.close()

'''
    进度条控制类
'''
class SpiderSplashProcess(ISplashDoWork):
    def __init__(self, mainWIndow, parent, downloadList):
        super().__init__()
        self.mainWIndow = mainWIndow
        self.parentWindow = parent
        self.downloadList = downloadList

    def process(self):
        for k in range(0, len(self.downloadList)):
            try:
                #生成百分数
                percent = int((k / len(self.downloadList)) * 100)
                #取远程URL
                dObj = self.downloadList[k]
                #经过编码的安全Url
                safeUrl = safe_url_string(dObj.remoteUrl, encoding="utf8")
                #生成本地保存位置
                localPath = os.path.join(self.parentWindow.downloadCurrentDir, dObj.destDirName, dObj.destFileName)
                os.makedirs(os.path.join(self.parentWindow.downloadCurrentDir, dObj.destDirName))
                #添加下载
                self.mainWIndow.msgWorker.addMsg(QTCommandInvokeArgs('download', safeUrl, localPath))
                #打印日志
                print('url:{0},local:{1}'.format(dObj.remoteUrl, localPath))
                #显示进度为XX,内容为XX
                self.eventObj.msgWorker.addMsg(SplashInvokeArgs(percent, '正在添加任务:{0}'.format(dObj.remoteUrl)))
                time.sleep(0.05)
            except Exception as ex:
                print(str(ex))
        #关闭窗体
        self.windowObj.close()
        self.parentWindow.windowObj.close()
        iotool.shellExecute(self.parentWindow.downloadCurrentDir + '/')
