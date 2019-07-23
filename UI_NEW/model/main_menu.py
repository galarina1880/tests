# -*- coding: utf-8 -*-
class MainMenu:

    def __init__(self, app):
        self.app = app

    def login(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/login"]').click()
        # login = '[href="/login"]'

    def all_events(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/events"]').click()
        # all_events = '[href="/events"]'

    def my_events(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/my_events"]').click()
        # my_events = '[href="/my_events"]'

    def partner_events(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/partner/events"]').click()
        # partner_events = '[href="/partner/events"]'

    def place_list(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[class="menu_desktop_level1_label"]').click()
        # place_list = '[href="/sport_places"]'

    def coach_list(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/coaches"]').click()
        # coach_list = '[href="/coaches"]'

    def become_partner(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/become_partner"]').click()
        # become_partner = '[href="/become_partner"]'

    def become_partner_form(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/become_partner/coach"]').click()
        # become_partner_form = '[href="/become_partner/coach"]'

    def dashboard(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/partner/"]').click()
        # dashboard = '[href="/partner/"]'

    def partner_prof(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/partner/profile"]').click()
        # partner_prof = '[href="/partner/profile"]'

    def partner_catalog(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/partner/catalog/231423?page=0&sort=review.count,desc"]').click()
        # partner_catalog = '[href="/partner/catalog/231423?page=0&sort=review.count,desc"]'

    def analytics(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/partner/statistics"]').click()
        # analytics = '[href="/partner/statistics"]'

    def profile(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/profile"]').click()
        # profile = '[href="/profile"]'

    def traffic(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/partner/my_indicators"]').click()
        # traffic = '[href="/partner/my_indicators"]'

    def finance(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/partner/finance"]').click()
        # finance = '[href="/partner/finance"]'
