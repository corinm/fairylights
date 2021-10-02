from random import randrange

from .Colours import ColoursFromAlgorithm
from utils.randomColour import angleToColour


RANGE_OF_ANALAGOUS_COLOURS = int(360 / 12 * 3)


class Segment:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


def randomComplementary(numberOfColours=6, angleAtStart=None):
    """
    Colours are chosen from segments opposite each other on the colour wheel
    The saturation and luminance of colours are varied to emphasise one segment over the other
    and create a more interesting palette
    """
    if angleAtStart is None:
        angleAtStart = randrange(0, 360)

    segmentSize = int(360 / 12)

    segment1 = Segment(angleAtStart, angleAtStart + segmentSize)
    opposite = Segment(angleAtStart + 180, angleAtStart + 180 + segmentSize)

    counter = 0

    def nextColour():
        nonlocal counter

        segment = segment1 if counter == 0 else opposite
        angle = randrange(segment.start, segment.end)
        colour = angleToColour(angle % 360)

        if counter != 0:
            if counter % 2 == 1:
                colour.luminance = 0.15
            else:
                colour.saturation = 0.7

        counter += 1

        if counter >= numberOfColours:
            counter = 0

        return colour

    return nextColour


complementaryRandom = ColoursFromAlgorithm(randomComplementary(), 6)
