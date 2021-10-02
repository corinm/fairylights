from random import randrange

from colour import Color

from .Colours import ColoursFromAlgorithm
from utils.colourWheel import COLOUR_WHEEL


class Segment:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


def randomSplitComplementary(numberOfColours: int = 5):
    angle = randrange(0, 12)
    index = 0

    def nextColour():
        nonlocal angle
        nonlocal index

        colour: Color = Color(None)

        if index == 0:
            colour = COLOUR_WHEEL[angle]
        elif index == 1:
            colour = COLOUR_WHEEL[(angle + 5) % 12]
        elif index == 2:
            colour = COLOUR_WHEEL[(angle + 7) % 12]
        elif index == 3:
            colour = Color(COLOUR_WHEEL[(angle + 5) % 12])
            colour.saturation = 0.86
        elif index == 4:
            colour = Color(COLOUR_WHEEL[(angle + 7) % 12])
            colour.saturation = 0.86

        print(angle, index, colour)

        index += 1

        if index >= numberOfColours:
            index = 0

        return colour

    return nextColour


splitComplementaryRandom = ColoursFromAlgorithm(randomSplitComplementary(), 5)
