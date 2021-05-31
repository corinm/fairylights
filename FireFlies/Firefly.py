from enum import Enum
from random import randrange


class Direction(Enum):
    DOWN = 1
    UP = 2


class Firefly:
    def __init__(self):
        self.direction: Direction = getRandomDirection()
        self.state = 0


def getRandomDirection():
    return Direction.UP if randrange(0, 2) == 0 else Direction.DOWN
