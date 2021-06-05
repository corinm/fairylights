import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from colour import Color  # noqa

from leds.Leds import Leds  # noqa

from .RandomTwinkling import RandomTwinkling  # noqa

yellow = Color(rgb=(11 / 255, 77 / 255, 57 / 255))


def run(leds: Leds):
    rt = RandomTwinkling(50, [yellow])

    while True:
        leds.setLeds(rt.tick())
