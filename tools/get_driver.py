# 区别两张导包使用方式
from time import sleep

from selenium import webdriver
import appium.webdriver

import pages
from base.base import Base


class GetDriver:
    __web_driver = None
    __app_driver = None

    @classmethod
    def get_web_driver(cls, url):
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开URL
            cls.__web_driver.get(url)
        return cls.__web_driver

    @classmethod
    def quit_web_driver(cls):
        if cls.__web_driver is not None:
            cls.__web_driver.quit()
            # 置空浏览器对象
            cls.__web_driver = None

    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            desired_caps = dict()
            desired_caps["platformName"] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = 'emulator-5554'
            # desired_caps['appPackage'] = 'com.android.settings'
            # desired_caps['appActivity'] = '.HWSettings'
            desired_caps['appPackage'] = pages.app_package
            desired_caps['appActivity'] = pages.app_activity
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            cls.__app_driver = appium.webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quit()
            cls.__app_driver = None





if __name__ == '__main__':
    driver = GetDriver.get_app_driver()
    print(driver)
    el = Base(driver).base_get_element(pages.app_username)
    el.click()
    sleep(2)
    msg = "13812345678"
    input(msg, driver)
    sleep(5)
    GetDriver.quit_app_driver()
