# coding=utf8

import os
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddStudentPage(BasePage):
    "添加学生页面"
    
    account_el = (By.ID, 'username')
    nickname_el = (By.ID, 'realname')
    password_el = (By.ID, 'password')
    sex_male = (By.CSS_SELECTOR, "input[name='sex'][value='1']")
    sex_female = (By.CSS_SELECTOR, "input[name='sex'][value='0']")
    sex_secret = (By.CSS_SELECTOR, "input[name='sex'][value='2']")
    role_el = (By.NAME, 'roleid')
    upload_img = (By.XPATH, "//span[contains(., '上传头像')]")
    local_upload = (By.XPATH, "//li[contains(., '本地上传')]")
    upload_input = (By.CSS_SELECTOR, "input[name='imgFile']")
    upload_ok = (By.CSS_SELECTOR, "input[value='确定']")
    email_el = (By.ID, 'email')
    phone_el = (By.ID, 'phone')
    save_stu = (By.ID, 'btn_sub')
    
    def input_account(self, username):
        "输入用户帐号"
        self.input_text(self.account_el, username)
        
    def input_nickname(self, nickname):
        "输入用户昵称"
        self.input_text(self.nickname_el, nickname)
        
    def input_password(self, password):
        "输入用户密码"
        self.input_text(self.password_el, password)
        
    def select_sex(self, sex):
        "选择性别"
        if sex == '男':
            self.click_element(self.sex_male)
        elif sex == '女':
            self.click_element(self.sex_female)
        else:
            self.click_element(self.sex_secret)
        
    
    def select_role(self, role):
        "选择角色"
        sel = Select(self.get_element(self.role_el))
        sel.select_by_visible_text(role)
    
    def upload_image(self, filepath):
        "上传头像"
        self.click_element(self.upload_img)
        self.click_element(self.local_upload)
        self.input_text(self.upload_input, filepath)
        self.click_element(self.upload_ok)
        
    def input_email(self, email):
        "输入邮箱地址"
        self.input_text(self.email_el, email) 
        
    def input_phone(self, phoneno):
        "输入手机号码"
        self.input_text(self.phone_el, phoneno) 
        
    def save_student(self):
        "点击确认保存"
        self.click_element(self.save_stu)
        
    
    def add_student_action(self, username, nickname, password, sex, role, filepath, email, phoneno):
        "添加学生"
        self.input_account(username)
        self.input_nickname(nickname)
        self.input_password(password)
        self.select_sex(sex)
        self.select_role(role)
        self.upload_image(os.path.abspath(filepath))
        self.input_email(email)
        self.input_phone(phoneno)
        self.save_student()
        return
    
    def get_save_result(self):
        "获取保存学生的结果"
        return self.get_alert_message()
    
    