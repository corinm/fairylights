import math
from colour import Color


def rainbow(numberOfLights: int):
    lights = []
    for i in range(0, 360):
        k = math.pi + i * (math.pi / 120)
        value = (math.cos(k) + 1) * 127.7 if k < math.pi * 3 else 0
        lights.append(math.floor(value))

    bulbs = []
    for i in range(0, 50):
        angle = i
        r = lights[(angle+120) % 360]
        g = lights[angle]
        b = lights[(angle+240) % 360]
        bulbs.append(Color(rgb=(r, g, b)))

    return bulbs
