import unittest

from parameterized import parameterized

import pages
from pages.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_json import ReadJson

log = GetLog.get_logger()


def get_data():
    data = ReadJson.read_json('mp_article.json')
    arr = []
    for a in data.values():
        arr.append((a.get('title'), a.get('channel')))
    return arr


class TestMisAudit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = GetDriver.get_web_driver(pages.mis_url)
        cls.pagein = PageIn(driver)
        log.info("调用后台系统登录成功方法")
        cls.pagein.page_get_PageMisLogin().page_mis_login_success()
        cls.au = cls.pagein.page_get_PageMisAudit()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver.quit_web_driver()

    @parameterized.expand(get_data())
    def test_mis_audit(self, title="BBB99904", channel="数据库"):
        log.info("调用审核文章的组合业务方法")
        self.au.page_mis_audit(title, channel)
        print(self.au.article_id)
        log.info("断言开始")
        try:
            self.assertTrue(self.au.page_mis_assert())
            log.info("断言正确")
        except Exception as e:
            log.error("断言错误，正在截图")
            self.au.base_get_screenshot()
            raise
