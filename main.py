from data_processor import DataProcessor
from data.restrictions import data as dataset
from dto.crawler_search import CrawlerSearch

search_data = CrawlerSearch('div')
search_data.set_attribute('class', 'auto-route-snippet-view__route-subtitle')

data = DataProcessor(5, dataset, search_data)

data.process()
