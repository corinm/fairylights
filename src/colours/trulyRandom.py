from random import randrange

from .Colours import ColoursFromAlgorithm
from utils.randomColour import angleToColour


def randomColour():
    def nextColor():
        angle = randrange(0, 360)
        return angleToColour(angle)

    return nextColor


trulyRandom = ColoursFromAlgorithm(randomColour(), 2)
