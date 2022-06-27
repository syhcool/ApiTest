#-*- coding:utf-8 -*-
#use:syh
from utils.ExcelUtils import ExcelReader
from common.ExcelConfig import dataconfig

class Data:
    def __init__(self,tasecase_file,sheet_name):
        self.read = ExcelReader(tasecase_file, sheet_name)

    def get_run_data(self):
        run_list = []
        for line in self.read.data():
            if str(line[dataconfig.is_run]).upper() == "Y":
                run_list.append(line)
        return run_list

    def get_case_list(self):
        """
        获取全部测试用例
        :return:
        """
        # run_list=list()
        # for line in self.reader.data():
        #         run_list.append(line)
        run_list = [line for line in self.read.data()]
        return run_list

    def get_case_pre(self, pre):
        # 获取全部测试用例
        # list判断，执行，获取
        """
        根据前置条件：从全部测试用例取到测试用例
        :param pre:
        :return:
        """
        run_list = self.get_case_list()
        for line in run_list:
            if pre in dict(line).values():
                return line
        return None