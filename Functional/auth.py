# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class auth(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_auth(self, login="admin", password="admin"):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(login, password, wd)
        self.open_sensors_list(wd)
        self.assertTrue(success)

    def login(self, login, password, wd):
        wd.find_element_by_css_selector("input.Input-Control").click()
        wd.find_element_by_css_selector("input.Input-Control").clear()
        wd.find_element_by_css_selector("input.Input-Control").send_keys("%s" % login)
        wd.find_element_by_xpath("//div[@class='Form']/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='Form']/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='Form']/div[2]/input").send_keys("%s" % password)
        wd.find_element_by_xpath("//div[@class='Form']//button[.='Войти']").click()

    def open_sensors_list(self, wd):
        wd.find_element_by_xpath("//div[@class='NavBar']/div[1]/div[3]/span/span").click()

    def open_home_page(self, wd):
        wd.get("http://172.17.30.30:8888/login")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
