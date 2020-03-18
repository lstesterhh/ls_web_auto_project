from  selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

'''
from selenium.webdriver.support.ui import WebDriverWait

element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId"))
is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).until_not(lambda x: x.find_element_by_id("someId").is_displayed())
'''


# e1=WebDriverWait(driver,20,1).until(lambda x:x.find_element_by_id("account"))
# e1.send_keys("admin")
# e2=WebDriverWait(driver,20,1).until(lambda x:x.find_element_by_name("password"))
# e2.send_keys("123456")
# e3=WebDriverWait(driver,20,1).until(lambda x:x.find_element_by_id("submit"))
# e3.click()

class base():
        def __init__(self,driver:webdriver.Chrome):
            self.driver=driver
            self.timeout=20
            self.t=1

        def findelementnew(self,locator):
            '''定位到元素，返回元素对象，没定位到返回tiemout异常'''
            if not isinstance(locator,tuple):
                print('locator参数类型错误，必须传元祖类型：loc=("id","value1")')
            else:
                print('正在定位元素信息：定位方式->%s,value->%s'%(locator[0],locator[1]))
                element=WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
                return element


        def findelement(self,locator):
           element=WebDriverWait(self.driver,self.timeout,self.t).until(lambda x:x.find_element(*locator))
           return element

        def findelements(self,locator):
            try:
               elements=WebDriverWait(self.driver,self.timeout,self.t).until(lambda x:x.find_elements(*locator))
               return elements
            except:
                return []

        def sendkeys(self,locator,text):
            e=self.findelement(locator)
            e.send_keys(text)

        def click(self,locator):
            element=self.findelement(locator)
            element.click()

        def is_selected(self,locator):
            e=self.findelement(locator)
            r=e.is_selected()
            return r

        def is_ElementExist(self,locator):
          try:
            ele=self.findelement(locator)
            return True
          except:
            return False

        def is_ElementsExist2(self,locator):
            eles=self.findelements(locator)
            n=len(eles)
            if n==0:
                return False
            elif n==1:
                return True
            else:
                print("定位到元素个数 %s"%n)
                return True
        def is_title(self,_title):
           """返回bool值"""
           try:
                result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(_title))
                return result
           except:
                 return False

        def is_title_contain(self,_title):
            '''返回bool值'''
            try:
                result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(_title))
                return result
            except:
                return False

        def is_text_in_element(self,locator,_text):
             '''返回bool值'''
             try:
                 result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,_text))
                 return result
             except:
                 return False

        def is_text_to_present_in_element_value(self,locator,_value):
            '''返回boole值，空字符串返回false'''
            try:
              result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator,_value))
              return result
            except:
              return False

        def is_alter(self):
            '''返回alter对象'''
            try:
              result=WebDriverWait(self.driver,2,self.t).until(EC.alert_is_present())
              return result
            except:
              return False

        def move_to_element(self,locator):
            e=self.findelement(locator)
            ActionChains(self.driver).move_to_element(e).perform()

        def get_text(self,locator):
            '''获取文本'''
            try:
               txt=self.findelement(locator).text
               return txt
            except:
                print("获取text失败，返回")
                return ""

        def select_by_index(self,locator,index=0):
            '''通过索引，index是索引第几个，从0开始，默认选第一个'''
            element=self.findelement(locator)
            Select(element).select_by_index(index)

        def select_by_value(self,locator,value):
            '''通过value属性'''
            element=self.findelement(locator)
            Select(element).select_by_value(value)

        def select_by_text(self,locator,text):
            '''通过文本值定位'''
            element=self.findelement(locator)
            Select(element).select_by_visible_text(text)

        def js_scroll_top(self):
            '''滚动到顶部'''
            js="window.scrollTo(0,0)"
            self.driver.execute_script(js)

        def js_scroll_end(self,x=0):
            '''滚动到底部,x代表横向滚动'''
            js="window.scrollTo(%s,document.body.scrollHeight)%x"
            self.driver.execute_script(js)

        def js_focus_element(self,locator):
            '''聚焦元素'''
            target=self.findelement(locator)
            self.driver.execute_script("arguments[0].scrollIntoView();",target)

if __name__ == '__main__':
     driver=webdriver.Firefox()
     driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
     test11=base(driver)
     # loc1=(By.ID,"account")
     # loc2=(By.NAME,"password")
     # loc3=(By.ID,"submit")
     loc1=("id","account")
     loc2=("name","password")
     loc3=("id","submit")
     test11.sendkeys(loc1,"admin")
     test11.sendkeys(loc2,"123456")
     test11.click(loc3)







