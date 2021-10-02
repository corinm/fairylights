from random import randrange

from .Colours import ColoursFromAlgorithm
from utils.randomColour import angleToColour

def colourWheel():
    angle = randrange(0, 360)

    def nextColour():
        nonlocal angle
        angle = (angle + 15) % 360
        return angleToColour(angle)

    return nextColour


colourWheel = ColoursFromAlgorithm(colourWheel(), 2)