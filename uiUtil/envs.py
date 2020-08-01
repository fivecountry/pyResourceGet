#-*- coding:utf-8 -*-
import sys
import os
import pathlib
import json
import base64
import subprocess
import shutil
import io
from uiUtil.globaltool import *

'''
   环境变量
'''
class cfenv(object):
    '''
        初始化配置及环境变量
    '''
    def initEnvData():
        #初始化配置对象
        cfenv.configObj = {}
        #初始化基础目录结构
        cfenv.rootDir = pathlib.Path(os.getcwd()).parent
        cfenv.binDir = os.path.join(cfenv.rootDir,'bin')
        cfenv.dataDir = os.path.join(cfenv.rootDir,'data')
        cfenv.pluginDir = os.path.join(cfenv.dataDir,'plugins')
        cfenv.scriptDir = os.path.join(cfenv.dataDir,'scripts')
        try:
            os.makedirs(cfenv.binDir)
        except Exception as ex1:
            pass
        try:
            os.makedirs(cfenv.dataDir)
        except Exception as ex1:
            pass
        try:
            os.makedirs(cfenv.pluginDir)
        except Exception as ex1:
            pass
        try:
            os.makedirs(cfenv.scriptDir)
        except Exception as ex1:
            pass
        
        #初始化配置文件路径
        cfenv.configFilePath = os.path.join(cfenv.rootDir,'config.json')
        cfenv.backupConfigFilePath = os.path.join(cfenv.rootDir,'config.json.backup')
        #cfenv.templeteScriptFile = os.path.join(cfenv.rootDir,'templete.js')

        #载入配置
        cfenv.loadConfig()

        #取环境变量名称
        #cfenv.switchScriptEnv()

    '''
        载入配置文件
    '''
    def loadConfig():
        #载入配置
        if pathlib.Path(cfenv.configFilePath).exists():
            #读入数据
            try:
                jsonStr = iotool.readAllText(cfenv.configFilePath)
                cfenv.configObj = json.loads(jsonStr)
            except Exception as exx:
                cfenv.initConfig()
        else:
            cfenv.initConfig()

    '''
        初始化配置文件,如果存在备份则使用，否则输出一个新的
    '''
    def initConfig():
        if pathlib.Path(cfenv.backupConfigFilePath).exists():
            shutil.copyfile(cfenv.backupConfigFilePath, cfenv.configFilePath)
        else:
            cfenv.writeNewConfig()
    
    '''
        保存配置
    '''
    def saveConfig():
        iotool.writeAllText(cfenv.configFilePath, json.dumps(cfenv.configObj, indent=4))

    '''
        输出标准配置文件
    '''
    def writeNewConfig():
        #初始化的例子
        cfenv.configObj['downloadDir'] = '~/PDownloaderDir'
        cfenv.configObj['plugins'] = {}
        cfenv.configObj['plugins']['testOne'] = {'name': '测试插件', 'dirName': 'testOne', 'readme': '这是一个测试插件'}
        #保存配置
        cfenv.saveConfig()
