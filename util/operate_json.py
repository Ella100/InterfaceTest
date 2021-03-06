#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
import os
# 获取请求数据，请求数据直接写在json文件里

curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
rootPath = os.path.abspath(os.path.dirname(curPath))
print(rootPath)

class OperateJson(object):
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = "data/TestcaseHeaders.json"
            self.file_name = os.path.join(rootPath, self.file_name)
            print("self.file_name: ", self.file_name)

        self.data = self.get_json()

    # 读取 json 文件
    def get_json(self):
        with open(self.file_name,encoding='UTF-8') as fp:
            data = json.load(fp)
        return data

    # 根据关键词读取数据
    def get_key_data(self, key):
        return self.data[key]

if __name__ == '__main__':
    oj = OperateJson()
    print(oj.get_key_data("login"))
