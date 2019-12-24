# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.ui_not_registered import UINotReg
from fixture.ui_registered import UIReg
from fixture.files import FileHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.ui = UINotReg(self)
        self.ui_reg = UIReg(self)
        # self.file = FileHelper(self)

    def open_hp_first_time(self):
        wd = self.wd
        # wd.maximize_window()
        wd.get('https://decathlon:DecSport@alldoyoga.staging.decathlon.ru/')
        # wd.get('https://decathlon:DecSport@alldoyoga.dev.decathlon.ru/')

    def destroy(self):
        self.wd.quit()
