from typing import Callable

from leds.Leds import Leds

from .FirefliesConstant import FirefliesConstant
from .FirefliesWaves import FirefliesWaves
from .patterns import flicker, staticGlow


def runStaticGlow(leds: Leds, shouldStop: Callable[[], bool]):
    ff = FirefliesWaves(50, staticGlow, ticksActiveRange=(2, 30), ticksBetweenWavesRange=(5, 150))

    while not shouldStop():
        leds.setLeds(ff.tick())

    ff.stop()

    while ff.isStopping():
        leds.setLeds(ff.tick())


def runStaticGlowShorter(leds: Leds, shouldStop: Callable[[], bool]):
    ff = FirefliesConstant()

    while not shouldStop():
        leds.setLeds(ff.tick())

    ff.stop()

    while ff.isStopping():
        leds.setLeds(ff.tick())


def runFlicker(leds: Leds, shouldStop: Callable[[], bool]):
    ff = FirefliesWaves(50, flicker, ticksActiveRange=(2, 30), ticksBetweenWavesRange=(5, 150))

    while not shouldStop():
        leds.setLeds(ff.tick())

    ff.stop()

    while ff.isStopping():
        leds.setLeds(ff.tick())
