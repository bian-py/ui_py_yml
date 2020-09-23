from time import sleep

import pages
from base.app_base import AppBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageAppLogin(AppBase):
    def page_app_input_username(self, driver, msg):
        self.app_base_login_input(driver, pages.app_username, msg)

    def page_app_input_pwd(self, driver, pwd):
        self.app_base_login_input(driver, pages.app_pwd, pwd)

    def page_app_click_login_btn(self):
        sleep(2)
        self.base_click(pages.app_login_btn)

    def page_app_login_is_success(self):
        return self.app_base_is_exit(pages.app_me)

    def page_app_login(self, driver, msg, pwd):
        log.info(f"输入用户名{msg}")
        self.page_app_input_username(driver, msg)
        log.info(f"输入密码{pwd}")
        self.page_app_input_pwd(driver, pwd)
        log.info("点击确定按钮")
        self.page_app_click_login_btn()

    def page_app_login_success(self, driver, msg="13812345678", pwd='246810'):
        log.info(f"输入用户名{msg}")
        self.page_app_input_username(driver, msg)
        log.info(f"输入密码{pwd}")
        self.page_app_input_pwd(driver, pwd)
        log.info("点击确定按钮")
        self.page_app_click_login_btn()
