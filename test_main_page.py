from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser,base_url):
    page = MainPage(browser, base_url)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()       # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser,base_url):
    page = MainPage(browser, base_url)
    page.open()
    page.should_be_login_link()