"""
This is the POM for the login Page based on the Page class in page.py
it accesses the webdriver.py file and WebdDriver class to implement the
actual web driver provided by selenium.

The locators are designed to make the process of creating webelements easier
by simplifying the access of elements to a simple find_element_by_locator method.
in this way the locator values only need to be changed in one location and not for
each call of a specific find_element_by... method.

"""
from driver import WebDriver as wd


locate = {
    'first': 'id=firstname',
    'last': 'id=lastname',
    'address': 'id=address',
    'zip': 'id=zipcode',
    'submit': 'id=signup'
}


url = "https://www.kimschiller.com/page-object-pattern-tutorial/"


class Page(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element_by_locator(self, locator):
        return self.driver.find_element_by_locator(locator)


class LoginPage(Page):

    # """ finds the first name element and input specified text run in the test class """
    # def input_first(self, text):
    #     elem = self.find_element_by_locator(locate['first'])
    #     wd.enter_text(text, elem)

    """ opens the web browser to the url indicated for the page """
    def open(self):
        return self.driver.get(url)

    """ Simply returns the title of the page to test against expected value """
    def get_title(self):
        return self.driver.title

    """ 
    finds if following elements are present and returns true if it is 
    """
    def first_present(self):
        return self.driver.elem_exists(locate['first'])

    def last_present(self):
        return self.driver.elem_exists(locate['last'])

    def zip_present(self):
        return self.driver.elem_exists(locate['zip'])

    def email_present(self):
        return self.driver.elem_exists(locate['address'])

    """ 
    Enters the appropriate string to the required field. 
    """
    def send_first(self, text):
        elem = locate['first']
        flag = self.driver.enter_text(elem, text)
        return flag

    def send_last(self, text):
        elem = locate['last']
        flag = self.driver.enter_text(elem, text)
        return flag

    def send_zip(self, text):
        elem = locate['zip']
        return self.driver.enter_text(elem, text)

    def send_email(self, text):
        elem = locate['address']
        return self.driver.enter_text(elem, text)

    """ Presses enter on specified button """
    def press_enter(self):
        return self.driver.press_submit(locate['submit'])

    """ Closes the web driver instance at the end of the test """
    def close(self):
        self.driver.close()
