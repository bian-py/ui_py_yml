from time import sleep

import pages
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMisAudit(WebBase):
    article_id = None

    def page_mis_click_management(self):
        sleep(1)
        self.base_click(pages.mis_management)

    def page_mis_click_audit_menu(self):
        sleep(1)
        self.base_click(pages.mis_audit_menu)

    def page_mis_input_title(self, title):
        sleep(1)
        self.base_input(pages.mis_title, title)

    def page_mis_input_channel(self, channel):
        sleep(1)
        self.base_input(pages.mis_channel, channel)

    def page_mis_select_status(self, placeholder_text="请选择状态", click_text="待审核"):
        self.web_base_click_element(placeholder_text, click_text)

    def page_mis_click_search_btn(self):
        self.base_click(pages.mis_search)
        sleep(5)

    def page_mis_get_article_id(self):
        return self.base_get_text(pages.mis_id)

    def page_mis_click_pass_btn(self):
        self.base_click(pages.mis_pass_bty)
        sleep(2)

    def page_mis_click_confirm(self):
        self.base_click(pages.mis_confirm)

    def page_mis_audit(self, title, channel):
        log.info("点击信息管理")
        self.page_mis_click_management()
        log.info("点击内容审核")
        self.page_mis_click_audit_menu()
        log.info("输入要搜索的文章标题")
        self.page_mis_input_title(title)
        log.info("输入查询频道")
        self.page_mis_input_channel(channel)
        log.info("选择查询状态")
        self.page_mis_select_status()
        log.info("点击搜索按钮")
        self.page_mis_click_search_btn()
        log.info("开始获取文章ID")
        self.article_id = self.page_mis_get_article_id()
        log.info(f"获取的文章ID是{self.article_id}")
        log.info("点击通过按钮")
        self.page_mis_click_pass_btn()
        log.info("点击确认通过按钮")
        self.page_mis_click_confirm()

    def page_mis_assert(self):
        sleep(3)
        log.info("修改查询状态，为已通过审核")
        self.page_mis_select_status(click_text='审核通过')
        log.info("点击查询按钮")
        self.page_mis_click_search_btn()
        return self.web_base_is_exist(self.article_id)
