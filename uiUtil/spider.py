#-*- coding:utf-8 -*-
import sys
import os
import pathlib
import js2py
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

'''
    使用JS代码实现蜘蛛程序
'''
class jsSpider(scrapy.Spider):
    #Spider名称
    name = 'jsSpider'

    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)
        #初始化解析器名称
        self.currentParseName = 'main'
        #初始化地址
        try:
            self.initStartUrls()
            for url in self.start_urls:
                print('URL:' + url)
        except Exception  as ex:
            print(ex)

    '''
        初始化地址
    '''
    def initStartUrls(self):
        if jsSpider.urlCode != None:
            getUrls = js2py.eval_js(jsSpider.urlCode)
            self.start_urls = getUrls()

    '''
        使用JS代码进行解析
    '''
    def parse(self, response):
        try:
            if jsSpider.resolveCode != None:
                spiderRun = js2py.eval_js(jsSpider.resolveCode)
                nextPageJsons = json.loads(spiderRun(self.currentParseName, response))
                print(nextPageJsons)
                if nextPageJsons.get('type') != None:
                    nextType = nextPageJsons['type']
                    nextParseName = nextPageJsons['parse']
                    nextPageUrls = nextPageJsons['urls']
                    for url in nextPageUrls:
                        if nextType == 'request':
                            self.currentParseName = nextParseName
                            yield scrapy.Request(url, callback=self.parse)
                        elif nextType == 'follow':
                            self.currentParseName = nextParseName
                            yield response.follow(url, callback=self.parse)
        except Exception as ex:
            print(ex)

'''
    蜘蛛工具
'''
class spidertool:
    '''
        创建蜘蛛进程
    '''
    def createSpiderProcess(scriptPluginDir):
        #载入脚本
        jsSpider.urlCode = iotool.readAllText(os.path.join(scriptPluginDir, 'url.js'))
        jsSpider.resolveCode = iotool.readAllText(os.path.join(scriptPluginDir, 'spider.js'))
        print('Url脚本：{0}\n'.format(jsSpider.urlCode))
        print('Spider脚本：{0}\n'.format(jsSpider.resolveCode))

        def spiderStart(q):
            try:
                runner = CrawlerRunner()
                runner.crawl(jsSpider)
                d = runner.join()
                d.addBoth(lambda _: reactor.stop())
                reactor.callFromThread(notThreadSafe, 3)
                reactor.run()
                print('jsSpider已启动!')
            except Exception as e:
                print(e)
        
        #运行蜘蛛程序
        return Process(target=spiderStart, args=(None))

    '''
        使用Xpath方式解析数据
    '''
    def resolveXPath(response, xpathString):
        return response.xpath(xpathString).extract()

    '''
        使用scrapy.Request方式()
    '''
    def requestPage(pName, urls):
        urlTT = []
        for u in urls:
            urlTT.append(u)
        data={'type': 'request', 'parse': pName, 'urls': urlTT}
        return json.dumps(data, indent=4)

    '''
        使用response.follow方式()
    '''
    def followPage(pName, urls):
        urlTT = []
        for u in urls:
            urlTT.append(u)
        data={'type': 'follow', 'parse': pName, 'urls': urlTT}
        return json.dumps(data, indent=4)

    '''
        不需要下一页
    '''
    def noPage():
        data={'type': 'nopage', 'parse': 'none', 'urls': []}
        return json.dumps(data, indent=4)

    '''
        初始化日志接口
    '''
    def initLogger(loggers):
        spidertool.logger = loggers

    '''
        打印日志
    '''
    def printLog(content):
        try:
            if spidertool.logger != None:
                spidertool.logger.printLog(content)
        except Exception as ex:
            print(ex)

    '''
        报告下载地址
    '''
    def reportDownloadUrl(url):
        try:
            if spidertool.logger != None:
                spidertool.logger.reportDownloadUrl(url)
        except Exception as ex:
            print(ex)

    '''
        报告下载完成
    '''
    def reportFinish():
        try:
            if spidertool.logger != None:
                spidertool.logger.reportFinish()
        except Exception as ex:
            print(ex)

'''
    日志接口
'''
class ILogDisplay:
    '''
        显示日志
    '''
    def printLog(self, content):
        raise NotImplementedError

    '''
        报告下载地址
    '''
    def reportDownloadUrl(self, url):
        raise NotImplementedError

    '''
        搜索完成
    '''
    def reportFinish(self):
        raise NotImplementedError
