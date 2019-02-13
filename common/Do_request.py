#-*-coding:utf-8 -*-
# @Time    :2019\1\1 0001 {TIME}
# @Author  :LiHaiLang
# @Email   :1614461577@qq.com
# @File    :run_test.py
# @Software:PyCharm
import requests
import json

class DoRequest:

    def __init__(self,method,url,data=None,cookies=None,headers=None):#对测试用例里面的方法进行判断
        try:
            if method == "get":
                self.res=requests.get(url=url,params=data,cookies=cookies,headers=headers)
            elif method == "post":
                self.res=requests.post(url=url,data=data,cookies=cookies,headers=headers)
        except Exception as e:
            raise e

    def get_status_code(self):#获得响应码
        return self.res.status_code
    def get_text(self):#返回str类型的响应体
        return self.res.text
    def get_json(self):# 返回dict类型的响应体
        json_dict = self.res.json()
        # 通过json.dumps函数将字典转换成格式化后的字符串
        # resp_text = json.dumps(json_dict, ensure_ascii=False, indent=4)
        # print('response: ', resp_text)  # 打印响应
        return json_dict




