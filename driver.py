from selenium import webdriver
from elements import Element

""" WebDriver is a subclass of the webdriver superclass. its main function
    at the moment is to return web elements from the Element class in the 
    elements.py file
    
    There are a few other methods for locating or returning true if an element 
    is present or visible or accessible. 

"""


class WebDriver(webdriver.Firefox):
    """ webdriver subclass to return web elements"""

    def __init__(self, **kwargs):
        super(WebDriver, self).__init__(**kwargs)

    """ Method for locating and returning elements """
    def find_element_by_locator(self, locate):
        locator_type, loc_value = locate.split('=')
        if locator_type == 'class':
            return Element(self.find_element_by_class_name(loc_value))
        elif locator_type == 'css':
            return Element(self.find_element_by_css_selector(loc_value))
        elif locator_type == 'id':
            return Element(self.find_element_by_id(loc_value))
        elif locator_type == 'link':
            return Element(self.find_element_by_link_text(loc_value))
        elif locator_type == 'name':
            return Element(self.find_element_by_name(loc_value))
        elif locator_type == 'plink':
            return Element(self.find_element_by_partial_link_text(loc_value))
        elif locator_type == 'tag':
            return Element(self.find_element_by_tag_name(loc_value))
        elif locator_type == 'xpath':
            return Element(self.find_element_by_xpath(loc_value))
        else:
            raise Exception('bad value')

    """ return bool of if element exists or not """
    def elem_exists(self, locate):
        try:
            self.find_element_by_locator(locate)
            return True
        except "No such thang":
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
