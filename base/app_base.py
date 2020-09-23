from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import pages
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()


class AppBase(Base):
    def app_base_is_exit(self, loc):
        log.info(f"开始判断页面元素{loc}是否存在")
        try:
            self.base_get_element(loc, timeout=3)
            print(f"找到元素{loc}")
            log.info("已经找到对应元素")
            return True

        except:
            print(f"未找到元素{loc}")
            log.error("未找到对应元素")
            return False

    def app_base_login_input(self, driver, loc, msg):
        log.info("开始进行自定义输入方法（相当于sendkeys)")
        self.base_click(loc)
        log.info(f"查找元素{loc}并点击")
        sleep(2)
        log.info("执行输入遍历")
        for a in msg:
            key = int(a) + 7
            driver.press_keycode(key)

    def app_base_right_swipe_left(self, loc_area, click_channel):
        log.info("正在调用从右向左滑动方法")
        # 查找区域元素
        el = self.base_get_element(loc_area)
        # 获取区域元素的位置（y坐标）,返回值是一个字典
        y = el.location.get("y")
        print(el.location)
        # 获取区域元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 计算起始位置和终止位置的坐标点
        start_x = width * 0.8
        start_y = y + height * 0.5
        end_x = width * 0.2
        end_y = y + height * 0.5
        # 在指定区域查找元素，通过添加其父级的方式
        # loc = By.XPATH, f"//*[@class='android.widget.HorizontalScrollView']//*[contains(@test,'{click_channel}')]
        # //*可以直接用class的值来代替，并且如果是直属级别后面用单个/
        loc = By.XPATH, f"//android.widget.HorizontalScrollView/*[contains(@text,'{click_channel}')]"
        # 循环滑动
        while True:
            # 获取当前页面结构
            page_source = self.driver.page_source
            try:
                sleep(1)
                el_target = self.base_get_element(loc, timeout=3)
                print(f"找到目标元素{loc}")
                sleep(1)
                el_target.click()
                break
            except:
                print(f"未找到元素{loc},进行滑动，重新寻找")
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            if page_source == self.driver.page_source:
                print("滑到最后一个屏幕，未找到元素")
                raise NoSuchElementException

    def app_base_down_swipe_up(self, loc_area, click_channel):
        log.info("正在调用从下到上滑动")
        # 查找区域元素
        el = self.base_get_element(loc_area)
        y = el.location.get("y")
        print(el.location)
        # 获取区域元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 计算起始位置和终止位置的坐标点
        start_x = width * 0.5
        start_y = y + height * 0.8
        end_x = width * 0.5
        end_y = y + height * 0.2
        # 在指定区域查找元素，通过添加其父级的方式
        # loc = By.XPATH, f"//*[@class='android.widget.HorizontalScrollView']//*[contains(@test,'{click_channel}')]
        # //*可以直接用class的值来代替，并且如果是直属级别后面用单个/
        loc = By.XPATH, f"//*[@bounds='[0,196][540,858]']//*[contains(@text,'{click_channel}')]"
        # 循环滑动
        while True:
            # 获取当前页面结构
            page_source = self.driver.page_source
            try:
                sleep(1)
                el_target = self.base_get_element(loc, timeout=3)
                print(f"找到目标元素{loc}")
                sleep(1)
                el_target.click()
                sleep(5)
                self.driver.press_keycode(4)
                break
            except:
                print(f"未找到元素{loc},进行滑动，重新寻找")
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            if page_source == self.driver.page_source:
                print("滑到最后一个屏幕，未找到元素")
                raise NoSuchElementException




