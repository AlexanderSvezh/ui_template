import os

from pages.constants import ConstantsData as const


def create_screen_dir():
    is_exist = os.path.exists(const.screen_directory)
    if not is_exist:
        os.makedirs(const.screen_directory)
