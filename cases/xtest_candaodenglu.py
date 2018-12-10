import unittest
from selenium import webdriver
import time
class ChanDao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()#只打开一个浏览器
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()#关闭
    def setUp(self):
        self.driver.get("http://127.0.0.1/zentao/user-login.html")
    def tearDown(self):
        self.driver.delete_all_cookies()#清除cookies
    def test_Deng1(self):
         time.sleep(3)
         self.driver.find_element_by_css_selector("#account").send_keys("admin")
         self.driver.find_element_by_css_selector('[name="password"]').send_keys("123456")
         self.driver.find_element_by_css_selector("#submit").click()
         time.sleep(3)
         a = self.driver.find_element_by_css_selector("#userMenu>a")
         t = a.text
         self.assertEqual(t,"admin")
if __name__=='__mian__':
    unittest.main()



