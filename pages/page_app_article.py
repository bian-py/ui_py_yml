import pages
from base.app_base import AppBase
from tools.get_log import GetLog

log = GetLog.get_logger()
class PageAppArticle(AppBase):

    def page_app_find_channel(self, click_channel):
        self.app_base_right_swipe_left(pages.app_el_area, click_channel)

    def page_app_find_article(self, click_title):
        self.app_base_down_swipe_up(pages.app_article_area, click_title)

    def page_app_article(self, click_channel, click_title):
        log.info("正在调用查询频道方法")
        self.page_app_find_channel(click_channel)
        log.info("正在调用查询文章方法")
        self.page_app_find_article(click_title)
