#-*- coding:utf-8 -*-
#use:syh
"""
登录	登录成功	http://211.103.136.242:8064/authorizations/
POST	json	{"username":"python","password":"123456"}	登录成功
"""
#import requests
from utils.RequestsUtils import Request
from config.Conf import ConfigYaml
import pytest
from utils.AssertUtil import AssertUtils
from common.Base import init_db

class test:
    def __init__(self):
        self.conf_y = ConfigYaml()
        self.url_path = self.conf_y.get_conf_url()

    def test_login(self):
        url = self.url_path + "/authorizations/"
        data = {"username":"python","password":"12345678"}
        r = Request().post(url=url,json=data)
        token = r["body"]["token"]
        return token
        print(r["body"]["token"])

class Test_one:

    def test_login(self):
        self.test = test()
        url = self.test.url_path + "/authorizations/"
        data = {"username":"python","password":"12345678"}
        r = Request().post(url=url,json=data)
        code = r["code"]
        body = r["body"]
        AssertUtils().asser_code(code,200)
        #AssertUtils().asser_in_body(body,'"id":"1","username":"python"')
        print(r)
        #1、初始化数据库
        conn = init_db("db_uat")
        #2、查询结果
        res_db = conn.find_one("select id,username from tb_users where username = 'python'")
        print('数据库查询结果{}'.format(res_db))
        #3、验证
        user_id = body["user_id"]
        username = body["username"]
        assert user_id == res_db["id"]
    @pytest.mark.skip
    def test_info(self):
        self.test = test()
        url = self.test.url_path + "/user/"
        headers = {
               'Authorization': 'JWT ' + test().test_login()
     }
        r = Request().get(url=url,headers=headers)
        print(r)

    def goods_list(self):
        self.test = test()
        url = self.test.url_path +"/cateqories/115/skus"
        params = {"page":"1","page_size":"10","ordering":"create_time"}
        r =Request().get(url=url,json=params)

        print(r.json())

    def goods_cart(self):
        self.test = test()
        url = self.test.url_path +"/cart/"
        headers = {
            'Authorization': 'JWT ' + test().test_login()
        }
        data = {"sku_id":"3","count":"1","selected":"true"}
        r = Request().post(url=url,headers=headers,json=data)
        print(r.json())

    """
    保存订单	http://211.103.136.242:8064/orders/	登录	post	json	
    {"address":"1","pay_method":"1"}
    """
    def orders(self):
        self.test = test()
        url = self.test.url_path +"/orders/"
        headers = {
            'Authorization': 'JWT ' + test().test_login()
        }
        data = {"address":"1","pay_method":"1"}
        r = Request().post(url=url,headers=headers,json=data)
        print(r.json())
if __name__== "__main__":
    pytest.main(["-vs","test_Mail.py::Test_one::test_login"])