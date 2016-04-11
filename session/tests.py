from unittest import TestCase

# Create your tests here.
from selenium import webdriver

class SessionFunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        self.browser.get('http://localhost:8000')
        self.login()
        self.logout()

    def login(self):
        login_option = self.browser.find_element_by_id('id_login')
        login_option.click()
        self.browser.implicitly_wait(5)
        name = self.browser.find_element_by_id('username')
        name.send_keys('admin')
        last_name = self.browser.find_element_by_id('password')
        last_name.send_keys('administrador')
        login_button = self.browser.find_element_by_id('id_button_login')
        login_button.click()

    def logout(self):
        self.browser.implicitly_wait(8)
        logout_option = self.browser.find_element_by_id('id_option_logout')

        # Check if logout option is enabled
        self.assertIsNotNone(logout_option)

        logout_option.click()
        self.browser.implicitly_wait(8)

