#-*-coding:utf-8 -*-
# @Time    :2019\1\1 0001 {TIME}
# @Author  :LiHaiLang
# @Email   :1614461577@qq.com
# @File    :run_test.py
# @Software:PyCharm
import unittest
from api_test2.common.Do_excel import DoExcel
from api_test2.common import Do_contants
from api_test2.common.Do_request import DoRequest
import json
from api_test2.common.Do_config import Config
from ddt import ddt,data,unpack
#1、还是需要从excel里面获取测试用例
run_excel = DoExcel(Do_contants.testcase_dir)  # 创建实例定位到excel测试用例
cases=run_excel.get_cases('login')#获取测试数据
@ddt#进行数据驱动，读取多条用例并执行,如果不写，只会执行一条用例。
class Login(unittest.TestCase):
    def setUp(self):
        print('开始测试')
    @data(*cases)#取到传进来的case用例
    def testlogin(self,cases):
        data=json.loads(cases.data)
        url = Config().get('api', 'url') + cases.url
        res = DoRequest(method=cases.http_method, url=url, data=data)  # 获取接口请求
        print('status_code:', res.get_status_code())  # 打印响应码
        res_dict = res.get_json()  # 获取请求响应，字典
        self.assertEqual(cases.expected,res.get_text()) #断言判断excel里面的期望值与实际返回的响应体是否一致
    def tearDown(self):
        print('测试结束')
