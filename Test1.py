import unittest
import time
from loginPage import LoginPage
from driver import WebDriver

desired_capabilities = {'browserName': 'firefox'}
selenium_grid_url = "http://198.0.0.1:4444/wd/hub"


class Test1(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = WebDriver()
        self.login = LoginPage(self.driver)

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()

    def test_page(self):
        self.login.open()
        self.assertTrue("Sign up", self.login.get_title())
        time.sleep(5)
        first_name = 'Billy'
        self.assertTrue(self.login.send_first(first_name))
        time.sleep(5)
        last_name = 'Smith'
        self.assertTrue(self.login.send_last(last_name))
        time.sleep(5)
        email = 'example@test.com'
        self.assertTrue(self.login.send_email(email))
        time.sleep(5)
        zip_code = '98000'
        self.assertTrue(self.login.send_zip(zip_code))
        time.sleep(7.5)
        self.assertTrue(self.login.press_enter())
        time.sleep(10)

    # def test_title(self):
    #     self.login.open()
    #     self.assertIn("Sign up", self.login.get_title())
    #
    # def test_first(self):
    #     self.login.open()
    #     self.assertTrue(self.login.first_present())
    #     text = 'Billy'
    #     self.assertTrue(self.login.send_first(text))
    #     time.sleep(5)
    #
    # def test_last(self):
    #     self.login.open()
    #     self.assertTrue(self.login.last_present())
    #     text = 'Smith'
    #     self.assertTrue(self.login.send_last(text))
    #     time.sleep(5)
    #
    # def test_zip(self):
    #     self.login.open()
    #     self.assertTrue(self.login.zip_present())
    #     text = 'your momma'
    #     self.assertTrue(self.login.send_zip(text))
    #     time.sleep(5)
    #
    # def test_email(self):
    #     self.login.open()
    #     self.assertTrue(self.login.email_present())
    #     text = 'example@test.com'
    #     self.assertTrue(self.login.send_email(text))
    #     time.sleep(5)
    #
    # def test_button(self):
    #     self.login.open()
    #     self.assertTrue(self.login.press_enter())
    #     time.sleep(10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
