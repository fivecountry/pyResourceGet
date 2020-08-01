#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from uiEvents.AWindowBase import *
from uiDefines.Ui_ListItemWidget2 import *
import os
import sys
import pathlib
import datetime

'''
    这是SpiderListItemWidget窗体的实现类
'''
class FSpiderListItemWidget(IWindowImplW):
    '''
       初始化所有数据(抽象函数)
    '''
    def initUIAndData(self):
        self.initEvents()

    '''
        初始化事件
    '''
    def initEvents(self):
        pass

    '''
       返回UI定义类的实例(例如uiDefines/Ui_MainWindow.py的实例,抽象函数)
    '''
    def getUIDefineObject(self):
        return Ui_ListItemWidget2()

    '''
        InvokeUI的实现(用于跨线程操作UI内容)
    '''
    def runUIImpl(self, uiArgs):
        pass

    '''
        添加项到列表
    '''
    def appendToList(self, listUI):
        self.listObj = listUI
        widgetObj,ui,event = WindowBuilder.buildWindow(None,self)
        widgetObj.setFixedWidth(278)
        widgetObj.setFixedHeight(35)
        self.itemObj = QListWidgetItem()
        self.itemObj.setSizeHint(QSize(278, 35))
        self.itemObj.setData(0,event)
        self.listObj.addItem(self.itemObj)
        self.listObj.setItemWidget(self.itemObj,widgetObj)

    '''
        设置文本
    '''
    def setText(self, content):
        self.uiObj.lblContent.setText(content)
