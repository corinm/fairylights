from typing import Callable

from leds.Leds import Leds

from .FirefliesConstant import FirefliesConstant
from .FirefliesWaves import FirefliesWaves
from .patterns import flicker, staticGlow


def runStaticGlow(leds: Leds, shouldStop: Callable[[], bool]):
    ff = FirefliesWaves(
        50, staticGlow, ticksActiveRange=(40, 120), ticksBetweenWavesRange=(50, 400)
    )

    while not shouldStop():
        leds.setLeds(ff.tick())

    ff.stop()

    while ff.isStopping():
        leds.setLeds(ff.tick())

    print("--- Stopped")


def runStaticGlowShorter(leds: Leds, shouldStop: Callable[[], bool]):
    ff = FirefliesConstant()

    while not shouldStop():
        leds.setLeds(ff.tick())

    ff.stop()

    while ff.isStopping():
        leds.setLeds(ff.tick())

    print("--- Stopped")


def runFlicker(leds: Leds, shouldStop: Callable[[], bool]):
    ff = FirefliesWaves(
        50, flicker, ticksActiveRange=(2 * 4, 30 * 4), ticksBetweenWavesRange=(5 * 4, 150 * 4)
    )

    while not shouldStop():
        leds.setLeds(ff.tick())

    ff.stop()

    while ff.isStopping():
        leds.setLeds(ff.tick())

    print("--- Stopped")
