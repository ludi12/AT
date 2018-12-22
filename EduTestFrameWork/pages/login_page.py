# coding=utf8

from selenium.webdriver.common.by import By
from manage_center_page import ManageCenterPage
from base_page import BasePage

class LoginPage(BasePage):
    """
    登录页面
    """

    # 定义页面内的元素

    # 用户名输入框
    username_loc = (By.ID,'username')
    # 密码输入框
    password_loc = (By.ID,'password')
    # 登录按钮
    login_btn_loc = (By.CSS_SELECTOR, "input[value='登 录']")

    def input_username(self, username):
        """
        输入用户名
        :param username: 要输入的用户名
        :return: None
        """
        self.input_text(self.username_loc, username)
        return

    def input_password(self, password):
        """
        输入登录密码
        :param username: 要输入的用户名
        :return: None
        """
        self.input_text(self.password_loc, password)
        return

    def click_login_button(self):
        """
        点击登录按钮
        :return: None
        """
        self.click_element(self.login_btn_loc)
        return ManageCenterPage(self._driver)