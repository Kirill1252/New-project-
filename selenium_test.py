from selenium import webdriver
import unittest


class NewVisitUser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'C:\Users\Петр\Desktop\NewSite\photo_blog\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_homepage_content_for_anonymous_users(self):
        self.browser.get(r'http://127.0.0.1:8000/user/')
        self.assertIn('Welcome', self.browser.title)



if __name__ == '__main__':
    unittest.main()