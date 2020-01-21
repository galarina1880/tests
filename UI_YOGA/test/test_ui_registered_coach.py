# -*- coding: utf-8 -*-


def test_ui_coach(app):
    app.open_hp_first_time()
    app.session.fb_driver(username='galarina1666@yandex.ru', password='kuzoid123')
    app.ui_reg.events_menu()
    app.ui_reg.students_menu()
    app.ui_reg.edit_prof()
    app.ui_reg.view_prof()
    app.ui_reg.studios_menu()
    app.ui_reg.partner_menu()
    app.ui_reg.goods()
    app.ui_reg.instr()
    # app.ui_reg.file()
