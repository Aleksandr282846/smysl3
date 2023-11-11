from selenium import webdriver
from selenium.webdriver.common.by import By
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
        self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Алексей Куличевский', header.text)

    def test_home_page_blog(self):
        self.browser.get('http://127.0.0.1:8000')
        article_list = self.browser.find_element_by_class_name('article-list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element_by_class_name(
            'article-title')
        article_summary = self.browser.find_element_by_class_name(
            'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)


if __name__ == '__main__':
    unittest.main()
