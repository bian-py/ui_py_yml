import unittest

from parameterized import parameterized

from pages.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_json import ReadJson

log = GetLog.get_logger()


def get_data():
    arr = list()
    data = ReadJson.read_json("app_login.json")
    for a in data.values():
        arr.append((a.get("username"), a.get("password")))
    return arr


class TestAppLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver.get_app_driver()
        cls.app_login = PageIn(cls.driver).page_get_PageAppLogin()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver.quit_app_driver()

    @parameterized.expand(get_data())
    def test_app_login(self, msg, pwd):
        log.info("开始调用app登录组合业务")
        self.app_login.page_app_login(self.driver, msg, pwd)
        try:
            log.info("开始进行断言")
            self.assertTrue(self.app_login.page_app_login_is_success())
            log.info("断言成功")
        except Exception as e:
            log.error(f"断言失败，错误信息如下{e}")
            print(e)
            self.app_login.base_get_screenshot()
            raise
