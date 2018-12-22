# coding=utf8

from base_page import BasePage
from member_manage_page import MemberManagePage
from selenium.webdriver.common.by import By

class ManageCenterPage(BasePage):
    """
    管理中心页面
    """


    # 课程管理链接
    course_manage_loc = (By.LINK_TEXT, '课程管理')

    # 会员中心链接
    member_center_loc = (By.LINK_TEXT, '会员中心')


    def go_to_course_manage(self):
        """
        切换到课程管理模块
        :return:
        """
        self.click_element(self.course_manage_loc)
        return

    def go_to_member_center(self):
        """
        切换到会员中心模块
        :return:
        """
        self.click_element(self.member_center_loc)
        return MemberManagePage(self._driver)


