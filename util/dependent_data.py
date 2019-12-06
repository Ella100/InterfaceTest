#coding=utf-8
from util.operate_excel import OperateExcel
from basic.intergrate_request import IntergrateRequest
from basic.get_excel_testcases import GetExcelTestcases
from jsonpath_rw import jsonpath,parse
import json

class DependentData:
    def __init__(self,case_id):
        self.case_id = case_id
        self.operate_excel = OperateExcel()
        self.data = GetExcelTestcases()

    # 通过caseId获取该caseid的整行数据
    def get_case_line_data(self):
       rows_data = self.operate_excel.get_rows_data(self.case_id)
       return rows_data

    # 执行依赖测试，获取结果
    def run_dependent(self):
        run_method = IntergrateRequest()
        # 拿行号
        row_num = self.operate_excel.get_row_num(self.case_id)
        # 请求数据
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_method(row_num)
        url = self.data.get_url(row_num)
        # 执行
        res = run_method.main_req(method,url,request_data,header)
        return json.loads(res)

    # 根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        # 根据层级关系去拿值
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)#结果集
        return [math.value for math in madle][0]

if __name__ == "__main__":
    o = DependentData("A0002")
    print(o.get_case_line_data())

    order = {
        "oriReqSn": "201912060000028126533628963713",
        "isSuccess": "true"
    }
    res = "oriReqSn"
    json_exe = parse(res)
    madle = json_exe.find(order)
    print([math.value for math in madle][0])
