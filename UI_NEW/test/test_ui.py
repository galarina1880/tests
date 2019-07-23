# -*- coding: utf-8 -*-


def test_ui_not_registered(app):
    app.open_login_pg()
    app.ui.all_events_view()
    app.ui.all_places_view()
    app.ui.all_coaches_view()
    app.ui.coach_request()
    app.session.logout()
