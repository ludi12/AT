# coding=utf8

import os
import unittest
from HTMLTestRunnerCN import HTMLTestRunner
from script.student_testcase import StudentManage
from lib.log_util import log_init
import logging

def main():
    log_init()
    logging.info("测试开始")
    # test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(StudentManage)
    test_suite = unittest.defaultTestLoader.discover("script", "*_testcase.py")

    report = open(r'report\report.html', 'w')
    runner = HTMLTestRunner(stream=report, verbosity=0, title='Edu测试报告', description='测试的描述信息', tester='李志超')
    runner.run(test_suite)
    # unittest.TextTestRunner(verbosity=2,descriptions='测试结果').run(test_suite)

    report.close()
    logging.info("生成测试报告")
    # 恢复数据库
    sql_file = r'resource\edu.sql'
    ret = os.system('mysql -uroot -proot --default-character-set=utf8 < %s'%sql_file)
    if ret:
        logging.error("恢复数据库失败")
    else:
        logging.info("恢复数据库完成")
    logging.info("测试结束")


if __name__ == '__main__':
    main()