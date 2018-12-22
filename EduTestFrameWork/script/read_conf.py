# -*-coding:utf-8 -*-

import yaml

def read_test_config(filename):
    """
    读取测试用例的配置
    :param filename:
    :return:
    """
    with open(filename) as f:
        return yaml.load(f)
if __name__ == '__main__':
    print read_test_config('E:\Python_script\Demo\AutoTest20181106\EduTestFrameWork\conf/testcases_config.yml')
