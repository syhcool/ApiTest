#-*- coding:utf-8 -*-
#use:syh
import json
import re
import subprocess
import os

from config.Conf import ConfigYaml
from config import Conf
from utils.MysqlUtils import Mysql
from utils.AssertUtil import AssertUtils
from utils.LogsUtils import my_log
from utils import LogsUtils


p_data = '\${(.*)}\$'
log = my_log()


#1、定义一个方法init_db
def init_db(db_alias):
    # 2、初始化数据库信息
    db_info = ConfigYaml().get_db_config_file(db_alias)
    host = db_info["host"]
    user = db_info["user"]
    passwd = db_info["passwd"]
    db_name = db_info["database"]
    port = int(db_info["port"])
#3、初始化sql对象
    conn = Mysql(host,user,passwd,db_name,port)
    print(conn)
    return conn
def json_parse(data):
    return json.load(data) if data else data
#替换获取的数据

def res_find(data,pattern_data=p_data):
    #pattern = re.compile('\${(.*)}\$')
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    return re_res
def res_sub(data,replase,pattern_data=p_data):
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    if re_res:
        re.sub(pattern_data,replase,data)
    return re_res
def params_find(handers,cookies):
    if "${" in handers:
        handers = res_find(handers)
    if "${" in cookies:
        cookies = res_find(cookies)
    return handers,cookies

def assert_db(db_name,result,db_verify):
    assert_util = AssertUtils()
    sql = init_db(db_name)
    #2、查询sql，excel定义好的
    db_res = sql.fetchone(db_verify)
    #log.debug("数据库查询结果：{}".format(str(db_res)))
    #3、数据库的结果与接口返回的结果验证
    #获取数据库结果的key
    verify_list = list(dict(db_res).keys())
    #根据key获取数据库结果，接口结果
    for line in verify_list:
        res_line = result[line]
        res_db_line = dict(db_res)[line]
        assert_util.asser_body(res_line, res_db_line)
def allure_report(report_path,report_html_path):
    allure_cmd = "allure generate {} -o {} --clean".format(report_path,report_html_path)
    log.info("报告地址")
    try:
        subprocess.call(allure_cmd,shell=True)
    except:
        log.error("用例执行失败")
        raise

if __name__ =="__main__":
    #init_db("db_uat")
    print(res_find('{"Authorization": "JWT ${token}$"}'))

