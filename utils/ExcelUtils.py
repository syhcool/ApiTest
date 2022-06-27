#-*- coding:utf-8 -*-
#use:syh
import os
import xlrd2

class ExcelReader:
    # 1、验证文件是否存在
    def __init__(self,exce_file,sheet_by):
        if os.path.exists(exce_file):
            self.exce_file = exce_file
            self.sheet_by = sheet_by
            self._data = []
        else:
            raise FileNotFoundError("文件不存在")

    # 2、读取sheet方式，名称，索引
    def data(self):
        if not self._data:
            workbook = xlrd2.open_workbook(self.exce_file)
            if type(self.sheet_by) not in [str,int]:
                raise TypeError("请输入数字或字符串")
            elif type(self.sheet_by) == int:
                sheet = workbook.sheet_by_index(self.sheet_by)
            elif type(self.sheet_by) == str:
                sheet = workbook.sheet_by_name(self.sheet_by)
        # 3、读取sheet内容
            #获取首行信息
            title = sheet.row_values(0)
            #循环，过滤首行
            for col in range(1, sheet.nrows):
                col_value = sheet.row_values(col)
                # 2、与首行组成字典，放在list中
                self._data.append(dict(zip(title,col_value)))
        return self._data
# 4、结果返回
if __name__ == "__main__":
    read = ExcelReader("../testcase/t_excel/接口测试用例.xlsx", 0)
    print(read.data())
