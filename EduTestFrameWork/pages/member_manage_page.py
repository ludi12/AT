# coding=utf8

from base_page import BasePage
from student_list_page import StudentListPage
from selenium.webdriver.common.by import By

class MemberManagePage(BasePage):
    """
    会员管理页面
    """


    # 学生列表链接
    student_list_loc = (By.LINK_TEXT, '学生列表')
    # 教师列表链接
    teacher_list_loc = (By.LINK_TEXT, '教师列表')
    # 角色列表链接
    roll_list_loc = (By.LINK_TEXT, '角色列表')

    # mainframe
    mainframe_loc = (By.ID, 'mainframe')

    def go_to_student_list(self):
        """
        切换到学生列表
        :return:
        """
        self.click_element(self.student_list_loc)
        self._driver.switch_to.frame(self.get_element(self.mainframe_loc))
        return StudentListPage(self._driver)

    def go_to_teacher_list(self):
        """
        切换到教师列表
        :return:
        """
        self.click_element(self.teacher_list_loc)
        return

    def go_to_roll_list(self):
        """
        切换到角色列表
        :return:
        """
        self.click_element(self.roll_list_loc)
        return
