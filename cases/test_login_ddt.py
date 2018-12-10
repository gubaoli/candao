import unittest
from selenium import webdriver
from page.zentao_loginpage import Login
from page.zentaoguanyupage import ZenPage
import ddt

datas = [
    {"user":"admin", "psw":"123456","expect":"True"},
    {"user":"admn", "psw":"123456", "expect":"False"},
    {"user":"admi", "psw":"123456", "expect":"False"},
    {"user":"admin", "psw":"13456", "expect":"False"},
    {"user":"dmin", "psw":"123456", "expect":"False"},
]
@ddt.ddt
class Test_guanyu(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.z = Login(self.driver)

    @ddt.data(*datas)
    def test_login_(self, test_datas):
        user = test_datas["user"]
        psw = test_datas["psw"]
        exp = test_datas["expect"]
        print("测试数据：%s %s"%(user, psw))
        self.z.login(user)
        result = self.z.get_login_reslut()
        if result == user:
            actul = True
        else:
            actul = False

        self.assertTrue(exp == actul)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()