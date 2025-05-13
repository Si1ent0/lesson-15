from selene import browser, have


class MainPage:
    def open(self):
        browser.open('https://github.com/')
        return self

    def open_sign_in_page_in_desktop(self):
        browser.element('.HeaderMenu-link--sign-up').click()
        return self

    def open_login_page_in_mobile(self):
        browser.element('.HeaderMenu-button.js-prevent-focus-on-mobile-nav').click()
        return self

    def sign_in_page_should_be_visible_for_mobile(self):
        browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
        return self

    def sign_up_page_should_be_visible_for_desktop(self):
        browser.element('.signup-form-fields__h2').should(have.text('Sign up to GitHub'))
        return self
