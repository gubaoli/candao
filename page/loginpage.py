import unittest
from selenium import webdriver
import time
from common.base import Base


class LoginPage():
    def __init__(self, driver):#初始化
        self.driver = driver
        self.b = Base(self.driver)

    def login(self, uesr="admin", psw="123456"):
        self.driver.get("http://127.0.0.1/zentao/user-login.html")
        time.sleep(3)
        self.b.send("xpath", ".//*[@id='account']", "admin")
        self.b.send("css selector", "[name='password']", "123456")
        self.b.click("css selector", "#submit")

    def get_login_reslut(self):#断言
        #time.sleep(3)
        #try:
            #t = self.b.get_text("css selector", "#userMenu>a")
            #return t
        #except:
            #return ""
        self.b.get_text("css selector", "#userMenu>a", timeout=5)

if __name__=='__main__':#实例化
    driver = webdriver.Firefox()
    z = LoginPage(driver)
    z.login()
    result = z.get_login_reslut()
    print(result)



