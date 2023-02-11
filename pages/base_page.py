import time

from pages.constants import ConstantsData as const


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def refresh_page(self):
        self.browser.refresh()

    def screenshot(self, filename):
        self.browser.save_screenshot(f'{const.screen_directory}/{filename}')

    def open_in_new_tab(self, link):
        self.browser.switch_to.new_window("tab")
        self.browser.get(link)
        time.sleep(2)

    def open_in_new_window(self, link):
        self.browser.switch_to.new_window("window")
        self.browser.get(link)
        time.sleep(2)
