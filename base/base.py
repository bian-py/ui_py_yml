from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog

log = GetLog.get_logger()

class Base:

    def __init__(self, driver):
        log.info(f"正在初始化driver：{driver}")
        self.driver = driver

    def base_get_element(self, loc, timeout=30, poll=0.5):
        log.info(f"正在查找元素：{loc}")
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll) \
            .until(lambda x: x.find_element(*loc))

    def base_click(self, loc):
        log.info(f"点击元素：{loc}")
        self.base_get_element(loc).click()

    def base_input(self, loc, msg):
        el = self.base_get_element(loc)
        log.info(f"清空元素：{loc}")
        el.clear()
        log.info(f"在{loc}元素上，输入{msg}")
        el.send_keys(msg)

    def base_get_text(self, loc):
        log.info(f"获取元素{loc}的文本信息")
        return self.base_get_element(loc).text

    # def base_if_login_success(self, loc):
    #
    #     if self.base_get_text(loc):
    #         return True
    #     else:
    #         return False
    def base_get_screenshot(self):
        log.error('出现错误，正在截图')
        self.driver.get_screenshot_as_file("../image/111.png")
