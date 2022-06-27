#-*- coding:utf-8 -*-
#use:syh
import os
from utils.YamlUtils import YamlReader
#1、获取项目基本目录
#获取绝对路径
current = os.path.abspath("../")

#定义config目录的路径
_config_path = current + os.sep + "config"
#定义conf.yaml文件的路径
_config_file = _config_path + os.sep + "conf.yaml"
#定义日志文件的路径
_log_path = current + os.sep + "logs"
#定义db_config.yaml文件路径
_db_config_file = _config_path + os.sep + "db_config.yaml"
#定义data目录的路径
_data_path = current + os.sep + "data"
#定义allure生成的位置
_allure_path = current + os.sep + "report"

def get_data_path():
    return _data_path

def get_config_path():
    return _config_path
def get_config_file():
    return _config_file

def get_log_path():
    return _log_path
def get_db_config_file():
    return _db_config_file
def get_report_path():
    return _allure_path

#2、读取配置文件
#创建类
#初始化yaml读取配置文件
#定义方法获取信息
class ConfigYaml:
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()
        self.db_config = YamlReader(get_db_config_file()).data()
    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]
    #获取日志级别
    def get_conf_log(self):
        return self.config["BASE"]["log_level"]
    #获取日志拓展名
    def get_conf_log_extension(self):
        return self.config["BASE"]["log_extension"]
    #获取数据库信息
    def get_db_config_file(self,db_alias):
        return self.db_config[db_alias]
    #excel_case
    def get_excel_case_file(self):
        return self.config["BASE"]["tasecase_file"]
    def get_excel_case_file_sheet(self):
        return self.config["BASE"]["sheet_name"]
    def get_email_info(self):
        return self.config["email"]


if __name__ == "__main__":
    # conf_read = ConfigYaml()
    # #print(conf_read.get_conf_url())
    # # print(conf_read.get_conf_log())
    # # print(conf_read.get_conf_log_extension())
    # print(conf_read.get_db_config_file("db_uat"))
    print(ConfigYaml().get_email_info())