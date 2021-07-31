from typing import Callable

from leds.Leds import Leds

from .FirefliesConstant import FirefliesConstant


def runGlowConstant(leds: Leds, shouldStop: Callable[[], bool]):
    ff = FirefliesConstant()

    while not shouldStop():
        leds.setLeds(ff.tick())

    ff.stop()

    while ff.isStopping():
        leds.setLeds(ff.tick())

    print("--- Stopped")
