from random import randrange

from .Colours import ColoursFromAlgorithm
from utils.randomColour import angleToColour


RANGE_OF_ANALAGOUS_COLOURS = int(360 / 12 * 3)


def randomColourAnalogous():
    """
    Creates an arc on the colour wheel from a random starting angle that covers 3/12 (1/4) of the wheel
    The starting angle is incremented every time a colour is chosen, causing the arc to gradually
    move around the colour wheel
    """
    angleAtStartOfRange = randrange(0, 360)

    def nextColour():
        nonlocal angleAtStartOfRange

        end = angleAtStartOfRange + RANGE_OF_ANALAGOUS_COLOURS
        colour = angleToColour(randrange(angleAtStartOfRange, end) % 360)

        angleAtStartOfRange = angleAtStartOfRange + 10
        if angleAtStartOfRange >= 360:
            angleAtStartOfRange -= 360

        return colour

    return nextColour


analogousRandom = ColoursFromAlgorithm(randomColourAnalogous(), 3)
