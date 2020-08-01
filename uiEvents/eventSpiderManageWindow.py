#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from uiEvents.AWindowBase import *
from uiDefines.Ui_SpiderManage import *
from uiEvents.eventSpiderListItemWidget import *
from uiUtil.envs import *
from uiUtil.globaltool import *
import os
import sys
import pathlib
import datetime

'''
    这是SpiderManageWindow窗体的实现类
'''
class FSpiderManageWindow(IWindowImplM):
    '''
       初始化所有数据(抽象函数)
    '''
    def initUIAndData(self):
        self.initEvents()
        self.initPluginData()
        self.clearData()
        self.msgWorker = QTInvokeQueueWorker(self)
        self.msgWorker.start()

    '''
        初始化事件
    '''
    def initEvents(self):
        self.uiObj.btnNew.clicked.connect(self.btnNewClicked)
        self.uiObj.btnDelete.clicked.connect(self.btnDeleteClicked)
        self.uiObj.btnSave.clicked.connect(self.btnSaveClicked)
        self.uiObj.lvPluginList.itemClicked.connect(self.lvPluginListItemClicked)
        self.uiObj.lvPluginList.itemChanged.connect(self.lvPluginListItemClicked)

    '''
        初始化插件数据
    '''
    def initPluginData(self):
        self.uiObj.lvPluginList.clear()
        if cfenv.configObj.get('plugins') == None:
            pass
        else:
            pluginData = cfenv.configObj['plugins']
            for k, v in pluginData.items():
                lw2 = FSpiderListItemWidget()
                lw2.appendToList(self.uiObj.lvPluginList)
                lw2.setText(v['name'])
                lw2.userData = v

    '''
       返回UI定义类的实例(例如uiDefines/Ui_MainWindow.py的实例,抽象函数)
    '''
    def getUIDefineObject(self):
        return Ui_SpiderManage()

    '''
        InvokeUI的实现(用于跨线程操作UI内容)
    '''
    def runUIImpl(self, uiArgs):
        pass

    '''
        清空编辑框
    '''
    def clearData(self):
        self.currentItem = {}
        self.uiObj.txtPluginName.setText('')
        self.uiObj.txtDirName.setText('')
        self.uiObj.txtReadme.setText('')

    '''
        列表点击
    '''
    def lvPluginListItemClicked(self, item):
        eventObj = item.data(0)
        self.currentItem =  eventObj.userData
        self.uiObj.txtPluginName.setText(self.currentItem['name'])
        self.uiObj.txtDirName.setText(self.currentItem['dirName'])
        self.uiObj.txtReadme.setText(self.currentItem['readme'])

    '''
        按钮新增
    '''
    def btnNewClicked(self, e):
        self.clearData()

    '''
        按钮删除
    '''
    def btnDeleteClicked(self, e):
        if QMessageBox.question(self, '提示', '真的要删除吗？', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            cfenv.configObj['plugins'].pop(self.currentItem['dirName'])
            self.initPluginData()
            self.clearData()

    '''
        按钮保存
    '''
    def btnSaveClicked(self, e):
        #设置数据
        if len(self.currentItem) == 0:
            self.currentItem['name'] = self.uiObj.txtPluginName.toPlainText().strip()
            self.currentItem['dirName'] = self.uiObj.txtDirName.toPlainText().strip()
            self.currentItem['readme'] = self.uiObj.txtReadme.toPlainText().strip()
        else:
            cfenv.configObj['plugins'].pop(self.currentItem['dirName'])
            self.currentItem['name'] = self.uiObj.txtPluginName.toPlainText().strip()
            self.currentItem['dirName'] = self.uiObj.txtDirName.toPlainText().strip()
            self.currentItem['readme'] = self.uiObj.txtReadme.toPlainText().strip()
        #保存数据
        cfenv.configObj['plugins'][self.currentItem['dirName']] = self.currentItem
        cfenv.saveConfig()
        self.initPluginData()
