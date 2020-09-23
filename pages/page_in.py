from base.base import Base
from pages.page_app_article import PageAppArticle
from pages.page_app_login import PageAppLogin
from pages.page_mis_audit import PageMisAudit
from pages.page_mis_login import PageMisLogin
from pages.page_mp_article import PageMpArticle
from pages.page_mp_login import PageMpLogin


class PageIn(Base):
    def __init__(self, driver):
        self.driver = driver

    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)

    def page_get_PageMisLogin(self):
        return PageMisLogin(self.driver)

    def page_get_PageMisAudit(self):
        return PageMisAudit(self.driver)

    def page_get_PageAppLogin(self):
        return PageAppLogin(self.driver)
    def page_get_PageAppArticle(self):
        return PageAppArticle(self.driver)
