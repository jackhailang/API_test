#-*-coding:utf-8 -*-
# @Time    :2019\1\1 0001 {TIME}
# @Author  :LiHaiLang
# @Email   :1614461577@qq.com
# @File    :run_test.py
# @Software:PyCharm
#常量管理：常量，一般不会改变的变量
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取到项目的根路径
# print(base_dir)
config_dir=os.path.join(base_dir,'conf')#配置文件的路径
# print(config_dir)
datas_dir=os.path.join(base_dir,'datas')#datas文件夹的路径
testcase_dir=os.path.join(datas_dir,'testcase.xlsx')
# print(datas_dir)
reports_dir=os.path.join(base_dir,'reports')#reports文件夹的路径
# print(reports_dir)
logs_dir=os.path.join(base_dir,'logs')#logs文件夹的路径
logs_file=os.path.join(logs_dir,'files')
logs_error=os.path.join(logs_dir,'error')
print(logs_file)


