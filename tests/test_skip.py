"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

import pytest
from lesson_15.pages.main_page import MainPage


def test_github_desktop(browser_setup_window):
    if browser_setup_window == 'mobile':
        pytest.skip('this test is not for mobile size browsers')
    main_page = MainPage()
    main_page.open()
    main_page.open_sign_in_page_in_desktop()
    main_page.sign_up_page_should_be_visible_for_desktop()


def test_github_mobile(browser_setup_window):
    if browser_setup_window == 'desktop':
        pytest.skip('this test is not for desktop size browsers')
    main_page = MainPage()
    main_page.open()
    main_page.open_login_page_in_mobile()
    main_page.sign_in_page_should_be_visible_for_mobile()