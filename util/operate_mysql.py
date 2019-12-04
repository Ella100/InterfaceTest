#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Desc    :   操作 数据库 中的数据
"""

import pymysql
import json


class OperateMysql(object):
    def __init__(self):
        # 数据库初始化连接
        self.connect_interface_testing = pymysql.connect(
            "129.28.170.125",
            "root",
            "Root@159357",
            "InterfaceTesting",
            cursorclass=pymysql.cursors.DictCursor
        )

        # 创建游标操作数据库
        self.cursor_interface_testing = self.connect_interface_testing.cursor()

    def select_data(self, sql):
        # 执行 sql 语句
        self.cursor_interface_testing.execute(sql)
        # 获取查询到的第一条数据
        first_data = self.cursor_interface_testing.fetchone()
        # 将返回结果转换成 str 数据格式
        first_data = json.dumps(first_data)
        return first_data


if __name__ == "__main__":
    om = OperateMysql()
    select_res = om.select_data(
        """
            SELECT * FROM test_table;
        """
    )
    print("select_res: ", select_res)

# GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '你的密码' WITH GRANT OPTION;
