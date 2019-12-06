#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Desc    :   对 Excel 的读写操作
"""
import xlrd
from xlutils.copy import copy

import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
rootPath = os.path.abspath(os.path.dirname(curPath))
print(rootPath)

class OperateExcel(object):
    def __init__(self, file_name=None, sheet_id=None):
        """
        :param file_name: excel文件的具体路径名称
        :param sheet_id:  要操作的第几 sheet 页
        """
        if file_name:
            self.file_name = file_name
        else:
            # self.file_name = '../data/util_data/operate_excel.xls'
            # self.file_name = os.path.join(basedir, "../data/TestcasesKeyword.xls")
            self.file_name = "data/TestcasesKeyword.xls"
            self.file_name = os.path.join(rootPath, self.file_name)
            print(self.file_name)
            # print("file_name: ", self.file_name)
            # file_path = os.path.abspath(self.file_name)
            # print("file_path: ", file_path)

        if sheet_id:
            self.sheet_id = sheet_id
        else:
            self.sheet_id = 0

        self.sheet_table = self.get_sheet()

    # 获取 sheet 页操作对象
    def get_sheet(self):
        data = xlrd.open_workbook(self.file_name)
        # 获得sheet表
        sheet_table = data.sheets()[self.sheet_id]
        return sheet_table

    # 获取该 sheet 页的行数和列数，拿到的是一个元组
    def get_sheet_nrows_ncols(self):
        return self.sheet_table.nrows, self.sheet_table.ncols

    # 获取该 sheet 页的行数
    def get_sheet_nrows(self):
        return self.sheet_table.nrows

    # 获取该 sheet 页的列数
    def get_sheet_ncols(self):
        return self.sheet_table.ncols

    # 获取具体单元格的数据
    def get_sheet_cell(self, row, col):
        """
        :param row: 单元格的行值
        :param col: 单元格的列值
        :return: cell_data
        """
        cell_data = self.sheet_table.cell_value(row, col)
        return cell_data

    # 写入数据到 excel 中
    def write_to_excel(self, row, col, value):
        # 同样的先打开 excel 操作句柄
        data = xlrd.open_workbook(self.file_name)
        copy_data = copy(data)
        # 选择写入的 sheet 页
        copy_data_sheet = copy_data.get_sheet(0)
        # 写入数据
        copy_data_sheet.write(row, col, value)
        # 保存数据
        copy_data.save(self.file_name)

#   根据对应的caseId找到对应行的内容
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    # 根据对应的caseId找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        clos_data = self.get_cols_data()
        for col_data in clos_data:
            if case_id in col_data:
                return num
            num = num + 1

    #根据行号找到该行的内容
    def get_row_values(self,row):
        row_data = self.sheet_table.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_cols_data(self,col_id=None):
        if col_id != None:
            cols = self.sheet_table.col_values(col_id)
        else:
            cols = self.sheet_table.col_values(0)
        return cols

if __name__ == "__main__":
    oe = OperateExcel()
    # print("获取 excel 表的行数和列表，返回元组形式：", oe.get_sheet_nrows_ncols())
    # print("获取 excel 表的行数：", oe.get_sheet_nrows())
    # print("获取 excel 表的列数：", oe.get_sheet_ncols())
    # print("获取单元格(1, 1)的值：", oe.get_sheet_cell(1, 1))
    # print("获取单元格(1, 2)的值：", oe.get_sheet_cell(1, 2))
    # print("获取单元格(2, 2)的值：", oe.get_sheet_cell(2, 2))
    # oe.write_to_excel(17, 7, '写入的数据')




