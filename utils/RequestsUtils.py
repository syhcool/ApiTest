#-*- coding:utf-8 -*-
#use:syh
#1、创建封装get方法
#2、发送requests get请求
#3、获取结果响应内容
#4、内容存在字典
#5、字典返回
import requests
from utils.LogsUtils import my_log
class Request:
    def __init__(self):
        self.log = my_log("Requests")

    def requests_api(self,url,json=None,headers=None,method="get"):
        if method == "get":
            self.log.debug("发送get请求")
            r = requests.get(url, json=json, headers=headers)
        elif method == "post":
            self.log.debug("发送post请求")
            r = requests.post(url, json=json, headers=headers)
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text()
        res = dict()
        res["code"] = code
        res["body"] = body

        return res
    def get(self,url,params=None,**kwargs):
        return self.requests_api(url,method="get",arams=params,**kwargs)
    def post(self,url, json=None,**kwargs):
        return self.requests_api(url,method="post", json=json,**kwargs)