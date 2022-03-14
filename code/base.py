import time

import pytest
from ui.locators import basic_locators
from selenium.common.exceptions import StaleElementReferenceException


CLICK_RETRY = 3


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    @pytest.fixture()
    def get_url(self, driver):
        return driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def get_login(self):
        return 'osandre97@gmail.com'

    def get_password(self):
        return '1234qwer'

    def get_name(self):
        return 'Андрей Петров'

    def try_login(self):
        login_button = self.find(basic_locators.LOGIN_LOCATOR)
        login_button.click()
        login1 = self.find(basic_locators.INPUT1_LOCATOR)
        login1.send_keys(self.get_login())
        self.driver.implicitly_wait(2)
        password = self.find(basic_locators.INPUT2_LOCATOR)
        password.send_keys(self.get_password())
        self.driver.implicitly_wait(2)
        login_button2 = self.find(basic_locators.LOGIN_BUTTON_LOCATOR)
        login_button2.click()

    def try_logout(self):
        self.driver.implicitly_wait(10)
        menu_button = self.find(basic_locators.MENU_BUTTON_LOCATOR)
        menu_button.click()
        self.driver.implicitly_wait(10)
        logout_button = self.find(basic_locators.LOGOUT_BUTTON_LOCATOR)
        logout_button.click()

    def try_edit_profile(self):
        profile_button = self.find(basic_locators.PROFILE_BUTTON_LOCATOR)
        profile_button.click()
        self.driver.implicitly_wait(5)
        input_str = self.find(basic_locators.INPUT_LOCATOR)
        input_str.clear()
        input_str.send_keys(self.get_name)
        self.driver.implicitly_wait(5)
        safe_button = self.find(basic_locators.SAFE_BUTTON_LOCATOR)
        safe_button.click()
        self.driver.implicitly_wait(5)
        main_button = self.find(basic_locators.MAIN_BUTTON_LOCATOR)
        main_button.click()
        self.driver.implicitly_wait(5)
        name = self.find(basic_locators.NAME_LOCATOR)
        name_title = name.get_attribute('title')
        return name_title

    def try_follow(self, locator):
        self.driver.implicitly_wait(5)
        button = self.find(locator)
        button.click()
        self.driver.implicitly_wait(5)
        url = self.driver.current_url
        return url

    def click(self, locator):
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator)
                # if i < 2:
                #     self.driver.refresh()
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise


