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
        arr.append((a.get('title'), a.get('content')))
    return arr


class TestMpArticle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver.get_web_driver(pages.mp_url)
        cls.login = PageIn(cls.driver)
        cls.ar = cls.login.page_get_PageMpArticle()
        log.info("调用登录成功方法")
        cls.login.page_get_PageMpLogin().page_mp_login_article()

    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_web_driver()

    @parameterized.expand(get_data())
    def test_mp_article(self, msg, value):
        self.ar.page_mp_article(msg, value)
        log.info("调用发布文章业务组合方法")
        try:
            log.info("开始断言")
            self.assertEqual(self.ar.page_get_issue_result(), "新增文章成功")
            log.info("断言成功")
        except Exception as e:
            log.error(f'断言失败，错误是{e}')
            self.ar.base_get_screenshot()
            print(e)
            raise
