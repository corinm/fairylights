import math
from random import randrange
from typing import List

from colour import Color


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


def randomColour():
    angle = randrange(0, 360)
    return angleToColour(angle)


RANGE_OF_ANALAGOUS_COLOURS = int(360 / 9 * 3)


def randomColourAnalogous():
    angleAtStartOfRange = randrange(0, 360)

    iterations = 0

    def nextColour():
        nonlocal iterations
        nonlocal angleAtStartOfRange
        iterations += 1

        if iterations >= 1:
            angleAtStartOfRange = angleAtStartOfRange + 5
            iterations = 0

            if angleAtStartOfRange >= 360:
                angleAtStartOfRange -= 360

        end = angleAtStartOfRange + RANGE_OF_ANALAGOUS_COLOURS
        return angleToColour(randrange(angleAtStartOfRange, end) % 360)

    return nextColour


class Segment:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


def randomAnalogousWeighted():
    angleAtStartOfRange = randrange(0, 360)
    segmentSize = int(360 / 12)

    segments: List[Segment] = [
        Segment(angleAtStartOfRange, angleAtStartOfRange + segmentSize),
        Segment(
            angleAtStartOfRange + segmentSize, angleAtStartOfRange + segmentSize * 2
        ),
        Segment(
            angleAtStartOfRange + segmentSize * 2, angleAtStartOfRange + segmentSize * 3
        ),
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

        print(colour)

        return colour

    return nextColour


# def randomComplimentaryMoving(numberOfColours=3):
#     angleAtStart = randrange(0, 360)
#     counter = 0
#     rc = randomComplimentary(numberOfColours=numberOfColours, angleAtStart=angleAtStart)

#     def nextColour():
#         nonlocal angleAtStart
#         nonlocal counter
#         nonlocal rc

#         counter += 1

#         if counter > 10:
#             counter = 0
#             angleAtStart += 137
#             rc = randomComplimentary(
#                 numberOfColours=numberOfColours, angleAtStart=angleAtStart
#             )

#         return rc()

#     return nextColour


def randomComplimentary(numberOfColours=3, angleAtStart=None):
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


def randomColour137Degrees():
    angle = randrange(0, 360)

    def nextColour():
        nonlocal angle
        angle += 137

        if angle >= 360:
            angle -= 360

        return angleToColour(angle)

    return nextColour


def colourWheel():
    angle = randrange(0, 360)

    def nextColour():
        nonlocal angle
        angle = (angle + 15) % 360
        return angleToColour(angle)

    return nextColour
