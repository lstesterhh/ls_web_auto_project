#coding:utf-8
import time
import unittest

from selenium import webdriver
from page.loginpage import LoginPage,url
from page.addbugpage import Addbug
class Addbugcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.add=Addbug(cls.driver)
        a=LoginPage(cls.driver)
        a.login()

    def setUp(self):
       # self.driver=webdriver.Chrome()
       # self.driver.maximize_window()
       # self.driver.get(url)
       # self.login=LoginPage(self.driver)
       # self.login.login()
       # self.add=Addbug(self.driver)
     self.driver.get(url)

    def test_addbug_01(self):
     timestr=str(time.time())
     self.add.addbug(timestr)
     result=self.add.get_bug_list_title_text()
     print(result)
     self.assertEqual(result,"测试的标题:"+ timestr)

    def test_addbug_02(self):
     timestr=str(time.time())
     self.add.addbug(timestr)
     result=self.add.get_bug_list_title_text()
     print(result)
     self.assertEqual(result,"测试的标题:"+ timestr)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()