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
    
    """ Method for locating and returning a list of elements """
    def find_elements_by_locator(self, locate):
        locate_type, locate_value = locate.split('=')
        if locate_type == 'class':
            elements = self.find_elements_by_class_name(locate_value)
        elif locate_type == 'css':
            elements = self.find_elements_by_css_selector(locate_value)
        elif locate_type == 'id':
            elements = self.find_elements_by_id(locate_value)
        elif locate_type == 'link':
            elements = self.find_elements_by_link_text(locate_value)
        elif locate_type == 'name':
            elements = self.find_elements_by_name(locate_value)
        elif locate_type == 'plink':
            elements = self.find_elements_by_partial_link_text(locate_value)
        elif locate_type == 'tag':
            elements = self.find_elements_by_tag_name(locate_value)
        elif locate_type == 'xpath':
            elements = self.find_elements_by_xpath(locate_value)
        else:
            raise Exception('Bad Locator value')
        """ returns a list of elements have been found. """
        return [Element(e) for e in elements]            
            
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

    """ 
        Sends String to specific element that is passed 
        Then returns true if sucessful 
    """
    def enter_text(self, elem, text):
        try:
            e = self.find_element_by_locator(elem)
            e.send_keys(text)
            return True
        except "nope not happening":
            return False
    
    """ Simply to press button objects """
    def press_submit(self, text):
        try:
            elem = self.find_element_by_locator(text)
            elem.click()
            return True
        except "no clicky for you":
            return False
