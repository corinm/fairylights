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

from .Twinkle import Twinkle  # noqa
from .TwinkleFromColourAlgorithm import TwinkleFromColourAlgorithm  # noqa
from .TwinkleFromPalettes import TwinkleFromPalettes  # noqa


def runTwinkleRetro(leds: Leds, shouldStop: Callable[[], bool]):
    rt = Twinkle(
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


def runRandomColours(leds: Leds, shouldStop: Callable[[], bool]):
    rt = TwinkleFromColourAlgorithm(50, trulyRandom)

    while not shouldStop():
        leds.setLeds(rt.tick())

    rt.stop()

    while rt.isStopping():
        leds.setLeds(rt.tick())


def runRandomAnalagousColours(leds: Leds, shouldStop: Callable[[], bool]):
    rt = TwinkleFromColourAlgorithm(
        50,
        randomColourAnalogous,
        secondsBetweenPaletteChanges=0,
        secondsBetweenColourChanges=5,
        numberOfColours=3,
    )

    while not shouldStop():
        leds.setLeds(rt.tick())

    rt.stop()

    while rt.isStopping():
        leds.setLeds(rt.tick())


def runRandomAnalagousWeightedColours(leds: Leds, shouldStop: Callable[[], bool]):
    rt = TwinkleFromColourAlgorithm(50, randomAnalogousWeighted, numberOfColours=3)

    while not shouldStop():
        leds.setLeds(rt.tick())

    rt.stop()

    while rt.isStopping():
        leds.setLeds(rt.tick())


def runRandomComplementary(leds: Leds, shouldStop: Callable[[], bool]):
    rt = TwinkleFromColourAlgorithm(50, randomComplementary, numberOfColours=6)

    while not shouldStop():
        leds.setLeds(rt.tick())

    rt.stop()

    while rt.isStopping():
        leds.setLeds(rt.tick())


# TODO: Not using this, what was the benefit, should I delete it?
def runRandomComplementaryMoving(leds: Leds, shouldStop: Callable[[], bool]):
    rt = TwinkleFromColourAlgorithm(50, randomComplementary, numberOfColours=6)

    while not shouldStop():
        leds.setLeds(rt.tick())

    rt.stop()

    while rt.isStopping():
        leds.setLeds(rt.tick())


def runRandomSplitComplementary(leds: Leds, shouldStop: Callable[[], bool]):
    rt = TwinkleFromColourAlgorithm(50, randomSplitComplementary, numberOfColours=5)

    while not shouldStop():
        leds.setLeds(rt.tick())

    rt.stop()

    while rt.isStopping():
        leds.setLeds(rt.tick())


def runRandomColour137Degress(leds: Leds, shouldStop: Callable[[], bool]):
    rt = TwinkleFromColourAlgorithm(
        50, randomColour137Degrees, secondsBetweenColourChanges=5, numberOfColours=6
    )

    while not shouldStop():
        leds.setLeds(rt.tick())

    rt.stop()

    while rt.isStopping():
        leds.setLeds(rt.tick())


def runColoursWheel(leds: Leds, shouldStop: Callable[[], bool]):
    rt = TwinkleFromColourAlgorithm(
        50, colourWheel, secondsBetweenPaletteChanges=0, secondsBetweenColourChanges=4
    )

    while not shouldStop():
        leds.setLeds(rt.tick())

    rt.stop()

    while rt.isStopping():
        leds.setLeds(rt.tick())


def runColoursWheelFast(leds: Leds, shouldStop: Callable[[], bool]):
    rt = TwinkleFromColourAlgorithm(
        50, colourWheel, secondsBetweenPaletteChanges=0, secondsBetweenColourChanges=1
    )

    while not shouldStop():
        leds.setLeds(rt.tick())

    rt.stop()

    while rt.isStopping():
        leds.setLeds(rt.tick())


def runCoolorPalettes(leds: Leds, shouldStop: Callable[[], bool]):
    rt = TwinkleFromPalettes(50, coolors)

    while not shouldStop():
        leds.setLeds(rt.tick())

    rt.stop()

    while rt.isStopping():
        leds.setLeds(rt.tick())
