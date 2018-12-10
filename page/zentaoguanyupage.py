from common.base import Base

class ZenPage(Base):
    '''登录页面元素抓取'''
    loc_about_1 = ("id", "proversion")
    loc_about_2 = ("id", "official")
    loc_about_3 = ("id", "changelog")
    loc_about_4 = ("id", "license")
    loc_about_5 = ("id", "extension")

    # 技术支持
    loc_jszc = ("xpath", ".//*[@class='card-content']/ul/li/a")

    # loc_jszc = ("css selector", ".card-content>ul>li>a")

    loc_about = ("link text", "关于")

    loc_iframe = ("id", "modalIframe")


    def swith_iframe(self):
        ele = self.find(self.loc_iframe)
        self.driver.switch_to_frame(ele)

    def click_about(self):
        self.click(self.loc_about)

    def click_link_no(self, n=0):
        # 定位一组，选下标去点击
        all = self.finds(self.loc_jszc)
        all[n].click()

    def click_about1(self):
        self.click(self.loc_about_1)

    def click_about2(self):
        self.click(self.loc_about_2)

    def click_about3(self):
        self.click(self.loc_about_3)

    def click_about4(self):
        self.click(self.loc_about_4)

    def click_about5(self):
        self.click(self.loc_about_5)


    #获取结果
    def get_result(self):
        self.driver.switch_to_window()


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    a = ZenPage(driver)

    # 先登录
    from page.zentao_loginpage import Login
    z = Login(driver)
    z.login()

    a.click_about()
    h1 = driver.current_window_handle

    a.swith_iframe()
    a.click_link_no(5)
    h2 = driver.window_handles
    driver.switch_to.window(h2[-1])
    t = driver.title
    x = ("xpath", ".//*[@id='article']/section/h3[1]")
    result = a.is_element_exist(x)
    print(result)
    driver.close()
    driver.switch_to.window(h1)

    assert result == True


