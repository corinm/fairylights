from typing import List

from colour import Color

from .Colours import Colours
from utils.randomColour import angleToColour


def createRainbowGradient(numberOfLights: int) -> List[Color]:
    bulbs = []

    for i in range(numberOfLights):
        angle = int((i / numberOfLights) * 360)
        bulbs.append(angleToColour(angle))

    return bulbs


class Rainbow(Colours):
    def __init__(self):
        pass

    def getColours(self, numberOfBulbs: int) -> List[Color]:
        return createRainbowGradient(numberOfBulbs)


rainbow = Rainbow()
