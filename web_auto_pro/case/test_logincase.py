from selenium import webdriver
import unittest
import time
from page.loginpage import LoginPage

'''
1、输入用户admin,密码：123456，登录
2、输入用户admin，密码输入空，点击登录
3、输入用户空，输入123456，点击保持登录，点击登录
'''
url="http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html"
class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
       #  cls.driver= webdriver.Firefox()
        cls.driver.maximize_window()
        cls.logpage=LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(url)

    def tearDown(self):
        #self.logpage.is_alter_exist()
        self.driver.delete_all_cookies()
       # self.driver.refresh()


    def test_01(self):
        '''输入用户admin,密码：123456，登录'''
        self.logpage.input_user("admin")
        self.logpage.input_password("123456")
        self.logpage.click_submit()
        result=self.logpage.get_login_name()
        print(result)
        # try:
        #  self.assertTrue(result=="admin")
        # except AssertionError:
        #     print("test_01 登录失败")
        # else:
        #     print("test_01 测试成功")
        self.assertTrue(result=="admin")


    def test_02(self):
        '''2、输入用户admin，密码输入空，点击登录'''
        self.logpage.input_user("admin")
        self.logpage.click_submit()
        self.logpage.is_alter_exist()
        result=self.logpage.get_login_name()
        print(result)
        # try:
        #  self.assertTrue(result=="")
        # except AssertionError:
        #     print("test_02 登录失败")
        # else:
        #     print("test_02 测试成功")
        self.assertTrue(result=="")



    def test_03(self):
        '''输入用户空，输入123456，点击保持登录，点击登录'''
        self.logpage.input_password("123456")
        self.logpage.click_keeplogin()
        self.logpage.click_submit()
        self.logpage.is_alter_exist()
        result=self.logpage.get_login_name()
        print(result)
        # try:
        #  self.assertTrue(result=="")
        # except AssertionError:
        #     print("test_03 登录失败")
        # else:
        #     print("test_03测试成功")
        self.assertTrue(result=="")



    def test_04(self):
        print("aaaaaaaaaaaaaaaa")
        self.logpage.click_forget_password()
        result=self.logpage.is_refresh_exist()
        print(result)
        # self.logpage.is_alter_exist()
        # try:
        #    self.assertTrue(result)
        # except AssertionError:
        #     print("test_04 登录失败")
        # else:
        #     print("test_04测试成功")
        self.assertTrue(result)



    @classmethod
    def tearDownClass(cls):
       cls.driver.quit()



if __name__ == '__main__':
    unittest.main()

