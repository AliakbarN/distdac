from typing import Any


class Coordinate:
    def __init__(self, x: float, y: float) -> None:
        self.y = y
        self.x = x

    def gety(self) -> float:
        return self.y

    def getx(self) -> float:
        return self.x

    def display(self) -> None:
        print('X:', self.x, 'Y:', self.y)
