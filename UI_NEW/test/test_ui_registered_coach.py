# -*- coding: utf-8 -*-


def test_ui_not_registered(app):
    app.open_hp_first_time()
    app.ui.open_login_page()
