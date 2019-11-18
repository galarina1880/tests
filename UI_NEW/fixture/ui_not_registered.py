# -*- coding: utf-8 -*-
from model.main_menu import MainMenu


class UINotReg:

    def __init__(self, app):
        self.app = app

    def all_events_view(self):
        wd = self.app.wd
        MainMenu.all_events(self)

    def all_places_view(self):
        wd = self.app.wd
        MainMenu.place_list(self)

    # Checking coaches view
    def all_coaches_view(self):
        wd = self.app.wd
        MainMenu.coach_list(self)

    # Checking coach request
    def coach_request(self):
        wd = self.app.wd
        MainMenu.become_partner(self)

    def open_coach_form(self):
        MainMenu.become_partner_form(self)

    def open_login_page(self):
        MainMenu.open_login_page(self)

    def close_login_popup(self):
        MainMenu.close_login_popup(self)

    def open_hp(self):
        MainMenu.open_hp(self)
