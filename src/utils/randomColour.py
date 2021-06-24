import math
from random import randrange
from typing import List

from colour import Color

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


def randomColour(numberOfColours: int):
    def nextColor():
        angle = randrange(0, 360)
        return angleToColour(angle)

    return nextColor


RANGE_OF_ANALAGOUS_COLOURS = int(360 / 12 * 3)


def randomColourAnalogous(numberOfColours: int):
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


class Segment:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


def randomAnalogousWeighted(numberOfColours: int):
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


def randomComplementary(numberOfColours=3, angleAtStart=None):
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
