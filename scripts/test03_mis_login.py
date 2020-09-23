import unittest

from parameterized import parameterized

import pages
from pages.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_json import ReadJson

log = GetLog.get_logger()


def get_data():
    data = ReadJson.read_json('mis_login.json')
    arr = []
    for a in data.values():
        arr.append((a.get('username'), a.get('password')))
    return arr


class TestMisLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 获取driver对象
        cls.driver = GetDriver().get_web_driver(pages.mis_url)
        # 通过统一入口类获取PageMpLogin对象
        cls.mis = PageIn(cls.driver).page_get_PageMisLogin()

    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_web_driver()

    @parameterized.expand(get_data())
    def test_mis_login(self, username, password):
        self.mis.page_mis_login(username, password)
        try:
            log.info("正在进行断言")
            # 断言中判断昵称中是否包含管理员
            self.assertIn('管理员', self.mis.page_mis_get_nick_name())
            # self.assertEqual(self.mis.page_mis_get_nick_name(), "欢迎 管理员")
            log.info("断言正确")
        except Exception as e:
            log.info(f"断言错误，错误信息：{e}")
            print(e)
            self.mis.base_get_screenshot()
            raise
