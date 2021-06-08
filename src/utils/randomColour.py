import math
from random import randrange

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
    # TODO: This is going to keep increasing in size as it iterates
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
        print(angleAtStartOfRange, end)
        return angleToColour(randrange(angleAtStartOfRange, end) % 360)

    return nextColour
