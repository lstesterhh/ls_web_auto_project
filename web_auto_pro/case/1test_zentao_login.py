#coding=utf-8
import unittest
from selenium import webdriver
import time
url="http://127.0.0.1/zentao/my/"
class LoginTestCase01(unittest.TestCase):
    '''登录案例'''
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()

    def setUp(self):
        self.driver.get(url)

    def get_login_useinfo(self):
      try:
        t=t=self.driver.find_element_by_xpath(".//*[text()='退出']").text
        return t
      except:
        pass

    def is_alert_on(self):
        try:
            a=self.driver.switch_to.alert
            text=a.text()
            a.accept()
            return text
        except:
            return ""


    def test_01(self):
        '''用例说明1'''
        time.sleep(4)
        self.driver.find_element_by_xpath("//*[@id='account']").send_keys("admin")
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@id='keepLoginon']").click()
        self.driver.find_element_by_xpath(".//*[text()='登录']").click()
        time.sleep(5)
        user=self.get_login_useinfo()
        print("获取的结果是：%s" %user)
        self.assertTrue(user=="退出")

    def test_02(self):
        '''test_02运行失败的测 '''
        time.sleep(4)
        self.driver.find_element_by_xpath("//*[@id='account']").send_keys("admin11")
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@id='keepLoginon']").click()
        self.driver.find_element_by_xpath(".//*[text()='登录']").click()
        time.sleep(5)
        user=self.get_login_useinfo()
        print("获取的结果是：%s" %user)
        self.assertTrue(1== 2)



    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
        unittest.main()