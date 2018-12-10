# coding:utf-8
from selenium import webdriver
import unittest
import time
class DengLu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()#只打开一次浏览器
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()#关闭浏览器
    def setUp(self):#前置条件
        self.driver.get("http://127.0.0.1/zentao/user-login.html")
    def tearDown(self):#后置处理关闭浏览器
        self.driver.delete_all_cookies()#退出登录
    def test_DengLu01(self):
        time.sleep(3)
        self.driver.find_element_by_css_selector("#account").send_keys("admin")
        self.driver.find_element_by_css_selector('[name="password"]').send_keys("123456")
        self.driver.find_element_by_css_selector("#submit").click()
        time.sleep(3)
        #实际结果
        a =self.driver.find_element_by_css_selector("#userMenu>a")
        t = a.text
        self.assertEqual(t,"admin")
    def test_DengLu02(self):
        time.sleep(3)
        self.driver.find_element_by_css_selector("#account").send_keys("admin1")
        self.driver.find_element_by_css_selector('[name="password"]').send_keys("123456")
        self.driver.find_element_by_css_selector("#submit").click()
        time.sleep(3)
        try:
           a =self.driver.find_element_by_css_selector("#userMenu>a")
           t = a.text
        except:
            t = ""
        self.assertNotEqual(t,"admin")
if __name__=='__mian__':
    unittest.mian()


