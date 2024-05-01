import time
from dto.coordinate import Coordinate
from dto.crawler_search import CrawlerSearch
from direction import Direction
from figure import Figure
from data.restrictions import data as dataset
from services.crawler import Crawler
from services.helpers.array_avarage import calculate_average
from services.helpers.mile_to_km import mile_to_km
from services.helpers.random_triangular import random_triangular
from services.helpers.record_data import record_data
from services.helpers.url_generator import UrlGenerator
from services.helpers.parse_crawler_response import parse_crawler_response

restriction_area = Figure()

for coordinates in dataset:
    coordinate = Coordinate(coordinates['x'], coordinates['y'])

    restriction_area.set_coordinate(coordinate)


directions = []
random_coordinates_number = 10

print('MAX X:', restriction_area.get_maxx(), 'MIN X :', restriction_area.get_minx(), 'MAX Y :', restriction_area.get_maxy(), 'MIN Y :', restriction_area.get_miny())

for i in range(random_coordinates_number):
    point_1_x = random_triangular(restriction_area.get_minx(), restriction_area.get_maxx())
    point_1_y = random_triangular(restriction_area.get_miny(), restriction_area.get_maxy())
    point_2_x = random_triangular(restriction_area.get_minx(), restriction_area.get_maxx())
    point_2_y = random_triangular(restriction_area.get_miny(), restriction_area.get_maxy())

    point_1 = Coordinate(point_1_x, point_1_y)
    point_2 = Coordinate(point_2_x, point_2_y)

    direction = Direction(point_1, point_2)

    print('POINT 1 ===', 'X:', point_1.x, 'Y:', point_1.y, 'POINT 2 ===', 'X:', point_2.x, 'Y:', point_2.y)
    print('ID:', i, 'APPROXIMATED DISTANCE :', direction.calculate_distance())
    print('================================================================================================================')

    directions.append(direction)

crawler_search = CrawlerSearch('div')
crawler_search.set_attribute('class', 'auto-route-snippet-view__route-subtitle')
crawler = Crawler(crawler_search)

precise_directions = []


for i, direction in enumerate(directions):
    data = {
        'point_1_x': direction.get_point1().x,
        'point_1_y': direction.get_point1().y,
        'point_2_x': direction.get_point2().x,
        'point_2_y': direction.get_point2().y
    }

    crawler.generate_url(data)
    precise_direction = crawler.crawl()
    precise_direction = parse_crawler_response(precise_direction)
    precise_direction = mile_to_km(precise_direction)

    precise_directions.append(precise_direction)

    print('ID:', i, 'PRECISE DISTANCE :', precise_direction)
    time.sleep(0.1)

res_coefficients = []

for i, pr_direction in enumerate(precise_directions):
    cal_dir = directions[i].calculate_distance()

    coefficient = pr_direction / cal_dir

    res_coefficients.append(coefficient)


print(res_coefficients)

average_coefficient = calculate_average(res_coefficients)
print(average_coefficient)

# record_data(res_coefficients, average_coefficient)