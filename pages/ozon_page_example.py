from .base_page import BasePage

from pages.constants import ConstantsData as const


class OzonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser, const.ozon_url)
