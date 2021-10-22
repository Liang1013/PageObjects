import unittest,threading
from thread.paracase import ParaCase
from thread.detailcase import DetailCase

from selenium import webdriver

class MythRead(threading.Thread):

    def __init__(self,dirver):
        threading.Thread.__init__(self)
        self.driver = dirver

    def run(self):
        print("Starting" + self.name)
        print("Exiting" + self.name)
        srunn_suite(self.driver)

def srunn_suite(dirver):
    suites = unittest.TestSuite()
    suites.addTest(ParaCase.parametrize(DetailCase,param=dirver))
    unittest.TextTestRunner(verbosity=1).run(suites)

if __name__ == "__main__":
    dr = [webdriver.Chrome(executable_path="/usr/local/bin/chromedriver"),webdriver.Safari()]
    for i in range(len(dr)):
        print(dr[i])
        th = MythRead(dr[i])
        th.start()
        th.join()
