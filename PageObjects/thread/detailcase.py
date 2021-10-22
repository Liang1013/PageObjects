from thread.paracase import ParaCase

class DetailCase(ParaCase):

    def test_login(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_name("wd").send_keys("李昂")
        self.driver.find_element_by_id("su").click()