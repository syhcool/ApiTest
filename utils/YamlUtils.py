#-*- coding:utf-8 -*-
#use:syh
#1、创建类
#2、初始化，文件是否村子
#3、yaml文件读取
import os
import yaml

class YamlReader:
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self._data = None
        self._data_all = None
    #单个文档读取
    def data(self):
        #第一次调用data读取yaml文件，如果不是，之前返回之前保存的数据
        if not self._data:
            with open(self.yamlf,"rb") as f:
                self._data = yaml.safe_load(f)
        return self._data
    def data_all(self):
        #读取多个，第一次调用data读取yaml文件，如果不是，之前返回之前保存的数据
        if not self._data_all:
            with open(self.yamlf,"rb") as f:
                self._data_all = list(yaml.safe_load_all(f))
        return self._data_all