"""
    This file holds the Element class. This class is used for returning web element objects
    to the web driver class. These elements are then utilized for whatever testing perposes are
    required in the unit tests.
"""
from selenium.webdriver.remote.webelement import WebElement as SelWebEle


""" Element is a subclass of webelement. Its used for returning web element objects  """


class Element(SelWebEle):
    def __init__(self, elem):
        super(Element, self).__init__(elem.parent, elem.id)

    """ finds and returns elements on a page by locate_value """
    def find_element_by_locator(self, locate):
        locate_type, locate_value = locate.split('=')
        if locate_type == 'class':
            return Element(self.find_element_by_class_name(locate_value))
        elif locate_type == 'css':
            return Element(self.find_element_by_css_selector(locate_value))
        elif locate_type == 'id':
            return Element(self.find_element_by_id(locate_value))
        elif locate_type == 'link':
            return Element(self.find_element_by_link_text(locate_value))
        elif locate_type == 'name':
            return Element(self.find_element_by_name(locate_value))
        elif locate_type == 'plink':
            return Element(self.find_element_by_partial_link_text(locate_value))
        elif locate_type == 'tag':
            return Element(self.find_element_by_tag_name(locate_value))
        elif locate_type == 'xpath':
            return Element(self.find_element_by_xpath(locate_value))
        else:
            raise Exception('Bad Locator value')

    """ returns a list of elements that are found by locate_value """
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
