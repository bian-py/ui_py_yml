'''验证el.is_displayed返回值情况'''
# from time import sleep
#
# import pages
# import base.app_base
# from base.base import Base
# from pages.page_app_login import PageAppLogin
# from pages.page_in import PageIn
# from tools.get_driver import GetDriver

#
# driver = GetDriver.get_web_driver(pages.mp_url)
# ll = PageIn(driver).page_get_PageMpLogin()
# ll.page_mp_login_article()
# el = ll.base_get_element(pages.mp_issue_article)
# print(el)
# print(el.is_displayed())
# ll.base_click(pages.mp_content_manage)
# print(el)
# print(el.is_displayed())
# GetDriver.quit_web_driver()
'''验证循环输入方法'''
# def input(msg, driver):
#     for a in msg:
#         key = int(a) + 7
#         driver.press_keycode(key)
#
#     driver = GetDriver.get_app_driver()
#     print(driver)
#     el = Base(driver).base_get_element(pages.app_username)
#     el.click()
#     sleep(2)
#     msg = "13812345678"
#     input(msg, driver)
#     sleep(5)
#     GetDriver.quit_app_driver()
'''验证滑动方法'''
# driver = GetDriver.get_app_driver()
# PageAppLogin(driver).page_app_login_success(driver)
# base.app_base.AppBase(driver).app_base_down_swipe_up(pages.app_article_area, "kkkk")
'''验证列表拼接'''
list = [1, 2, 3]
list2 = [2, 3, 4]
list.extend(list2)
print(list)
