from typing import List
from random import randrange

from colour import Color
from colours.AnalogousRandom import randomColourAnalogous

from .Colours import Colours
from utils.randomColour import angleToColour


RANGE_OF_ANALAGOUS_COLOURS = int(360 / 12 * 3)


class Segment:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


def randomAnalogousWeighted():
    """
    This algorithm divides the arc into three segments and chooses colours from each segment in turn
    Each time a colour is chosen its luminance or saturation are varied to emphasise one of the three segments over the other two
    Note: Arc does NOT move over time
    """
    angleAtStartOfRange = randrange(0, 360)
    segmentSize = int(360 / 12)

    segments: List[Segment] = [
        Segment(angleAtStartOfRange, angleAtStartOfRange + segmentSize),
        Segment(angleAtStartOfRange + segmentSize, angleAtStartOfRange + segmentSize * 2),
        Segment(angleAtStartOfRange + segmentSize * 2, angleAtStartOfRange + segmentSize * 3),
    ]

    currentSegment = 0

    def nextColour():
        nonlocal currentSegment

        angle = randrange(segments[currentSegment].start, segments[currentSegment].end)

        colour = angleToColour(angle % 360)

        if currentSegment == 0:
            colour.luminance = 0.15
        elif currentSegment == 1:
            colour.saturation = 0.8

        currentSegment += 1

        if currentSegment >= 3:
            currentSegment = 0

        return colour

    return nextColour

nextColour = randomAnalogousWeighted()


class AnalogousWeightedRandom(Colours):
    def __init__(self):
        self._firstCall = True
        self._colours: List[Color] = [nextColour(), nextColour(), nextColour()]

    def getColours(self) -> List[Color]:
        if self._firstCall:
            self._firstCall = False
            return self._colours

        self._colours = [self._colours[1], self._colours[2], nextColour()]

        return self._colours
