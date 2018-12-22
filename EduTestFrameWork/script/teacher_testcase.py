# coding=utf8

import unittest
from selenium import webdriver
from lib.browser import open_browser
from pages.login_page import LoginPage
from lib.read_conf import *
from time import sleep
import logging


tc_conf = read_test_config('conf/testcase_conf.yml')['TeacherManage']

@unittest.skipUnless(tc_conf['TeacherManage'], 'skip TeacherManage tests')
class TeacherManage(unittest.TestCase):
    """
    学生模块测试用例
    """

    @unittest.skipUnless(tc_conf['test1_add_teacher'], 'skip test1_add_teacher test')
    def test1_add_teacher(self):
        """
        添加教师
        :return:
        """
        logging.info("执行测试用例test1_add_teacher")
        logging.info("执行测试用例test1_add_teacher结果: pass")

    @unittest.skipUnless(tc_conf['test2_del_teacher'], 'skip test2_del_teacher test')
    def test2_del_teacher(self):
        """
        删除教师
        :return:
        """
        logging.info("执行测试用例test2_del_teacher")
        logging.info("执行测试用例test2_del_teacher结果: pass")