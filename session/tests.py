import random
import string
from unittest import TestCase

# Create your tests here.
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SessionFunctionalTest(TestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        name = self.browser.find_element_by_id('username')
        name.send_keys('admin')

        last_name = self.browser.find_element_by_id('password')
        last_name.send_keys('administrador')

        self.browser.implicitly_wait(5)

        self.assertIsNotNone(self.browser.find_element_by_link_text('admin'))

