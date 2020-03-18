from case.basway import base
from selenium import webdriver

class LoginTest(base):


    loc_user=("xpath","//*[@id='account']")
    loc_password=("xpath","//*[@name='password']")
    loc_submit=("xpath",".//*[text()='登录']")

    def login(self):
        '''测试用例test_01，登录登录成功'''
        self.sendkeys(self.loc_user,"admin")
        self.sendkeys(self.loc_password,"123456")
        self.click(self.loc_submit)


if __name__ == '__main__':
      driver=webdriver.Firefox()
      driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
      loginer=LoginTest(driver)
      loginer.login()
      driver.quit()
