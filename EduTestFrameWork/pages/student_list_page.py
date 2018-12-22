# coding=utf8

from time import sleep
from base_page import BasePage
from add_student_page import AddStudentPage
from selenium.webdriver.common.by import By

class StudentListPage(BasePage):
    """
    学生列表页面
    """


    # 添加学生按钮
    add_student_loc = (By.XPATH, "//span[.='添加学生']")


    def click_add_student(self):
        """
        点击添加学生
        :return: 添加学生信息页面对象
        """
        self.click_element(self.add_student_loc)
        sleep(1)
        return AddStudentPage(self._driver)