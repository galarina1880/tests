from selenium import webdriver
from fixture.session import SessionHelper
from fixture.ui_not_registered import UINotReg
# from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.ui = UINotReg(self)

    def open_login_pg(self):
        wd = self.wd
        wd.maximize_window()
        wd.get('https://decathlon:DecSport@alldoyoga.staging.decathlon.ru/')
        # wd.get('https://decathlon:DecSport@alldoyoga.dev.decathlon.ru/')

    def destroy(self):
        self.wd.quit()
