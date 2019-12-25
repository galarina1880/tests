# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.keys import Keys


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

    # Menu for logged manager/coach/user
    def manager(self):
        wd = self.app.wd
        time.sleep(5)
        wd.find_element_by_css_selector('[href="/partner/club/"]').click()
        time.sleep(5)

    def events_man_left_menu(self):
        wd = self.app.wd
        time.sleep(10)
        events = wd.find_elements_by_css_selector('[class="menu-link"]')
        events[0].click()
        time.sleep(5)

    # def coaches_man_left_menu(self):
    #     wd = self.app.wd
    #     time.sleep(10)
    #     coaches = wd.find_elements_by_css_selector('[class="menu-link"]')
    #     coaches[1].click()
    #     time.sleep(5)

    def studios_man_left_menu(self):
        wd = self.app.wd
        time.sleep(10)
        studios = wd.find_elements_by_css_selector('[class="menu-link"]')
        studios[1].click()
        time.sleep(5)

    def students_man_left_menu(self):
        wd = self.app.wd
        time.sleep(10)
        students = wd.find_elements_by_css_selector('[class="menu-link"]')
        students[2].click()
        # students = wd.find_element_by_css_selector('[class="menu-link router-link-exact-active router-link-active"]')
        # students.click()
        time.sleep(15)

    def dashboard(self):
        wd = self.app.wd
        time.sleep(5)
        wd.find_element_by_css_selector('[href="/partner/"]').click()
        # dashboard = '[href="/partner/"]'

    def events_left_menu(self):
        wd = self.app.wd
        time.sleep(10)
        events = wd.find_elements_by_css_selector('[class="menu-link"]')
        events[0].click()
        time.sleep(5)
        # events[[""0""].'/partner/events'].click()
        # return events
        # events[0].click()

    def students_left_menu(self):
        wd = self.app.wd
        time.sleep(10)
        wd.find_element_by_css_selector('[href="/partner/students"]')
        # students = wd.find_elements_by_css_selector('[class="menu-link"]')
        # students[1].click()
        time.sleep(5)

    def profile_edit(self):
        wd = self.app.wd
        time.sleep(10)
        prof_edit = wd.find_elements_by_css_selector('[class="menu-link"]')
        prof_edit[2].click()
        time.sleep(5)

    def profile_view(self):
        wd = self.app.wd
        time.sleep(10)
        view_prof = wd.find_elements_by_css_selector('[class="menu-link"]')
        view_prof[3].click()
        back = wd.find_element_by_link_text('На предыдущую страницу')
        back.click()
        time.sleep(5)

    def studios_left_menu(self):
        wd = self.app.wd
        time.sleep(10)
        stud = wd.find_elements_by_css_selector('[class="menu-link"]')
        stud[4].click()
        time.sleep(5)

    def partn_left_menu(self):
        wd = self.app.wd
        time.sleep(10)
        stud = wd.find_elements_by_css_selector('[class="menu-link"]')
        stud[5].click()
        time.sleep(5)

    def goods_left_menu(self):
        wd = self.app.wd
        time.sleep(10)
        goods = wd.find_elements_by_css_selector('[class="menu-link"]')
        goods[6].click()
        time.sleep(5)

    def instr(self):
        wd = self.app.wd
        time.sleep(10)
        wd.find_element_by_css_selector('[href="/partner/how_to_use"]')
        # instr = wd.find_elements_by_css_selector('[class="menu-link"]')
        # instr[7].click()
        time.sleep(5)

    def events_dashboard(self):
        wd = self.app.wd
        time.sleep(5)
        events = wd.find_element_by_link_text('Перейти к управлению событиями')
        events.click()
        time.sleep(5)
        # partner_events = '[href="/partner/events"]'

    # def partner_prof(self):
    #     wd = self.app.wd
    #     wd.find_element_by_css_selector('[href="/partner/profile"]').click()
    #     # partner_prof = '[href="/partner/profile"]'
    #
    # def partner_catalog(self):
    #     wd = self.app.wd
    #     wd.find_element_by_css_selector('[href="/partner/catalog/231423?page=0&sort=review.count,desc"]').click()
    #     # partner_catalog = '[href="/partner/catalog/231423?page=0&sort=review.count,desc"]'
    #
    # def analytics(self):
    #     wd = self.app.wd
    #     wd.find_element_by_css_selector('[href="/partner/statistics"]').click()
    #     # analytics = '[href="/partner/statistics"]'
    #
    # def profile(self):
    #     wd = self.app.wd
    #     wd.find_element_by_css_selector('[href="/profile"]').click()
    #     # profile = '[href="/profile"]'
    #
    # def traffic(self):
    #     wd = self.app.wd
    #     wd.find_element_by_css_selector('[href="/partner/my_indicators"]').click()
    #     # traffic = '[href="/partner/my_indicators"]'
    #
    # def finance(self):
    #     wd = self.app.wd
    #     wd.find_element_by_css_selector('[href="/partner/finance"]').click()
    #     # finance = '[href="/partner/finance"]'

    def my_events(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="/my_events"]').click()
        # my_events = '[href="/my_events"]'

    # Footer links
    def footer_event(self):
        wd = self.app.wd
        time.sleep(10)
        wd.find_element_by_link_text('Записаться на занятие').click()

    def footer_terms(self):
        wd = self.app.wd
        time.sleep(10)
        terms = wd.find_element_by_css_selector('[href="/terms"]')
        wd.execute_script('arguments[0].scrollIntoView(true);', terms)
        terms.click()
