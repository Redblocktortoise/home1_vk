import time

import pytest
from selenium.webdriver.common.by import By

from base import BaseCase
from ui.locators import basic_locators


class TestExample(BaseCase):

    @pytest.mark.UI()
    def test_foo(self):
        url = 1
        assert url == 1

    @pytest.mark.UI()
    def test_login(self):
        self.try_login()
        self.driver.implicitly_wait(10)
        url = self.driver.current_url
        assert url == "https://target.my.com/dashboard"

    @pytest.mark.UI()
    def test_logout(self):
        self.try_login()
        # self.driver.implicitly_wait(10)
        self.try_logout()
        self.driver.implicitly_wait(5)
        url = self.driver.current_url
        assert url == "https://target.my.com/"

    @pytest.mark.UI()
    def test_edit_profile(self):
        self.try_login()
        self.driver.implicitly_wait(5)
        name_title = self.try_edit_profile()
        assert name_title == 'Имя Фамилия'

    @pytest.mark.UI()
    @pytest.mark.parametrize(
        "locator, link",
        [
            (
                (By.XPATH, '//*[@class="center-module-button-14O4yB center-module-segments-1MqckW"]'),
                'https://target.my.com/segments/segments_list'
            ),
            (
                (By.XPATH, '//*[@class="center-module-button-14O4yB center-module-profile-1kuUOa"]'),
                'https://target.my.com/profile/contacts'
            ),
            (
                (By.XPATH, '//*[@class="center-module-button-14O4yB center-module-statistics-2Wbrwh"]'),
                'https://target.my.com/statistics/summary'
            )
        ]
    )
    def test_link_follow(self,  locator, link):
        self.try_login()
        self.driver.implicitly_wait(5)
        url = self.try_follow(locator)
        assert url == link




