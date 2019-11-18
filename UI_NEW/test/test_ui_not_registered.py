# -*- coding: utf-8 -*-
from model.main_menu import MainMenu


def test_ui_not_registered(app):
    app.open_hp_first_time()
    app.ui.all_events_view()
    app.ui.all_places_view()
    app.ui.all_coaches_view()
    app.ui.coach_request()
    app.ui.close_login_popup()
    app.ui.open_login_page()
    app.ui.open_hp()
