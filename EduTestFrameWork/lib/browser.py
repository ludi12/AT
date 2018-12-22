# coding=utf8

from selenium import webdriver

def open_browser(browser='chrome', url='http://localhost/admin.php', impl_wait=10):
    """
    打开并初始化浏览器
    :param browser:
    :param url:
    :param impl_wait:
    :return:
    """
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser.lower() == 'ie':
        driver = webdriver.Ie()
    elif browser.lower() == 'opera':
        driver = webdriver.Opera()
    elif browser.lower() == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    driver.implicitly_wait(impl_wait)
    driver.maximize_window()
    driver.get(url=url)
    return driver