# -*- coding: utf-8 -*-
import time


class MainMenu:

    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        wd = self.app.wd
        time.sleep(10)
        wd.find_element_by_css_selector('[href="/login"]').click()
        time.sleep(10)
        # login = '[href="/login"]'

    def open_hp(self):
        wd = self.app.wd
        time.sleep(10)
        wd.find_element_by_css_selector('[href="/"]').click()
        time.sleep(10)

    def all_events(self):
        wd = self.app.wd
        time.sleep(10)
        all_events = wd.find_element_by_css_selector('[href="/events"]')
        all_events.click()
        # time.sleep(10)

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
        time.sleep(10)
        all_places = wd.find_element_by_css_selector('[href="/sport_places"]')
        all_places.click()
        # time.sleep(10)

    def coach_list(self):
        wd = self.app.wd
        time.sleep(10)
        all_coaches = wd.find_element_by_css_selector('[href="/coaches"]')
        all_coaches.click()
        # time.sleep(10)
        # coach_list = '[href="/coaches"]'

    def become_partner(self):
        wd = self.app.wd
        time.sleep(10)
        become_coach = wd.find_element_by_css_selector('[href="/become_partner"]')
        become_coach.click()
        time.sleep(10)
        form = wd.find_element_by_css_selector('[class="custom-btn__btn"]')
        form.click()
        # become_partner = '[href="/become_partner"]'

    def close_login_popup(self):
        wd = self.app.wd
        time.sleep(10)
        close = wd.find_element_by_css_selector('[class="dialogClose float-right"]')
        close.click()
        # become_partner_form = '[href="/become_partner/coach"]'

    # Menu for logged user/coach
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
