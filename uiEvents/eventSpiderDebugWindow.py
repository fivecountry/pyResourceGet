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
import twisted
from twisted.internet import *
import scrapy.crawler as crawler
import scrapy
from scrapy.crawler import *
from multiprocessing import *
from scrapy.utils.log import *
from uiUtil.globaltool import *
import json
import scrapy.spiderloader
import scrapy.statscollectors
import scrapy.logformatter
import scrapy.dupefilters
import scrapy.squeues
import scrapy.extensions.spiderstate
import scrapy.extensions.corestats
import scrapy.extensions.telnet
import scrapy.extensions.logstats
import scrapy.extensions.memusage
import scrapy.extensions.memdebug
import scrapy.extensions.feedexport
import scrapy.extensions.closespider
import scrapy.extensions.debug
import scrapy.extensions.httpcache
import scrapy.extensions.statsmailer
import scrapy.extensions.throttle
import scrapy.core.scheduler
import scrapy.core.engine
import scrapy.core.scraper
import scrapy.core.spidermw
import scrapy.core.downloader
import scrapy.downloadermiddlewares.stats
import scrapy.downloadermiddlewares.httpcache
import scrapy.downloadermiddlewares.cookies
import scrapy.downloadermiddlewares.useragent
import scrapy.downloadermiddlewares.httpproxy
import scrapy.downloadermiddlewares.ajaxcrawl
import scrapy.downloadermiddlewares.decompression
import scrapy.downloadermiddlewares.defaultheaders
import scrapy.downloadermiddlewares.downloadtimeout
import scrapy.downloadermiddlewares.httpauth
import scrapy.downloadermiddlewares.httpcompression
import scrapy.downloadermiddlewares.redirect
import scrapy.downloadermiddlewares.retry
import scrapy.downloadermiddlewares.robotstxt
import scrapy.spidermiddlewares.depth
import scrapy.spidermiddlewares.httperror
import scrapy.spidermiddlewares.offsite
import scrapy.spidermiddlewares.referer
import scrapy.spidermiddlewares.urllength
import scrapy.pipelines
import scrapy.core.downloader.handlers.http
import scrapy.core.downloader.contextfactory
import twisted
import twisted.internet
import scrapy.crawler

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
        self.uiObj.btnTest.setEnabled(True)
        self.displayLog(uiArgs.content)

    '''
        按钮测试
    '''
    def btnTestClicked(self, e):
        TestSpider.windowObj = self
        TestSpider.rootUrl = self.uiObj.txtUrl.text()
        TestSpider.xpathText = self.uiObj.txtXPathText.toPlainText()
        self.uiObj.btnTest.setEnabled(False)
        def spiderStart():
            try:
                process = CrawlerProcess()
                process.crawl(TestSpider)
                process.start()
                print('testSpider已启动!')
            except Exception as e:
                print(e)
        
        #运行蜘蛛程序
        p = Process(target=spiderStart)
        p.start()

class TestSpider(scrapy.Spider):
    #Spider名称
    name = 'testSpider'

    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)
        #初始化地址
        try:
            self.start_urls = []
            self.start_urls.append(FSpiderDebugWindow.rootUrl)
            if len(self.start_urls) >= 1:
                print('URL:' + self.start_urls[0])
        except Exception  as ex:
            print(ex)

    '''
        XPath解析
    '''
    def parse(self, response):
        try:
            result = response.xpath(FSpiderDebugWindow.xpathText).extract()
            for s in result:
                TestSpider.windowObj.msgWorker.addMsg(QTCommandInvokeArgs(None, s, None))
        except Exception as ex:
            print(ex)
