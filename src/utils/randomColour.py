import math
from random import randrange
from typing import List

from colour import Color

from .colours import coolors
from .colourWheel import COLOUR_WHEEL


def generateColourWheel():
    wheel = []

    for i in range(0, 360):
        k = math.pi + i * (math.pi / 120)
        value = (math.cos(k) + 1) * 127.7 if k < math.pi * 3 else 0
        wheel.append(math.floor(value))

    return wheel


wheel = generateColourWheel()


def angleToColour(angle: int):
    # angle = 0-360
    assert angle >= 0
    assert angle <= 360

    r = wheel[(angle + 120) % 360]
    g = wheel[angle]
    b = wheel[(angle + 240) % 360]

    return Color(rgb=(r / 255, g / 255, b / 255))


def randomColour137Degrees(numberOfColours: int):
    """
    Colours are chosen by choosing a random starting point on the colour wheel
    then incrementing by 137deg each time a colour is requested
    This creates a palette where colours overlap as little as possible
    """
    angle = randrange(0, 360)

    def nextColour():
        nonlocal angle
        angle += 137

        if angle >= 360:
            angle -= 360

        return angleToColour(angle)

    return nextColour


def colourWheel(numberOfColours: int):
    angle = randrange(0, 360)

    def nextColour():
        nonlocal angle
        angle = (angle + 15) % 360
        return angleToColour(angle)

    return nextColour


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


def randomCoolorPalettes(numberOfColours: int = 0):
    currentPalleteIndex: int = randrange(0, len(coolors))
    colourIndex = 0

    def nextColour():
        nonlocal colourIndex

        colour: Color = coolors[currentPalleteIndex][colourIndex]
        colourIndex += 1

        if colourIndex >= len(coolors[currentPalleteIndex]):
            colourIndex = 0

        return colour

    return nextColour
