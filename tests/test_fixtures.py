"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

from lesson_15.pages.main_page import MainPage


def test_github_desktop(desktop_setup):
    main_page = MainPage()
    main_page.open()
    main_page.open_sign_in_page_in_desktop()
    main_page.sign_up_page_should_be_visible_for_desktop()


def test_github_mobile(mobile_setup):
    main_page = MainPage()
    main_page.open()
    main_page.open_login_page_in_mobile()
    main_page.sign_in_page_should_be_visible_for_mobile()