# coding=utf8

import unittest
from selenium import webdriver
from lib.browser import open_browser
from pages.login_page import LoginPage
from lib.read_conf import *
from time import sleep
import logging

tc_conf = read_test_config('conf/testcase_conf.yml')['StudentManage']
test_data_conf = read_test_data('script/student_testcase.yml')

@unittest.skipUnless(tc_conf['StudentManage'], 'skip StudentManage tests')
class StudentManage(unittest.TestCase):
    """
    学生模块测试用例
    """

    def setUp(self):
        self.driver = open_browser(browser='chrome', url='http://localhost/admin.php', impl_wait=10)

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    @unittest.skipUnless(tc_conf['test1_add_student'], 'skip test1_add_student test')
    def test1_add_student(self):
        """
        添加学生
        :return:
        """
        logging.info("执行测试用例test1_add_student")
        td = test_data_conf['test1_add_student']
        # 登录系统
        login_page = LoginPage(self.driver)
        login_page.input_username(td['login_username'])
        login_page.input_password(td['login_password'])
        manage_center_page = login_page.click_login_button()
        ret = login_page.page_should_contain(td['login_verify_text'])
        self.assertTrue(ret, '登录失败')
        #
        # ManageCenterPage(self.driver).go_to_member_center()
        # MemberManagePage(self.driver).go_to_student_list()
        # StudentListPage(self.driver).click_add_student()
        #
        member_mange_page = manage_center_page.go_to_member_center()
        student_list_page = member_mange_page.go_to_student_list()
        add_student_page = student_list_page.click_add_student()
        add_student_page.add_student_action(td['username'], td['nickname'], td['password'],
                                            td['sex'], td['roll'], td['tx_path'],
                                            td['email'], td['phone'])

        ret = add_student_page.get_save_result()
        self.assertEqual(ret, u'保存成功', '保存学生信息失败')
        logging.info("执行测试用例test1_add_student结果: pass")

    @unittest.skipUnless(tc_conf['test2_del_student'], 'skip test2_del_student test')
    def test2_del_student(self):
        """
        删除学生
        :return:
        """
        logging.info("执行测试用例test2_del_student")
        logging.info("执行测试用例test2_del_student结果: pass")