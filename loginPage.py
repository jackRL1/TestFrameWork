"""
This is the POM for the login Page based on the Page class in page.py
it accesses the webdriver.py file and WebdDriver class to implement the
actual web driver provided by selenium.

The locators are designed to make the process of creating webelements easier
by simplifying the access of elements to a simple find_element_by_locator method.
in this way the locator values only need to be changed in one location and not for
each call of a specific find_element_by... method.

"""

from webDriver import WebDriver
from page import Page

url = "https://www.kimschiller.com/page-object-pattern-tutorial/"

locate = {
    'first': 'id=firstname',
    'last': 'id=lastname',
    'address': 'id=address',
    'zip': 'id=zipcode'
}


class LoginPage(Page):

    def __init__(self):
        self.driver = WebDriver()
        Page.__init__(self, self.driver)
        print('loginPage initiated ')

    # opens url by sending it through to web driver.py which instantiates web driver.Firefox()
    def open(self):
        self.driver.go_to(url)

    """ finds the first name element and input specified text run in the test class """
    def input_first(self, text):
        elem = self.driver.find_element_by_locator(locate['first'])
        self.driver.enter_text(text, elem)

    """ Simply returns the title of the page to test against expected value """
    def get_title(self):
        return self.driver.title()

    """ finds if first name element is present and returns true if it is """
    def first_present(self):
        self.driver.elem_exists(locate['first'])

    """ Closes the web driver instance at the end of the test """
    # def close(self):
    #     self.driver.close()

