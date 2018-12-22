# coding=utf8

from selenium.common.exceptions import *
from time import sleep

class BasePage(object):
    """
    所有页面的父类
    """

    def __init__(self, driver):
        self._driver = driver

    def get_element(self, locator):
        """
        获取页面元素
        :param locator: 元素的定位信息,eg: (By.ID,'username')
        :return: 匹配的元素对象
        """
        return self._driver.find_element(*locator)

    def get_elements(self, locator):
        """
        获取一组页面元素
        :param locator: 元素的定位信息,eg: (By.ID,'username')
        :return: 匹配的元素对象的列表
        """
        return self._driver.find_elements(*locator)

    def input_text(self, locator, text):
        """
        向文本框输入文本
        :param locator:
        :param text:
        :return:
        """
        ele = self.get_element(locator=locator)
        ele.clear()
        ele.send_keys(text)
        return

    def click_element(self, locator):
        """
        点击页面元素
        :param locator:
        :return:
        """
        self.get_element(locator=locator).click()
        return

    def page_should_contain(self, text):
        """
        校验页面的文本
        :param text:
        :return:
        """
        xpath = "//*[contains(., '%s')]" % text
        try:
            self._driver.find_element_by_xpath(xpath=xpath)
            return True
        except NoSuchElementException:
            return False

    def get_alert_message(self):
        """
        返回当前页面的消息窗文本
        :return:
        """
        try:
            sleep(2)
            a = self._driver.switch_to.alert
            return a.text
        except:
            return