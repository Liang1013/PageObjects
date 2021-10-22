from Base.base import Base
from selenium import webdriver

import time

class PageUpload(Base):

    log_bth = ("id","switcher_plogin")
    user = ("id","u")
    paw = ("id","p")
    bth = ("id","login_button")

    letter = ("id","composebtn")
    upload = ("name","UploadFile")


    def qq_upload(self):
        self.driver.switch_to.frame("login_frame")
        self.click(self.log_bth)
        self.sendkeys(self.user,"1634262959")
        self.sendkeys(self.paw,"liang1013")
        self.click(self.bth)
        self.driver.switch_to.default_content()
        self.click(self.letter)
        self.driver.switch_to.frame("mainFrame")
        self.sendkeys(self.upload,"麦商机V2.2测试用例.xmind")
        self.driver.switch_to.default_content()


if __name__ == "__main__":
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    driver.maximize_window()
    driver.get("https://mail.qq.com/")
    up = PageUpload(driver)
    up.qq_upload()

    time.sleep(4)
    driver.quit()