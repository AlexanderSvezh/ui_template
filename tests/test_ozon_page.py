import pytest
import time

from pages.ozon_page_example import OzonPage


@pytest.mark.first
def test_ozon_open(browser):
    page = OzonPage(browser)
    page.open()
    assert 'OZON' in browser.title
    page.screenshot('ozon_open_1.png')


def test_ozon_refresh(browser):
    page = OzonPage(browser)
    page.open()
    assert 'OZON' in browser.title
    page.screenshot('ozon_open_2.png')

    page.refresh_page()
    page.screenshot('ozon_after_refresh.png')


def test_ozon_change_tab(browser):
    page = OzonPage(browser)
    page.open()
    assert 'OZON' in browser.title
    page.screenshot('ozon_open_3.png')

    page.open_in_new_tab(link='http://ya.ru')
    page.screenshot('ozon_new_tab_3.png')


def test_ozon_change_window(browser):
    page = OzonPage(browser)
    page.open()
    assert 'OZON' in browser.title
    page.screenshot('ozon_open_4.png')

    page.open_in_new_window(link='http://ya.ru')
    time.sleep(3)
    page.screenshot('ozon_new_window_4.png')
