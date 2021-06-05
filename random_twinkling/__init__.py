from .RandomTwinkling import RandomTwinkling

from time import sleep
from colour import Color


def run(leds):
    rt = RandomTwinkling(50, Color(rgb=(11/255, 77/255, 57/255)))

    while True:
        leds.setLeds(rt.tick())
