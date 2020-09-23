'''以下数据为自媒体模块登录配置数据'''
# 用户名
from selenium.webdriver.common.by import By

mp_username = By.CSS_SELECTOR, '[placeholder="请输入手机号"]'
# 验证码
mp_password = By.CSS_SELECTOR, '[placeholder="验证码"]'
# 登录按钮
mp_btn = By.CSS_SELECTOR, ".el-button--primary"
# 昵称
mp_usernickname = By.CSS_SELECTOR, ".user-name"

"""URL配置信息"""
mp_url = 'http://ttmp.research.itcast.cn/#/login'
mis_url = 'http://ttmis.research.itcast.cn/#/'

'''以下数据为自媒体模块发布文章配置数据'''
# 点击元素的父节点，一般不点击文字
mp_content_manage = By.XPATH, "//span[text()='内容管理']/.."
mp_issue_article = By.XPATH, "//*[contains(text(),'发布文章')]"
mp_title = By.CSS_SELECTOR, '[placeholder="文章名称"]'

mp_article_frame = By.CSS_SELECTOR, '#publishTinymce_ifr'
# 表单内容定位到body
mp_artile = By.CSS_SELECTOR, '#tinymce'

mp_bookface = By.XPATH, "//span[text()='自动']"
mp_issue_btn = By.XPATH, "//span[text()='发表']/.."
mp_result = By.XPATH, "//*[contains(text(),'新增文章成功')]"

'''以下数据是后台管理模块的登录配置数据'''
mis_username = By.CSS_SELECTOR, '[placeholder="用户名"]'
mis_pwd = By.CSS_SELECTOR, '[placeholder="密码"]'
mis_login_btn = By.CSS_SELECTOR, '#inp1'
mis_nickname = By.CSS_SELECTOR, '.user_info'
'''以下数据是后台管理模块的文章审核配置数据'''
mis_management = By.XPATH, "//*[text()='信息管理']/."
mis_audit_menu = By.XPATH, "//*[text()='内容审核']/."
mis_title = By.CSS_SELECTOR, '[placeholder="请输入: 文章名称"]'
mis_channel = By.CSS_SELECTOR, '[placeholder="请输入: 频道"]'
mis_search = By.CSS_SELECTOR, ".find"
mis_id = By.CSS_SELECTOR, ".cell>span"
mis_pass_bty = By.XPATH, "//*[text()='通过']/.."
mis_confirm = By.CSS_SELECTOR, ".el-button--primary "
'''以下是app应用元素配置信息'''
app_username = By.XPATH, "//*[@index='1' and @class='android.widget.EditText']"
app_pwd = By.XPATH, "//*[@index='2' and @class='android.widget.EditText']"
app_login_btn = By.XPATH, "//*[@text='登录' and @class='android.widget.Button']"
app_me = By.XPATH, "//*[@index=3 and contains(@text,'我的')]"

app_package = 'com.itcast.toutiaoApp'
app_activity = '.MainActivity'
'''以下是app应用查找文章配置信息'''
app_el_area = By.XPATH, "//*[@class='android.widget.HorizontalScrollView']"
app_article_area = By.XPATH,"//*[@index='2' and @bounds='[0,196][540,858]']"
