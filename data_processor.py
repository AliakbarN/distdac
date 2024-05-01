import time

from direction import Direction
from dto.coordinate import Coordinate
from dto.crawler_search import CrawlerSearch
from figure import Figure
from services.crawler import Crawler
from services.helpers.array_avarage import calculate_average
from services.helpers.mile_to_km import mile_to_km
from services.helpers.parse_crawler_response import parse_crawler_response
from services.helpers.random_triangular import random_triangular
from services.helpers.record_data import record_data


class DataProcessor:
    def __init__(self, iterations: int, dataset: list, search_data: CrawlerSearch) -> None:
        self.iterations = iterations
        self.dataset = dataset
        self.restriction_area = self._make_restriction_area()
        self.crawler = Crawler(search_data)

    def process(self) -> float:
        print('PROCESSING...')

        directions = self._generate_directions()
        precise_directions_distances = self._get_precise_directions_distances(directions)
        coefficients = self._calculate_coefficients(self._get_calculated_distances(directions), precise_directions_distances)
        average_coefficient = calculate_average(list(coefficients.values()))

        record_data(self._form_record_data(directions, precise_directions_distances, coefficients, average_coefficient))

        print('PROCESSING COMPLETE!')

        return average_coefficient

    def _make_restriction_area(self) -> Figure:
        restriction_area = Figure()

        for coordinates in self.dataset:
            coordinate = Coordinate(coordinates['x'], coordinates['y'])

            restriction_area.set_coordinate(coordinate)

        return restriction_area

    def _form_record_data(self, directions: dict, precise_directions_distances: dict, coefficients: dict, coefficient: float) -> dict:
        data = {
            'PRECISE DISTANCES': precise_directions_distances.copy(),
            'CALCULATED DISTANCES': self._get_calculated_distances(directions),
        }

        coordinates = {}

        for index, direction in directions.items():
            coordinates[index] = {
                'POINT 1: X': direction.get_point1().x,
                'POINT 1: Y': direction.get_point1().y,
                'POINT 2: X': direction.get_point2().x,
                'POINT 2: Y': direction.get_point2().x,
                'NEXT': '|||'
            }

        data['COORDINATES'] = coordinates
        data['COEFFICIENTS'] = coefficients.copy()
        data['COEFFICIENT'] = coefficient

        return data

    def _generate_directions(self) -> dict:
        directions = {}

        for index in range(self.iterations):
            coordinate_1 = self._generate_random_coordinate()
            coordinate_2 = self._generate_random_coordinate()

            direction = Direction(coordinate_1, coordinate_2)

            directions[str(index)] = direction

        return directions

    def _get_precise_directions_distances(self, directions: dict) -> dict:
        print('CRAWLING...')

        distances = {}

        for index, direction in directions.items():
            data = {
                'point_1_x': direction.get_point1().x,
                'point_1_y': direction.get_point1().y,
                'point_2_x': direction.get_point2().x,
                'point_2_y': direction.get_point2().y
            }

            self.crawler.generate_url(data)

            precise_direction = self.crawler.crawl()
            precise_direction = parse_crawler_response(precise_direction)
            precise_direction = mile_to_km(precise_direction)

            distances[str(index)] = precise_direction

            time.sleep(0.1)

        return distances

    @staticmethod
    def _calculate_coefficients(calculated_distances: dict, precise_distances: dict) -> dict:
        coefficients = {}

        for index, calculated_distance in calculated_distances.items():
            precise_distance = precise_distances[index]

            coefficient = precise_distance / calculated_distance
            coefficients[str(index)] = coefficient

        return coefficients

    def _generate_random_coordinate(self) -> Coordinate:
        x = random_triangular(self.restriction_area.get_minx(), self.restriction_area.get_maxx())
        y = random_triangular(self.restriction_area.get_miny(), self.restriction_area.get_maxy())

        coordinate = Coordinate(x, y)
        return coordinate

    @staticmethod
    def _get_calculated_distances(directions: dict) -> dict:
        distances = {}

        for index, direction in directions.items():
            distance = direction.calculate_distance()
            distances[str(index)] = distance

        return distances
