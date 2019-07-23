from selenium.webdriver.support.ui import WebDriverWait


class SessionHelper:

    def __init__(self, app):
        self.app = app

    # def driver_alt(self, username, password):
    #     wd = self.app.wd
    #     self.app.open_login_pg()
    #     # alt_driver = webdriver.Chrome("C:\\WORK\\PYTHON\\workflow\\chromedriver_win32\\chromedriver.exe")
    #     # alt_driver.maximize_window()
    #     # alt_driver.get('https://decathlon:DecSport@alldoyoga.staging.decathlon.ru/')
    #     # # alt_driver.get('https://alldoyoga.dev.decathlon.ru/')
    #     WebDriverWait(wd, 40).until(lambda x: wd.find_element_by_css_selector('[href="/login"]'))
    #     wd.find_element_by_css_selector('[href="/login"]').click()

    def fb_driver(self, username, password):
        wd = self.app.wd
        wd.implicitly_wait(5)
        # WebDriverWait(fb, 40).until(lambda x: fb.find_element_by_css_selector('[href="#/login"]')).click()
        wd.find_element_by_css_selector('[href="/login"]').click()
        wd.find_element_by_css_selector('[class="linkFB btn btn-secondary mr-2"]').click()
        # wd.find_element_by_css_selector('[id="m_login_email"]').send_keys('galarina1666@yandex.ru')
        # wd.find_element_by_css_selector('[id="m_login_password"]').send_keys('kuzoid123')
        wd.find_element_by_css_selector('[id="m_login_email"]').send_keys(username)
        wd.find_element_by_css_selector('[id="m_login_password"]').send_keys(password)
        wd.find_element_by_css_selector('[id="u_0_5"]').click()
        # fb.find_element_by_css_selector('[id="email"]').send_keys('galarina1666@yandex.ru')
        # fb.find_element_by_css_selector('[id="pass"]').send_keys('kuzoid123')
        # fb.find_element_by_css_selector('[id="loginbutton"]').click()
    #     return fb

    # def vk_driver(self):
    #     vk = webdriver.Chrome("C:\\WORK\\PYTHON\\workflow\\chromedriver_win32\\chromedriver.exe")
    #     vk.maximize_window()
    #     vk.get('https://decathlon:DecSport@alldoyoga.staging.decathlon.ru/')
    #     # vk.get('https://alldoyoga.dev.decathlon.ru/')
    #     time.sleep(3)
    #     # WebDriverWait(fb, 40).until(lambda x: fb.find_element_by_css_selector('[href="#/login"]')).click()
    #     vk.find_element_by_css_selector('[href="/login"]').click()
    #     vk.find_element_by_css_selector('[class="linkVK btn btn-secondary mr-2"]').click()
    #     vk.find_element_by_css_selector('[name="email"]').send_keys('decast666@gmail.com')
    #     vk.find_element_by_css_selector('[name="pass"]').send_keys('kuzoid')
    #     vk.find_element_by_css_selector('[id="install_allow"]').click()
    #     return vk

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
