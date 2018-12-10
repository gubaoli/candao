from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Firefox()
# driver.get("http://127.0.0.1:81/zentao/user-login.html")

# 基类
class Base():
    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver

    # def find(self, by, value, timeout=30):
    #     element = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element(by, value))
    #     return element
    #
    # def finds(self, by, value, timeout=30):
    #     element = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements(by, value))
    #     return element

    def find(self, locator, timeout=30):
        element = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_element_located(locator))
        return element

    def finds(self, locator, timeout=30):
        elements = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_all_elements_located(locator))
        return elements

    def send(self, locator, text):
        element = self.find(locator)
        element.send_keys(text)

    def click(self, locator):
        element = self.find(locator)
        element.click()

    def clear(self, locator):
        element = self.find(locator)
        element.clear()

    def get_text(self, locator, timeout=30):
        try:
            element = self.find(locator, timeout)
            t = element.text
            return t
        except:
            return ""

    def is_text_in_element(self, locator, _text, timeout=30):
        try:
            r = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, _text))
            return True
        except:
            return False

    def is_alert_exist(self, timeout=30):
        a = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        return a

    def move_to_element(self, locator):
        e = self.find(locator)
        ActionChains(self.driver).move_to_element(e).perform()

    def is_element_exist(self, locator, timeout=10):
        try:
            self.find(locator, timeout)
            return True
        except:
            return False

    def swith_frame(self, locator):
        ele = self.find(locator)
        self.driver.switch_to.frame(ele)

    def js_to_end(self):
        js1 = "window.scrollTo(0, 10000)"
        self.driver.execute_script(js1)

    def js_to_top(self):
        js1 = "window.scrollTo(0, 0)"
        self.driver.execute_script(js1)

    def js_to_elemenet(self, locator):
        target = self.find(locator)
        driver.execute_script("arguments[0].scrollIntoView();", target)




if __name__ == '__main__':
    driver = webdriver.Firefox()
    b = Base(driver)
    driver.get()
    driver.find_element_by_id()
    b.click()




