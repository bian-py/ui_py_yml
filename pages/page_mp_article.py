from time import sleep

import pages
from base.web_base import WebBase
from pages.page_mp_login import PageMpLogin
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMpArticle(WebBase):

    def page_click_content_management(self):
        sleep(3)
        log.info("点击内容管理")
        self.base_click(pages.mp_content_manage)
        sleep(1)

    def page_click_issue_article(self):
        log.info("点击发布文章")
        self.base_click(pages.mp_issue_article)
        sleep(1)

    def page_input_article_title(self, msg):
        log.info(f"输入文章标题：{msg}")
        self.base_input(pages.mp_title, msg)
        sleep(1)

    def page_input_article(self, value):
        log.info("切换表单")
        self.driver.switch_to.frame(self.base_get_element(pages.mp_article_frame))
        sleep(1)
        log.info("输入文章内容")
        self.base_input(pages.mp_artile, value)
        log.info("切换回原始目录")
        self.driver.switch_to.default_content()
        sleep(1)

    def page_select_bookface(self):
        log.info("选择文章页面图片")
        self.base_click(pages.mp_bookface)
        sleep(1)

    def page_select_issue_channel(self):
        self.web_base_click_element(placeholder_text='请选择', click_text='数据库')
        sleep(1)

    def page_click_issue_btn(self):
        log.info("点击发布按钮")
        self.base_click(pages.mp_issue_btn)
        sleep(1)

    def page_get_issue_result(self):
        log.info("获取发布结果")
        sleep(1)
        return self.base_get_text(pages.mp_result)

    def page_mp_article(self, msg, value):
        # PageMpLogin.page_mp_login_article()
        if not self.base_get_element(pages.mp_issue_article).is_displayed():
            self.page_click_content_management()

        self.page_click_issue_article()
        self.page_input_article_title(msg)
        self.page_input_article(value)
        self.page_select_bookface()
        self.page_select_issue_channel()
        self.page_click_issue_btn()
