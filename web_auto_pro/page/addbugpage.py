#coding:utf-8
from case.basway import base
from selenium import webdriver
import time


class Addbug(base):

    loc_test=("xpath",'.//*[@data-id="qa"]/a')
    loc_bug=("xpath",'.//*[@data-id="bug"]/a')
    loc_tibug=("xpath",".//*[text()='提Bug']")
    loc_yxbb=("xpath",'.//*[@class="chosen-choices"]/li')
    loc_truck=("xpath",".//*[@id='openedBuild_chosen']/div/ul/li")
    loc_biaoti=("xpath",".//*[@id='title']")
    iframe=("class name","ke-edit-iframe")
    body=("class name","article-content")
    submit=("xpath",".//*[@id='submit']")
    loc_buglist=("xpath",".//*[@id='bugList']/tbody/tr/td[4]/a")
    loc_firselement=("xpath",".//*[@id='bugList']/tbody/tr[1]/td[4]/a")


    def addbug(self,timestr):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_tibug)
        self.click(self.loc_yxbb)
        self.click(self.loc_truck)
        self.sendkeys(self.loc_biaoti,text="测试的标题:%s" %timestr)
        frame=self.findelement(self.iframe)
        self.driver.switch_to.frame(frame)
        self.sendkeys(self.body,text="你好禅道body正文")
        self.driver.switch_to.default_content()
        self.click(self.submit)

    def get_bug_list_title_text(self):
        try:
            all_title=self.findelements(self.loc_buglist)
            print(all_title)
            t1=all_title[0].text
            print(t1)
            return t1
        except:
            return ""

    def get_new_text(self,_text):
        result=self.is_text_in_element(self.loc_firselement,_text=_text)
        print("结果如下:%s"%result)
        return result

if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://127.0.0.1:81/zentao/user-login.html")
    from case.atest_zentao_login_new import LoginTest
    login=LoginTest(driver)
    login.login()
    loc_firselement=("xpath",".//*[@id='bugList']/tbody/tr[1]/td[4]/a")
    add_bug=Addbug(driver)
    timestr=str(time.time())
    print(timestr)
    add_bug.addbug(timestr)
    result=add_bug.get_bug_list_title_text()
    print("开始校验相等： "+result)
    y="测试的标题:"+timestr
    r1=add_bug.get_new_text(y)
    print("新的测试结果如下：%s" %r1)
    # assert result ==y
    driver.quit()









