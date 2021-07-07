import os
import sys
from typing import Callable

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


from colour import Color  # noqa

from leds.Leds import Leds  # noqa
from utils.colours import coolors, retroColours  # noqa
from utils.randomColour import colourWheel  # noqa
from utils.randomColour import randomAnalogousWeighted  # noqa
from utils.randomColour import randomColour137Degrees  # noqa
from utils.randomColour import randomColourAnalogous  # noqa
from utils.randomColour import randomComplementary  # noqa
from utils.randomColour import randomCoolorPalettes  # noqa
from utils.randomColour import randomSplitComplementary  # noqa
from utils.randomColour import randomColour as trulyRandom  # noqa

from .RandomTwinkling import RandomTwinkling  # noqa
from .RandomTwinklingFromColourAlgorithm import RandomTwinklingFromColourAlgorithm  # noqa
from .RandomTwinklingFromPalettes import RandomTwinklingFromPalettes  # noqa


def runTwinklingRetro(leds: Leds, shouldStop: Callable[[], bool]):
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

    while not shouldStop():
        leds.setLeds(rt.tick())

    rt.stop()

    while rt.isStopping():
        leds.setLeds(rt.tick())


def runRandomColours(leds: Leds):
    rc = RandomTwinklingFromColourAlgorithm(50, trulyRandom)

    while True:
        leds.setLeds(rc.tick())


def runRandomAnalagousColours(leds: Leds):
    rac = RandomTwinklingFromColourAlgorithm(
        50,
        randomColourAnalogous,
        secondsBetweenPaletteChanges=0,
        secondsBetweenColourChanges=5,
        numberOfColours=3,
    )

    while True:
        leds.setLeds(rac.tick())


def runRandomAnalagousWeightedColours(leds: Leds):
    rawc = RandomTwinklingFromColourAlgorithm(50, randomAnalogousWeighted, numberOfColours=3)

    while True:
        leds.setLeds(rawc.tick())


def runRandomComplementary(leds: Leds):
    rc = RandomTwinklingFromColourAlgorithm(50, randomComplementary, numberOfColours=6)

    while True:
        leds.setLeds(rc.tick())


def runRandomComplementaryMoving(leds: Leds):
    rc = RandomTwinklingFromColourAlgorithm(50, randomComplementary, numberOfColours=6)

    while True:
        leds.setLeds(rc.tick())


def runRandomSplitComplementary(leds: Leds):
    rc = RandomTwinklingFromColourAlgorithm(50, randomSplitComplementary, numberOfColours=5)

    while True:
        leds.setLeds(rc.tick())


def runRandomColour137Degress(leds: Leds):
    rc = RandomTwinklingFromColourAlgorithm(
        50, randomColour137Degrees, secondsBetweenColourChanges=5, numberOfColours=6
    )

    while True:
        leds.setLeds(rc.tick())


def runColoursWheel(leds: Leds):
    rac = RandomTwinklingFromColourAlgorithm(
        50, colourWheel, secondsBetweenPaletteChanges=0, secondsBetweenColourChanges=4
    )

    while True:
        leds.setLeds(rac.tick())


def runColoursWheelFast(leds: Leds):
    rac = RandomTwinklingFromColourAlgorithm(
        50, colourWheel, secondsBetweenPaletteChanges=0, secondsBetweenColourChanges=1
    )

    while True:
        leds.setLeds(rac.tick())


def runCoolorPalettes(leds: Leds):
    rt = RandomTwinklingFromPalettes(50, coolors)

    while True:
        leds.setLeds(rt.tick())
