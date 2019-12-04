#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
print('rootPath: ', rootPath)

from basic.get_excel_testcases import GetExcelTestcases
from basic.intergrate_request import IntergrateRequest
from util.email_config import EmailConfig
from util.operate_json import OperateJson
from util.compare_str import CompareStr


class RunExcelTestcases(object):
    def __init__(self):
        self.gtc = GetExcelTestcases()
        self.ir = IntergrateRequest()
        self.ec = EmailConfig()
        self.oj = OperateJson()
        self.cs = CompareStr()

    # 执行测试用例
    def run_testcases(self):
        # 定义空列表，存放执行成功和失败的测试用例
        pass_lists = []
        fail_lists = []
        no_execute_lists = []
        # no_execute_case_name = []

        # 获取总的用例条数
        cases_num = self.gtc.get_cases_num()
        # 遍历执行每一条测试用例
        for case in range(1, cases_num):
            # 用例是否执行
            is_run = self.gtc.get_is_run(case)
            # print("is_run: ", is_run)
            # 接口的请求方式
            method = self.gtc.get_method(case)
            # 请求测试接口
            url = self.gtc.get_url(case)
            # 要请求的数据
            data = self.gtc.get_payload(case)
            depend_case = self.gtc.is_depend(case)
            # 将参数写到json文件里
            # data = self.gtc.get_data_for_json(case)

            # 取出 header
            if case == 1:
                header = None
            else:
                header = self.oj.get_json()

            if depend_case != None:
                pass

            # 获取预期结果值 expected_result
            expected_result = self.gtc.get_expected_result(case)

            if is_run is True:
                res = self.ir.main_req(method, url, data, header)
                if self.cs.is_contain(expected_result, res):
                    self.gtc.write_actual_result(case, 'pass')
                    pass_lists.append(case)
                else:
                    self.gtc.write_actual_result(case, 'fail')
                    fail_lists.append(case)
            else:
                no_execute_lists.append(case)
        print("没有执行的测试用例, 按序号有：", no_execute_lists)
        self.ec.send_mail(pass_lists, fail_lists, no_execute_lists)
        print("....邮件已发送成功...")


if __name__ == "__main__":
    rts = RunExcelTestcases()
    rts.run_testcases()
    print("...程序已执行完毕...")
