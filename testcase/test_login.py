#-*- coding:utf-8 -*-
#use:syh
import os
import pytest
from config import Conf
from config.Conf import ConfigYaml
from utils.YamlUtils import YamlReader
from utils.RequestsUtils import Request
from common import Base
import allure
import requests


test_file = Conf.get_data_path() + os.path.sep + "testlogin.yaml"
#test_file = os.path.join(Conf.get_data_path(),"testlogin.yaml")

data_list = YamlReader(test_file).data_all()
print(data_list)
@pytest.mark.parametrize("login",data_list)
def test_yaml(login):
    url = ConfigYaml().get_conf_url() + login["url"]
    print(url)
    data = login["data"]
    print(data)
    res = Request().post(url=url,json=data)
    print(res)

if __name__ == "__main__":
    report_path = Conf.get_report_path() + os.sep + "result"
    report_html_path = Conf.get_report_path()+os.sep+"html"
    pytest.main(["-s","test_excel_case.py","--alluredir",report_path])
    Base.allure_report(report_path, report_html_path)