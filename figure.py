from dto.coordinate import Coordinate


class Figure:
    def __init__(self, coordinates: list = None):
        self.coordinates = coordinates

        if coordinates is None:
            self.coordinates = []

    def get_minx(self) -> float:
        return min(coordinate.x for coordinate in self.coordinates)

    def get_maxx(self) -> float:
        return max(coordinate.x for coordinate in self.coordinates)

    def get_miny(self) -> float:
        return min(coordinate.y for coordinate in self.coordinates)

    def get_maxy(self) -> float:
        return max(coordinate.y for coordinate in self.coordinates)

    def display(self):
        for coordinate in self.coordinates:
            print("X:", coordinate.x, "Y:", coordinate.y)

    def set_coordinate(self, coordinate: Coordinate):
        self.coordinates.append(coordinate)
