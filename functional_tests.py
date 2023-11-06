from selenium import webdriver
import unittest


class BasicInstallTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_home_page_title(self):
        # начальная страница сайта
        # Заголовок сайта
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Сайт Алексея Куличевского', self.browser.title)

    def test_home_page_header(self):
        # Шапка сайта
        browser = self.browser.get('http://127.0.0.1:8000')
        header = browser.find_element_by_tag_name('h1')[0]
        self.assertIn('Алексей Куличевский', header)
        # self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
