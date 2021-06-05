from colour import Color

from .RandomTwinkling import RandomTwinkling

yellow = Color(rgb=(11 / 255, 77 / 255, 57 / 255))


def run(leds):
    rt = RandomTwinkling(50, yellow)

    while True:
        leds.setLeds(rt.tick())
