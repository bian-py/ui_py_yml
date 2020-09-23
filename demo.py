from selenium import webdriver
from time import sleep
import threading


#
# cap = {"browserName": "chrome",
#        "platform": "WINDOWS"
#        }

# cap_chrome = webdriver.DesiredCapabilities.CHROME.copy()
# cap_chrome['platform'] = 'WINDOWS'
#
# driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", cap_chrome)


# driver = webdriver.Edge()

def get_baidu(driver):
    driver.get("http://www.baidu.com")
    sleep(5)
    driver.find_element_by_css_selector("#kw").send_keys("python")
    driver.find_element_by_css_selector("#su").click()
    sleep(3)
    driver.quit()


def get_driver(browser):
    # cap = {"browserName": browser,
    #        "platform": "WINDOWS"
    #        }
    cap = None
    if browser == 'chrome':
        cap = webdriver.DesiredCapabilities.CHROME.copy()
    elif browser == 'edge':
        cap = webdriver.DesiredCapabilities.EDGE.copy()

    cap['platform'] = 'WINDOWS'

    return webdriver.Remote("http://127.0.0.1:4444/wd/hub", cap)


browserName = ['chrome', 'edge']

for a in browserName:
    driver = get_driver(a)
    threading.Thread(target=get_baidu, args=(driver,)).start()
#         同时启动两个线程
