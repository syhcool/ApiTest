#-*- coding:utf-8 -*-
#use:syh
from utils.LogsUtils import my_log
import json
#定义封装类
class AssertUtils:
    #初始化数据，日志
    def __init__(self):
        self.log = my_log("AssertUtil")
    #验证返回状态码相等,raise返回异常
    def asser_code(self,code,expected_code):
        try:
            assert int(code) == int(expected_code)
            return True
        except:
            self.log.error("code error,code is {},expected_code is {}".format(code,expected_code))
            raise

    # 验证返回body相等,raise返回异常
    def asser_body(self,body,expected_body):
        try:
            assert int(body) == int(expected_body)
            return True
        except:
            self.log.error("body error,body is {},expected_body is {}".format(body,expected_body))
            raise

    def asser_in_body(self,body,expected_body):

        try:
            body = json.dumps(body)
            assert expected_body in body
            return True
        except:
            self.log.error("不包含或者body是错误的,body is {},expected_body is {}".format(body,expected_body))
            raise