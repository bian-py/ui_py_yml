import pytest

from parameterized import parameterized

import pages
from pages.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_json import ReadJson
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMpLogin:

    @classmethod
    def setup_class(cls):
        # 获取driver对象
        cls.driver = GetDriver().get_web_driver(pages.mp_url)
        # 通过统一入口类获取PageMpLogin对象
        cls.mp = PageIn(cls.driver).page_get_PageMpLogin()

    @classmethod
    def teardown_class(cls):
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("username,password",read_yaml("mp_login.yaml"))
    def test_mp_login(self, username, password):
        self.mp.page_mp_login(username, password)
        try:
            log.info("正在进行断言")
            assert self.mp.page_get_nickname(), username
            log.info("断言正确")
        except Exception as e:
            log.info(f"断言错误，错误信息：{e}")
            print(e)
            self.mp.base_get_screenshot()
            raise
