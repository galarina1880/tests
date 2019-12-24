# -*- coding: utf-8 -*-
import os
from model.main_menu import MainMenu

class FileHelper:
    def file(self):
        os.system(r'nul>UI_Output.txt')
        my_file = open('UI_Output.txt', 'a')
        my_file.write('Events list available, first event data: \n\n' + str(MainMenu.events_left_menu(self)) + '\n\n')
        # my_file.write('Places list available, first place data: \n\n' + str(check_pl_list()) + '\n\n')
        # my_file.write('Coaches list available, first coach data: \n\n' + str(check_coach_list()) + '\n\n')
        my_file.close()
