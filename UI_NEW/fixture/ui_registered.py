# -*- coding: utf-8 -*-
from model.main_menu import MainMenu


class UIReg:
    def __init__(self, app):
        self.app = app

    #Left menu check
    def events_menu(self):
        MainMenu.events_left_menu(self)

    def students_menu(self):
        MainMenu.students_left_menu(self)

    def edit_prof(self):
        MainMenu.profile_edit(self)

    def view_prof(self):
        MainMenu.profile_view(self)

    def studios_menu(self):
        MainMenu.studios_left_menu(self)



# def check_ev_list(self):
#     request = requests.get('https://api.staging.decathlon.ru/events-service/events/instances?canceled=false&bounds=55.83710572400662,37.741316776891836,55.70903567468666,37.53820702310804&sports=292&date_start=2019-06-17T16:05&date_end=2019-07-17T16:05&time_start=00:00&time_end=23:59&price_min=0&price_max=10000&coaches=&place_id=&size=25&page=0').text
#     return json.loads(request)['content'][0]
#
# def write_first_event(self):
#     wd = self.app.wd
#     res = check_ev_list()
#     ev_id = res['id']
#     ev_slug = res['event']['slug']
#     # time = res['datetime'].split(':')
#     # ev_time = '%3A'.join(time)
#     # zone1 = res['event']['zone']
#     # ev_zone = strftime("%H.%M.%S", zone1)
#     # print(coach_id)
#     wd.get('https://alldoyoga.staging.decathlon.ru/events/{event}_{slug}'.format(event=ev_id, slug=ev_slug))
#     wd.implicitly_wait(60)

# def check_pl_list():
#     request = requests.get('https://api.staging.decathlon.ru/sport-places-service/sport-places/list?bounds=55.79694536427719,37.65819121986726,55.705489031727424,37.57865478013275&sports=&coaches=&size=25&page=0').text
#     return json.loads(request)['content'][0]
#
#
# time.sleep(3)
# res = check_pl_list()
# pl_id = res['id']
# pl_nm = res['slug']
# # print("/sport_places/{place}_{name}".format(place=pl_id, name=pl_nm))
# wd.find_element_by_css_selector('[href="/sport_places/{place}_{name}"]'.format(place=pl_id, name=pl_nm)).click()
# time.sleep(3)
#


# def check_coach_list():
#     request = requests.get('https://api.staging.decathlon.ru/partner-service/partners/profiles?size=24&type=COACH').text
#     return json.loads(request)['content'][0]
#
#
# time.sleep(3)
# res = check_coach_list()
# coach_id = res['id']
# coach_slug = res['slug']
# # print(coach_id)
# wd.find_element_by_css_selector('[href="/coaches/{coach}_{slug}"]'.format(coach=coach_id, slug=coach_slug)).click()
# time.sleep(5)


