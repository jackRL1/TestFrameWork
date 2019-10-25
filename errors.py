"""
Exception class for throwing errors making the debugging much easier.
throws detailed errors
"""


class Exceptions(Exception):
    """ This is the base class exceptions of exception """
    pass


class BadLocatorValue(Exceptions):
    def get_message(self):
        return self.mess

    def set_message(self, message):
        self.mess = message

    message = property(get_message, set_message)


class NoSuchElementException(Exceptions):
    def get_message(self):
        return self.mess

    def set_message(self, message):
        self.mess = message

    message = property(get_message, set_message)
