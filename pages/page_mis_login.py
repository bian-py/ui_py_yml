import pages
from base.web_base import WebBase
from tools.get_log import GetLog

log =GetLog.get_logger()
class PageMisLogin(WebBase):
    def page_mis_input_username(self, username):
        self.base_input(pages.mis_username, username)

    def page_mis_input_password(self, password):
        self.base_input(pages.mis_pwd, password)

    def page_mis_click_login_btn(self):
        # 处理js,使按钮可用
        js = 'document.getElementById("inp1").disabled = false'
        self.driver.execute_script(js)
        self.base_click(pages.mis_login_btn)

    def page_mis_get_nick_name(self):
        return self.base_get_text(pages.mis_nickname)

    def page_mis_login(self, username, password):
        log.info(f"输入用户名{username}")
        self.page_mis_input_username(username)
        log.info(f"输入密码{password}")
        self.page_mis_input_password(password)
        log.info("点击登录按钮")
        self.page_mis_click_login_btn()

    def page_mis_login_success(self, username="testid", password='testpwd123'):
        log.info(f"输入用户名{username}")
        self.page_mis_input_username(username)
        log.info(f"输入密码{password}")
        self.page_mis_input_password(password)
        log.info("点击登录按钮")
        self.page_mis_click_login_btn()
