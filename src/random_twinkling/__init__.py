import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


from colour import Color  # noqa

from leds.Leds import Leds  # noqa
from utils.randomColour import colourWheel  # noqa
from utils.randomColour import randomAnalogousWeighted  # noqa
from utils.randomColour import randomColour137Degrees  # noqa
from utils.randomColour import randomColourAnalogous  # noqa
from utils.randomColour import randomComplimentary  # noqa
from utils.randomColour import randomColour as trulyRandom  # noqa

from .RandomColours import RandomColours  # noqa
from .RandomTwinkling import RandomTwinkling  # noqa

blue80s = Color(rgb=(11 / 255, 77 / 255, 57 / 255))
pink80s = Color(rgb=(57 / 255, 11 / 255, 77 / 255))

# Retro Noma Pickwick fairy lights
pink = Color(rgb=(93 / 255, 19 / 255, 56 / 255))
blue = Color(rgb=(0 / 255, 73 / 255, 127 / 255))
orange = Color(rgb=(199 * 0.8 / 255, 90 * 0.8 / 255, 0 * 0.8 / 255))
green = Color(rgb=(54 * 0.4 / 255, 139 / 255, 27 * 0.4 / 255))
red = Color(rgb=(184 * 0.7 / 255, 44 * 0.4 / 255, 8 * 0.4 / 255))


def runTwinklingRetro(leds: Leds):
    rt = RandomTwinkling(50, [pink, blue80s, orange, green, red])

    while True:
        leds.setLeds(rt.tick())


def runRandomColours(leds: Leds):
    rc = RandomColours(50, trulyRandom)

    while True:
        leds.setLeds(rc.tick())


def runRandomAnalagousColours(leds: Leds):
    rac = RandomColours(50, randomColourAnalogous())

    while True:
        leds.setLeds(rac.tick())


def runRandomAnalagousWeightedColours(leds: Leds):
    rawc = RandomColours(50, randomAnalogousWeighted(), numberOfColours=3)

    while True:
        leds.setLeds(rawc.tick())


def runRandomComplimentary(leds: Leds):
    rc = RandomColours(50, randomComplimentary(6), numberOfColours=6)

    while True:
        leds.setLeds(rc.tick())


def runRandomComplimentaryMoving(leds: Leds):
    rc = RandomColours(50, randomComplimentary(6), numberOfColours=6)

    while True:
        leds.setLeds(rc.tick())


def runRandomColour137Degress(leds: Leds):
    rc = RandomColours(50, randomColour137Degrees(), 5, 6)

    while True:
        leds.setLeds(rc.tick())


def runColoursWheel(leds: Leds):
    rac = RandomColours(50, colourWheel(), 4)

    while True:
        leds.setLeds(rac.tick())
