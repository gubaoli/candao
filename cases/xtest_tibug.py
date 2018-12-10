import unittest
from selenium import webdriver
import time
from page.loginpage import LoginPage
from page.tijiaobugpage import TiJiao

class TestTiJiao(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.z = LoginPage(self.driver)
        self.z.login()
        self.a = TiJiao(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_ti_bug(self):
            timestr = str(time.time())
            self.a.ti_bug(timestr)#提交bug
            #获取bug
            result = self.a.get_bug_list_title_text()
            print(result)

            self.assertEqual(result, "111:"+timestr)

if __name__=="__main__":
    unittest.main()
