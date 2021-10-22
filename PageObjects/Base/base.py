from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

from Common.log import Log
'''
 Example:
            from selenium.webdriver.support.ui import WebDriverWait \n
            element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
            is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
                        until_not(lambda x: x.find_element_by_id("someId").is_displayed())
'''
class Base():

    def __init__(self,driver:webdriver.Chrome):
        self.logger = Log("Base").get_log()
        self.driver = driver
        self.times = 20

    def findelement(self,locale):
        try:
            element = WebDriverWait(self.driver,self.times)\
                .until(lambda x: x.find_element(*locale))
            return element
        except:
            self.logger.error("%s 页面未能找到此定位%s 元素"%(locale))

    def findelment_text(self,locale,text):
        try:
            element = WebDriverWait(self.driver,self.times)\
                .until(EC.text_to_be_present_in_element(locale,text))
            return element
        except:
            self.logger.error("%s 页面未能找到此断言%s 元素"%(locale))
            return False

    def sendkeys(self,locale,value):
        self.findelement(locale)\
            .send_keys(value)

    def click(self,locale):
        self.findelement(locale)\
            .click()