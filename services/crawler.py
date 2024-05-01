from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from dto.crawler_search import CrawlerSearch
from services.helpers.url_generator import UrlGenerator


class Crawler:
    def __init__(self, search: CrawlerSearch) -> None:
        self.search = search
        self.url = None

        self.url_generator = UrlGenerator()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')

        self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    def crawl(self) -> str:
        self._check_url()

        content = self._getContent(self.url)
        soup = BeautifulSoup(content, 'html.parser')
        needle = soup.find(self.search.search_element, attrs=self.search.attributes)

        return needle.text

    def generate_url(self, data: dict) -> None:
        self.url = self.url_generator.generate(data)

    def _getContent(self, url: str) -> str:
        self.driver.get(url)
        return self.driver.page_source

    def _check_url(self) -> None:
        if self.url is None:
            raise Exception("URL cannot be None")

    def __del__(self):  # Assuming Python 2 or using @destructor in Python 3
        self.driver.quit()
