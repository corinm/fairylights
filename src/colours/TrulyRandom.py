from typing import List
from random import randrange

from colour import Color

from .Colours import Colours
from utils.randomColour import angleToColour


def randomColour():
    def nextColor():
        angle = randrange(0, 360)
        return angleToColour(angle)

    return nextColor

nextColour = randomColour()

class TrulyRandom(Colours):
    """
        Generates completely random colours
    """
    def __init__(self):
        self._firstCall = True
        self._colours: List[Color] = [nextColour(), nextColour()]

    def getColours(self) -> List[Color]:
        if self._firstCall:
            self._firstCall = False
            return self._colours

        self._colours = [self._colours[1], nextColour()]

        return self._colours
