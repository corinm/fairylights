from .RandomTwinkling import RandomTwinkling

from time import sleep
from colour import Color


def run(leds):
    rt = RandomTwinkling(50, Color('#00494b'))

    print(Color('#00494b').red, Color('#00494b').green, Color('#00494b').blue)

    while True:
        leds.setLeds(rt.tick())
