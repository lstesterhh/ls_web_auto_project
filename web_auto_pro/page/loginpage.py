#coding:utf-8
from case.basway import base
from selenium import webdriver
import time

url="http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html"
class LoginPage(base):
    # 定位登录界面的元素
    loc_user=("xpath","//*[@id='account']")
    loc_password=("xpath","//*[@name='password']")
    loc_submit=("xpath",".//*[text()='登录']")
    loc_keep_login=("xpath",".//*[@id='keepLoginon']")
    loc_loginname=("xpath",".//*[@id='userMenu']/a")
    loc_forget_password=("xpath",".//*[text()='忘记密码']")
    loc_refresh=("xpath",".//*[text()='刷新']")

    def input_user(self,text):
       self.sendkeys(self.loc_user,text)

    def input_password(self,text):
        self.sendkeys(self.loc_password,text)

    def click_keeplogin(self):
        self.click(self.loc_keep_login)

    def click_submit(self):
        self.click(self.loc_submit)

    def get_login_name(self):
        user=self.get_text(self.loc_loginname)
        return user

    def login(self,user="admin",psw="123456",keep_login=False):
        '''登录流程'''
        self.driver.get(url)
        self.input_user(user)
        self.input_password(psw)
        if keep_login:self.click_keeplogin()
        time.sleep(2)
        self.click_submit()



    def is_alter_exist(self):
       # try:
       #      a=self.driver.switch_to.alert
       #      a.accept()
       # except:
       #      return
      a=self.is_alter()
      if a:
          print("当前有alter对象")
          time.sleep(2)
          a.accept()
      else:
          print("当前没有alter对象"+str(a))

    def click_forget_password(self):
        self.click(self.loc_forget_password)

    def is_refresh_exist(self):
        r=self.is_ElementExist(self.loc_refresh)
        return r

if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.maximize_window()
    # driver.get(url)
    login=LoginPage(driver)
    # login.input_user("admin")
    # login.input_password("123456")
    # login.click_keeplogin()
    # login.click_submit()
    #
    login.login()





    driver.quit()



