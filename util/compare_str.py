#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class CompareStr(object):
    def is_contain(self, str1, str2):
        """
        判断预期结果是否和实际结果相同
        :param str1: 预期结果值
        :param str2: 实际结果值
        :return: flag
        """
        if str1 in str2:
            flag = True
        else:
            flag = False
        return flag


if __name__ == "__main__":
    cs = CompareStr()
    print(cs.is_contain("abc", "abcedf"))
