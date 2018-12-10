from common.base import Base
login_url = "http://127.0.0.1/zentao/user-login.html"


class Login(Base):
    loc_user = ("id", "account")
    loc_psw = ("css selector", "[name='password']")
    loc_baoc = ("id", "keepLoginon")
    loc_dengl = ("id", "submit")


    def input_user(self, user):
        self.send(self.loc_user, user)

    def input_psw(self,psw):
        self.send(self.loc_psw, psw)

    def click_baocun(self):
        self.click(self.loc_baoc)

    def click_dengl(self):
        self.click(self.loc_dengl)


    def login(self, user="admin", psw="123456", flog=False):
        self.driver.get(login_url)
        self.input_user(user)
        self.input_psw(psw)
        if flog:
            self.click_baocun()
        self.click_dengl()


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    z = Login(driver)
    #driver.get(login_url)
    z.login(flog=True)

    #z.input_user("admin")
    #z.input_psw("123456")
    #z.click_baocun()
    #z.click_dengl()