from selenium import webdriver
from errors import Exceptions


class WebDriver(webdriver.Firefox):

    def __init__(self):
        self.driver = webdriver.Firefox()

    def go_to(self, url):
        self.driver.get(url)

    """ Method for locating and returning elements """
    def find_element_by_locator(self, locate):
        locator_type, loc_value = locate.split('=')
        if locator_type == 'class':
            return self.find_element_by_class_name(loc_value)
        elif locator_type == 'css':
            return self.find_element_by_css_selector(loc_value)
        elif locator_type == 'id':
            return self.find_element_by_id(loc_value)
        elif locator_type == 'link':
            return self.find_element_by_link_text(loc_value)
        elif locator_type == 'name':
            return self.find_element_by_name(loc_value)
        elif locator_type == 'plink':
            return self.find_element_by_partial_link_text(loc_value)
        elif locator_type == 'tag':
            return self.find_element_by_tag_name(loc_value)
        elif locator_type == 'xpath':
            return self.find_element_by_xpath(loc_value)
        else:
            raise Exceptions.BadLocatorValue(locate)

    """ returns the title of the page"""
    def title(self):
        return self.driver.title

    """ return bool of if element exists or not """
    def elem_exists(self, locate):
        try:
            self.find_element_by_locator(locate)
            return True
        except Exceptions.NoSuchElementException(locate):
            return False

    """ returns bool if element is visible or not """
    def visible(self, locate):
        if self.elem_exists(locate):
            if self.find_element_by_locator(locate).is_displayed():
                return True
            else:
                return False
        else:
            return False

    """ returns bool if element is accessible or not """
    def usable(self, locate):
        if self.visible(locate):
            return True
        else:
            return False

    """ Sends text to specific element that is passed """
    def enter_text(self, text, elem):
        elem.send_keys(text)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

