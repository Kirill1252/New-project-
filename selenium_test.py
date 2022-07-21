import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class NewVisitUser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'C:\Users\Петр\Desktop\NewSite\photo_blog\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_homepage_content_for_anonymous_users(self):
        self.browser.get(r'http://127.0.0.1:8000/user/')
        # Checking page elements
        self.assertIn('Welcome', self.browser.title)
        headlines = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertTrue('Welcome to my site!', headlines)
        # element nav
        nav = self.browser.find_elements(By.TAG_NAME, 'nav')
        self.assertTrue(nav)
        nav_element = self.browser.find_elements(By.TAG_NAME, 'a')
        self.assertTrue(nav_element)
        # Link text
        link_text_home = self.browser.find_element(By.LINK_TEXT, 'Home')
        self.assertTrue(link_text_home)
        link_text_courses = self.browser.find_element(By.LINK_TEXT, 'Courses')
        self.assertTrue(link_text_courses)
        link_text_blog = self.browser.find_element(By.LINK_TEXT, 'Blog')
        self.assertTrue(link_text_blog)
        link_text_registration = self.browser.find_element(By.LINK_TEXT, 'Registration')
        self.assertTrue(link_text_registration)
        link_text_login = self.browser.find_element(By.LINK_TEXT, 'Login')
        self.assertTrue(link_text_login)


if __name__ == '__main__':
    unittest.main()
