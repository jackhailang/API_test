#-*-coding:utf-8 -*-
# @Time    :2019\1\1 0001 {TIME}
# @Author  :LiHaiLang
# @Email   :1614461577@qq.com
# @File    :run_test.py
# @Software:PyCharm
import configparser#读取配置文件
import os #路径拼接
from api_test2.common import Do_contants
#1、创建实例
#2、加载配置文件
#3、根据section，option来获取配置文件的值
class Config:
    #1、创建实例
    def __init__(self):
        self.config=configparser.ConfigParser()#每次进行配置文件操作都需要执行，所以进行初始化函数，定义为类的属性。
    #2、加载配置文件
        file_name=os.path.join(Do_contants.config_dir,'globle.conf')
        self.config.read(filenames=file_name,encoding='utf-8')
        if self.getboolean('switch','on'):
            online = os.path.join(Do_contants.config_dir, 'online.conf')
            self.config.read(filenames=online,encoding='utf-8')
        else:
            test = os.path.join(Do_contants.config_dir, 'test.conf')
            self.config.read(filenames=test,encoding='utf-8')
    #3、根据section，option来获取配置文件的值
    def get(self,section,option):#返回str类型
        return self.config.get(section,option)

    def getboolean(self,section,option):#返回布尔类型
        return self.config.getboolean(section,option)

    def getint(self,section,option):
        return self.config.getint(section,option)

    def getfloat(self,section,option):
        return self.config.getfloat(section,option)
if __name__ == '__main__':
    con=Config()
    con_1=con.get('mysql','user')
    print(con_1)


