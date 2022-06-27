#-*- coding:utf-8 -*-
#use:syh
import pymysql
from utils.LogsUtils import my_log
from utils.YamlUtils import YamlReader
from config.Conf import ConfigYaml
#连接数据库
class Mysql:
    def __init__(self,host,user,passwd,database,port=3306):
        self.log = my_log()
        self.db_config = YamlReader

        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            database=database,
            #    charset = "utf-8"
        )
        #设置游标为字典
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def find_one(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def find_all(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def exec(self,sql):
        """执行"""
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Mysql 执行失败，已回滚")
            self.log.error(ex)
            return False
        return True
    #关闭对象
    def __del__(self):
        #关闭光标对象
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()
if __name__ == "__main__":

    mysql = Mysql("211.103.136.242","test","test123456","meiduo",port =7090)
    res = mysql.find_all("select * from tb_users")
    print(res)
# conn = pymysql.connect(
#     host ="211.103.136.242",
#     port =7090,
#     user ="test",
#     passwd ="test123456",
#     database = "meiduo",
# #    charset = "utf-8"
# )
