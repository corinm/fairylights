from .RandomTwinkling import RandomTwinkling

from time import sleep
from colour import Color


def run(leds):
    rt = RandomTwinkling(50, Color(rgb=(11, 77, 77)))

    while True:
        leds.setLeds(rt.tick())
