import unittest

from parameterized import parameterized

from pages.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_json import ReadJson

log = GetLog.get_logger()


def get_data():
    arr = list()
    data = ReadJson.read_json("app_article.json")
    for a in data.values():
        arr.append((a.get("channel"), a.get("title")))
    print(arr)
    return arr


class TestAppArticle(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver.get_app_driver()
        cls.pagein = PageIn(cls.driver)
        cls.pagein.page_get_PageAppLogin().page_app_login_success(cls.driver)
        cls.ar = cls.pagein.page_get_PageAppArticle()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver.quit_app_driver()

    @parameterized.expand(get_data())
    def test_app_article(self, click_channel="python", click_title='Python'):
        try:
            self.ar.page_app_article(click_channel, click_title)
        except Exception as e:
            log.error(e)
            self.ar.base_get_screenshot()
            raise
