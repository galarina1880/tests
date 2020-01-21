# -*- coding: utf-8 -*-


def test_ui_manager(app):
    app.open_hp_first_time()
    app.session.fb_driver(username='galarina1666@yandex.ru', password='kuzoid123')
    app.ui_reg.man_dashboard()
    app.ui_reg.man_events()
    # app.ui_reg.man_coaches()
    app.ui_reg.man_studios()
    app.ui_reg.man_students()
