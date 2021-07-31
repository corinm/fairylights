from typing import Callable

from colour import Color

from leds.Leds import Leds

from ..twinkle.Twinkle import Twinkle

pleasantWhite = Color(rgb=(90 / 255, 86 / 255, 9 / 255))


def runGlitterWarm(leds: Leds, shouldStop: Callable[[], bool]):
    g = Twinkle(
        50,
        [pleasantWhite],
        timeBetweenTwinkles=0.2,
        timeToPeak=0.3,
        maxLuminance=0.03,
    )

    while not shouldStop():
        leds.setLeds(g.tick())

    g.stop()

    while g.isStopping():
        leds.setLeds(g.tick())
