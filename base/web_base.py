from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()


# Web专属base
class WebBase(Base):
    def web_base_click_element(self, placeholder_text, click_text):
        # 点击复选框——暂停——点击包含文本的元素
        log.info("点击复选框")
        loc = By.CSS_SELECTOR, f'[placeholder="{placeholder_text}"]'
        self.base_click(loc)
        sleep(1)
        log.info(f"点击频道：{click_text}")
        loc = By.XPATH, f'//*[text()="{click_text}"]'
        self.base_click(loc)

    def web_base_is_exist(self, id):
        loc = By.XPATH, f"//*[text()='{id}']"
        try:
            self.base_get_element(loc, timeout=3)
            log.info("找到对应文章ID元素")
            return True
        except:
            log.error("未找到文章ID信息")
            return False
