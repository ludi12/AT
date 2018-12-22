# coding=utf8

import yaml
import logging

def read_test_config(filename):
    """
    读取测试用例的配置
    :param filename:
    :return: 字典类型
    """
    with open(filename) as f:
        return yaml.load(f)



def read_test_data(filename):
    """
    从配置文件读取测试数据
    :param filename:
    :return: 字典类型
    """
    with open(filename) as f:
        return yaml.load(f)