from selenium import webdriver
import unittest,ddt
from PageObject.page_login import PageLogin
from Common.excel import Excel
from Common.log import Log

excel = Excel("login.xlsx").get_data()
@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        self.logger = Log("TestLogin").get_log()
        self.driver = webdriver.Safari()
        self.driver.maximize_window()
        self.log = PageLogin(self.driver)
        self.logger.info("---------用例开始---------")

    @classmethod
    def tearDown(self) -> None:
        self.logger.info("----------pass-----------")
        self.driver.quit()

    def login(self,url,user,paw):
        self.driver.get(url)
        self.log.is_user(user)
        self.log.is_paw(paw)
        self.log.is_bth()

    @ddt.data(*excel)
    def test_login(self,data):
        '''麦商机登陆测试用例'''
        self.login(
            data['url'],data['user'],data['paw'])
        text = self.log.is_login_text(
            data['suc'],data['assert'])
        print("麦商机登陆断言结果：",text)
        if True == text:
            self.assertTrue(text)
            self.logger.info("登陆成功")
        else:
            self.assertTrue(text)
            self.logger.info("登陆失败")

if __name__ == "__main__":
    unittest.main()