from random import randrange

from .Colours import ColoursFromAlgorithm
from utils.randomColour import angleToColour

def randomColour137Degrees():
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


every137Degrees = ColoursFromAlgorithm(randomColour137Degrees(), 5)
