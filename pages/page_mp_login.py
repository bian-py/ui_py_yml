from time import sleep

import pages
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMpLogin(WebBase):

    def page_input_username(self, username):
        self.base_input(pages.mp_username, username)

    def page_input_password(self, password):
        self.base_input(pages.mp_password, password)

    def page_click_login_btn(self):
        sleep(1)
        self.base_click(pages.mp_btn)

    # 断言使用
    def page_get_nickname(self):
        return self.base_get_text(pages.mp_usernickname)

    # 脚本层调用
    def page_mp_login(self, username, password):
        '''登录业务'''
        log.info(f"正在调用自媒体登录业务方法，用户名：{username}，密码：{password}")
        self.page_input_username(username)
        self.page_input_password(password)

        self.page_click_login_btn()

    def page_mp_login_article(self, username=13812345678, password=246810):
        '''发布文章业务'''
        log.info(f"正在调用自媒体登录业务方法，用户名：{username}，密码：{password}")
        self.page_input_username(username)
        self.page_input_password(password)

        self.page_click_login_btn()