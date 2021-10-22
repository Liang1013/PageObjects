import xlrd,os

class Excel:

    def __init__(self,file):
        propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        filepath = os.path.join(propath, "Data",file)
        self.book_data = xlrd.open_workbook(filepath)
        self.book_sheet = self.book_data.sheet_by_name("Sheet1")  # 打开文件中的第一个表
        self.keys = self.book_sheet.row_values(0)  # 获取第一行作为字典的键
        self.rownum = self.book_sheet.nrows  # 获取行数
        self.colnum = self.book_sheet.ncols  # 获取列数

    def get_data(self):
        list = []
        for i in range(1,self.rownum):
            rows_data = self.book_sheet.row_values(i)  # 获取每一行值作为列表
            rows_dir = {}
            for y in range(0,self.colnum):  # 将每一列的值与每一行对应起来
                rows_dir[self.keys[y]] = rows_data[y]
            list.append(rows_dir)
        return list

if __name__ == "__main__":
    data = Excel("login.xlsx")
    t = data.get_data()
    print(t)