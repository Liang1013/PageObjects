import unittest,ddt,os

propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filepath = os.path.join(propath, "Data","tt.json")

@ddt.ddt
class UnitTesting(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        pass

    @classmethod
    def tearDown(self) -> None:
        pass

    @ddt.file_data(filepath)
    def test_A(self,tt):
        '''解析json格式文件，打印出结果'''
        print(tt)

if __name__ == "__main__":
    unittest.main()
