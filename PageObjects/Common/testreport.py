from Common import HTMLTestRunner
from Common.route import Route
from Common.log import Log
import  unittest

class TestReport():
    logger = Log("TestReport").get_log()

    def __init__(self):
        self.discover = unittest.defaultTestLoader.discover(
            start_dir=Route().route_report("TestCases"),pattern="test*.py")
        self.reportpath = Route().route_report("Reports/") + "report.html"
        self.fg = open(self.reportpath, "wb")
        self.reunner = HTMLTestRunner.HTMLTestRunner(
            stream=self.fg,title="麦商机测试用例",description="自动化测试")

    def report(self):
        '''运行'''
        self.reunner.run(self.discover)
        self.logger.info("生成测试报告成功")