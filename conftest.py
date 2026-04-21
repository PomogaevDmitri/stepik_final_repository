import pytest
from selenium import webdriver
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
                     default='ru',
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

#передача базовго url
@pytest.fixture()
def base_url(request):
    language = request.config.getoption("--language")
    return (f"http://selenium1py.pythonanywhere.com/"
            f"{language}/")


