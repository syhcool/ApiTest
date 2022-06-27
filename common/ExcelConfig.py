#-*- coding:utf-8 -*-
#use:syh
"""
用例ID	模块	接口名称	请求URL	前置条件	请求类型	请求参数类型	请求参数	预期结果	实际结果	备注
是否运行	headers	cookies	status_code	数据库验证
"""
class dataconfig:
    cass_id = "用例ID"
    cass_model = "模块"
    cass_name = "接口名称"
    url = "请求URL"
    pre_exec = "前置条件"
    method = "请求类型"
    params_type = "请求参数类型"
    params = "请求参数"
    expect_result = "预期结果"
    actual_result = "实际结果"
    is_run = "是否运行"
    headers = "headers"
    cookies = "cookies"
    code = "status_code"
    db_verify = "数据库验证"
