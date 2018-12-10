import unittest
from selenium import webdriver
import time
class GanJi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self):
        self.driver.get("https://www.ganji.com")
    def tearDown(self):
        self.driver.delete_all_cookies()
    def test_Ganji(self):
        time.sleep(2)
        self.driver.find_element_by_link_text("登录").click()
        time.sleep(3)
        self.driver.find_element_by_name("login_username").send_keys(15801531433)
        self.driver.find_element_by_name("login_password").send_keys("zhili873230")
        time.sleep(2)
        self.driver.find_element_by_class_name("submit").click()
        time.sleep(3)
        a = self.driver.find_element_by_xpath('//*[@class="logined-a js-username"]')
        t = a.text
        self.assertEqual(t,"#m_290109486")
    def test_Ganji0(self):
        time.sleep(2)
        self.driver.find_element_by_link_text("登录").click()
        time.sleep(3)
        self.driver.find_element_by_name("login_username").send_keys(15801531433)
        self.driver.find_element_by_name("login_password").send_keys("zhili873230")
        time.sleep(2)
        self.driver.find_element_by_class_name("submit").click()
        time.sleep(3)
        try:
           a = self.driver.find_element_by_xpath('//*[@class="logined-a js-username"]')
           t = a.text
        except:
            t = ""
        self.assertNotEqual(t,"158015314")
if __name__=='__mian__':
    unittest.mian()