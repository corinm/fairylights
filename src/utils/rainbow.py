import math
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
