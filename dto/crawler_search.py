class CrawlerSearch:
    def __init__(self, search_element: str) -> None:
        self.search_element = search_element
        self.attributes = {
            'class': '',
        }

    def set_attribute(self, attribute: str, value: str) -> None:
        self._check_attribute(attribute)

        self.attributes[attribute] = value

    def _check_attribute(self, attribute: str) -> None:
        if attribute not in self.attributes:
            raise AttributeError()
