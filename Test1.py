import unittest
from loginPage import LoginPage
from webDriver import WebDriver


class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver()


    @classmethod
    def tearDownClass(cls):
        cls.driver.tearDown()

    def test_title(self):
        self.assertTrue('Sign up', self.logTest.get_title())


if __name__ == '__main__':
    unittest.main()
