#-*- coding:utf-8 -*-
#use:syh
#封装log工具类
#1、创建类
#2、定义参数
#3、编写输出控制台
import logging
from config import Conf
import datetime,os
from config.Conf import ConfigYaml

log_l = {
    "info" : logging.INFO,
    "debug" : logging.DEBUG,
    "warning" : logging.WARNING,
    "error" : logging.ERROR
}

class Logger:
    # 2、定义参数(输出文件路径，loggername，日志级别)
    def __init__(self,log_file,log_name,log_level):
        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level

        self.logger = logging.getLogger(self.log_name)
        # 2、设置日志级别
        self.logger.setLevel(log_l[self.log_level])
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        if not self.logger.handlers:
            #输出控制台
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level])
            fh_stream.setFormatter(formatter)

            # 3、创建handler
            fh_file = logging.FileHandler(self.log_file,encoding="utf-8",mode="a")
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)
            #创建handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)
#1、初始化参数数据
#日志文件名称，日志文件级别
#日志文件名称 = logs目录+当前时间+拓展名
#log目录
log_path = Conf.get_log_path()
#当前时间
current_time = datetime.datetime.now().strftime("%Y-%m-%d")
#拓展名
log_extension = ConfigYaml().get_conf_log_extension()
logfile = os.path.join(log_path,current_time + log_extension)
#print(logfile)
#日志文件级别
loglevel = ConfigYaml().get_conf_log()
#2、对外方法，初始log工具类，提供其他类使用
def my_log(log_name = __file__):
    return Logger(logfile,log_name,loglevel).logger

if __name__ == "__main__":
    my_log().debug("this is a debug")
