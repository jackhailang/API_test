#-*-coding:utf-8 -*-
# @Time    :2019\1\1 0001 {TIME}
# @Author  :LiHaiLang
# @Email   :1614461577@qq.com
# @File    :run_test.py
# @Software:PyCharm
#数据库的操作封装类
#1、连接数据库
#2、编写一个sql
#3、建立游标
#4、执行获得返回
import pymysql
from api_test2.common.Do_config import Config
class MysqlUtil:
    def __init__(self):
        #1、连接数据库
        config=Config()
        host = config.get('mysql', 'host')
        port = config.getint('mysql', 'port')#port是一个数值，所以要用int
        user = config.get('mysql', 'user')
        password = config.get('mysql', 'pwd')
        try:
            self.mysql=pymysql.connect(host=host, user=user, password=password,
                            database=None,port=port)
        except ConnectionError as e:
            print('连接异常，请检查')
            raise e
        #3、建立游标
    def fetch_one(self,sql):#查询一条数据并返回
        cursor=self.mysql.cursor()
        cursor.execute(sql)#根据sql进行查询。
        return cursor.fetchone()#4、获得返回值
if __name__ == '__main__':
     #2、编写一个sql
     sql = 'select mobilephone from future.member where  mobilephone != ""  order by mobilephone desc limit 1 '
     mysqluntil=MysqlUtil()
     results=mysqluntil.fetch_one(sql)
     print(results)
