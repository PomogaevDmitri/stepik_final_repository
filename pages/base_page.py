
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import none_of


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_url_contains_str(self, str_in_url):
        try:
            str_in_url in self.browser.current_url
        except NoSuchElementException:
            return False
        return True

    def removing_spaces(self, stroke):
        return ''.join(stroke.split())