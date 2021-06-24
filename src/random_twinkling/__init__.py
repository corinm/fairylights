import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


from colour import Color  # noqa

from leds.Leds import Leds  # noqa
from utils.colours import retroColours  # noqa
from utils.randomColour import colourWheel  # noqa
from utils.randomColour import randomAnalogousWeighted  # noqa
from utils.randomColour import randomColour137Degrees  # noqa
from utils.randomColour import randomColourAnalogous  # noqa
from utils.randomColour import randomComplementary  # noqa
from utils.randomColour import randomSplitComplementary  # noqa
from utils.randomColour import randomColour as trulyRandom  # noqa

from .RandomColours import RandomColours  # noqa
from .RandomTwinkling import RandomTwinkling  # noqa


def runTwinklingRetro(leds: Leds):
    rt = RandomTwinkling(
        50,
        [
            retroColours["pink"],
            retroColours["blue"],
            retroColours["orange"],
            retroColours["green"],
            retroColours["red"],
        ],
    )

    while True:
        leds.setLeds(rt.tick())


def runRandomColours(leds: Leds):
    rc = RandomColours(50, trulyRandom)

    while True:
        leds.setLeds(rc.tick())


def runRandomAnalagousColours(leds: Leds):
    rac = RandomColours(
        50,
        randomColourAnalogous,
        secondsBetweenPaletteChanges=0,
        secondsBetweenColourChanges=5,
        numberOfColours=3,
    )

    while True:
        leds.setLeds(rac.tick())


def runRandomAnalagousWeightedColours(leds: Leds):
    rawc = RandomColours(50, randomAnalogousWeighted, numberOfColours=3)

    while True:
        leds.setLeds(rawc.tick())


def runRandomComplementary(leds: Leds):
    rc = RandomColours(50, randomComplementary, numberOfColours=6)

    while True:
        leds.setLeds(rc.tick())


def runRandomComplementaryMoving(leds: Leds):
    rc = RandomColours(50, randomComplementary, numberOfColours=6)

    while True:
        leds.setLeds(rc.tick())


def runRandomSplitComplementary(leds: Leds):
    rc = RandomColours(50, randomSplitComplementary, numberOfColours=5)

    while True:
        leds.setLeds(rc.tick())


def runRandomColour137Degress(leds: Leds):
    rc = RandomColours(50, randomColour137Degrees, secondsBetweenColourChanges=5, numberOfColours=6)

    while True:
        leds.setLeds(rc.tick())


def runColoursWheel(leds: Leds):
    rac = RandomColours(
        50, colourWheel, secondsBetweenPaletteChanges=0, secondsBetweenColourChanges=4
    )

    while True:
        leds.setLeds(rac.tick())


def runColoursWheelFast(leds: Leds):
    rac = RandomColours(
        50, colourWheel, secondsBetweenPaletteChanges=0, secondsBetweenColourChanges=1
    )

    while True:
        leds.setLeds(rac.tick())
