import math
from dto.coordinate import Coordinate


class Direction:
    def __init__(self, point1: Coordinate, point2: Coordinate) -> None:
        self.point1 = point1
        self.point2 = point2

    def calculate_distance(self) -> float:
        x1 = math.radians(self.point1.getx())
        y1 = math.radians(self.point1.gety())
        x2 = math.radians(self.point2.getx())
        y2 = math.radians(self.point2.gety())

        # Equirectangular approximation for small distances
        if abs(x1 - x2) < 0.02 and abs(y1 - y2) < 0.02:
            dx = x2 - x1
            dy = y2 - y1
            distance = math.sqrt(dx * dx + dy * dy) * 6371  # Radius of the Earth in kilometers
            return distance

        # Haversine formula for larger distances
        else:
            dx = x2 - x1
            dy = y2 - y1
            a = math.sin(dy / 2) ** 2 + math.cos(y1) * math.cos(y2) * math.sin(dx / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = 6371 * c  # Radius of the Earth in kilometers
            return distance

    def get_point1(self) -> Coordinate:
        return self.point1

    def get_point2(self) -> Coordinate:
        return self.point2
