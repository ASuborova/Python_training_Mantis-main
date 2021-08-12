from selenium import webdriver
from fixture.sessionhelper import SessionHelper
from fixture.progecthelper import ProgectHelper
from generator.progect import GeneratorProgect


class Application:
    def __init__(self, browser, BUrl):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unknown browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.ses_h = SessionHelper(self)
        self.pog_h = ProgectHelper(self)
        self.gen = GeneratorProgect(self)
        self.BUrl = BUrl

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        # home page
        wd.get(self.BUrl)

    def district(self):
        self.wd.quit()
