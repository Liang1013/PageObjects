from selenium import webdriver
import time
from Base.base import Base
from Common.route import Route

'''
ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
'''
class PageLogin(Base):

    user = ("css selector",".ant-form-horizontal>div:nth-child(1)>div>div>span>input")
    pwa = ("css selector",".ant-form-horizontal>div:nth-child(2)>div>div>span>input")
    bth = ("css selector",".registered-button")

    #断言
    success_text = ("css selector",".phone")
    fail_text = ("css selector",".ant-message-error>span")

    def is_user(self,user):
        self.sendkeys(self.user,user)

    def is_paw(self,paw):
        self.sendkeys(self.pwa,paw)

    def is_bth(self):
        self.click(self.bth)

    def is_login(self,):
        self.rou = Route().route_yaml("login.yaml","test")
        self.driver.maximize_window()
        self.driver.get(self.rou["url"])
        self.is_user(self.rou['user'])
        self.is_paw(self.rou['paw'])
        self.is_bth()

    def is_login_text(self,suc,text):
        if suc == 0:
            return self.findelment_text(self.success_text,text)
        elif suc == 1:
            return self.findelment_text(self.fail_text,text)
        else:
            return False