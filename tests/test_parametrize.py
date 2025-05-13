"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""

import pytest
from lesson_15.pages.main_page import MainPage


@pytest.mark.parametrize("browser_setup", ['desktop'], indirect=True)
def test_github_desktop(browser_setup):
    main_page = MainPage()
    main_page.open()
    main_page.open_sign_in_page_in_desktop()
    main_page.sign_up_page_should_be_visible_for_desktop()


@pytest.mark.parametrize("browser_setup", ['mobile'], indirect=True)
def test_github_mobile(browser_setup):
    main_page = MainPage()
    main_page.open()
    main_page.open_login_page_in_mobile()
    main_page.sign_in_page_should_be_visible_for_mobile()