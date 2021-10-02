import math
from random import randrange

from colour import Color

from .colours import coolors


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


def randomCoolorPalettes():
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
