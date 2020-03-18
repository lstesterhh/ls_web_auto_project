#coding:utf-8
from selenium import webdriver
import unittest
import time
from page.loginpage import LoginPage
import ddt
from common.read_excel import ExcelUtil
import os

'''
1、输入用户admin,密码：123456，登录
2、输入用户admin，密码输入空，点击登录
3、输入用户空，输入123456，点击保持登录，点击登录
'''
url="http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html"
# testdates=[
#         {"user":"admin","psw":"123456","expect":"admin"},
#         {"user":"admin","psw":"","expect":""},
#         {"user":"","psw":"123456","expect":""}
#     ]
propath=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filepath=os.path.join(propath,"common","datas.xlsx")
print(filepath)

filepath="G:\\web_auto_pro\\common\\datas.xlsx"
sheetName="Sheet1"
data=ExcelUtil(filepath,sheetName)
testdates=data.dict_data()
print(testdates)


@ddt.ddt
class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
       #  cls.driver= webdriver.Firefox()
        cls.driver.maximize_window()
        cls.logpage=LoginPage(cls.driver)
        cls.driver.get(url)

    def setUp(self):
        self.logpage.is_alter_exist()
        self.driver.delete_all_cookies()
        self.driver.get(url)

    # def tearDown(self):
    #     self.logpage.is_alter_exist()
    #     self.driver.delete_all_cookies()
    #    # self.driver.refresh()


    def login_case(self,user,psw,expect):
        self.logpage.input_user(user)
        self.logpage.input_password(psw)
        self.logpage.click_submit()
        result=self.logpage.get_login_name()
        print(result)
        self.assertTrue(result==expect)

    @ddt.data(*testdates)
    def test_01(self,data):
      '''输入用户admin,密码：123456，登录'''
      print("测试数据:%s"%data)
      self.login_case(data["user"],data["psw"],data["expect"])

    @classmethod
    def tearDownClass(cls):
       cls.driver.quit()



if __name__ == '__main__':
    unittest.main()

