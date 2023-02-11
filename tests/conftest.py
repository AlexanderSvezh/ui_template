import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.constants import ConstantsData as const
from helpers.helper import create_screen_dir


@pytest.fixture()
def browser(headless=False):
    create_screen_dir()

    option = webdriver.ChromeOptions()
    option.add_argument('--no-proxy-server')
    option.add_argument('--no-sandbox')
    option.add_argument("window-size=1920,1080")
    option.add_argument('--start-maximized')
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--disable-infobars')
    option.add_argument('--disable-gpu')
    option.add_argument("--disable-extensions")
    option.add_argument('--disable-web-security')

    if headless:
        option.add_argument("--headless")

    service = Service(const.chromedriver_path)
    browser = webdriver.Chrome(service=service, options=option)

    yield browser
    browser.quit()
