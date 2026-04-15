import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
#парсинг командной строки
def pytest_addoption(parser):
    # парсинг browser_name
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help="Choose browser: chrome or firefox")
    # парсинг language
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language: es, ru)")

#Инициализация браузера
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        print(f" start '{browser_name}' for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print(f" start '{browser_name}' browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError(f"--browser_name '{browser_name}'"
                                f" should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

#передача урла
@pytest.fixture
def base_url(request):
    language = request.config.getoption("--language")
    return (f"http://selenium1py.pythonanywhere.com/"
            f"{language}/catalogue/coders-at-work_207/")

#WebDriverWait на проверку кликабельности на сайте
@pytest.fixture
def clickable_button_in_5(browser):
    def _clickable_button_in_5(css_selector_button):
        return WebDriverWait(browser, 5).\
                    until(ec.element_to_be_clickable((By.CSS_SELECTOR, css_selector_button))
                          )
    return _clickable_button_in_5

