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
        article_list = self.browser.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element(By.CLASS_NAME,
                                                  'article-title')
        article_summary = self.browser.find_element(By.CLASS_NAME,
                                                    'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)

    def test_home_page_article_title_link_leads_to_article_page(self):
        self.browser.get('http://127.0.0.1:8000')

        article_title = self.browser.find_element(
            By.CLASS_NAME, 'article-title')

        article_title_text = article_title.text

        article_link = article_title.find_element(By.TAG_NAME, 'a')
        self.browser.get(article_link.get_attribute('href'))
        article_page_title = self.browser.find_element(
            By.CLASS_NAME, 'article-title')
        self.assertEqual(article_title_text, article_page_title.text)


if __name__ == '__main__':
    unittest.main()
