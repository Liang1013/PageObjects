import unittest

class ParaCase(unittest.TestCase):
    #unittest增加参数化
    def __init__(self,methodName='Tests',param=None):
        super(ParaCase, self).__init__(methodName)
        self.driver = param

    def setUp(self) -> None:
        self.driver.maximize_window()

    @staticmethod
    def parametrize(testcase,param=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase(name,param=param))
        return suite
