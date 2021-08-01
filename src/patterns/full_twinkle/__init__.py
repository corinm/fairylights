from typing import Callable

from leds.Leds import Leds
from utils.colours import coolors, retroColours  # noqa

from ..twinkle.Twinkle import Twinkle


def runFullTwinkleRetro(leds: Leds, shouldStop: Callable[[], bool]):
    pattern = Twinkle(
        50,
        [
            retroColours["pink"],
            retroColours["blue"],
            retroColours["orange"],
            retroColours["green"],
            retroColours["red"],
        ],
        timeBetweenTwinkles=0.01,
    )

    while not shouldStop():
        leds.setLeds(pattern.tick())

    pattern.stop()

    while pattern.isStopping():
        leds.setLeds(pattern.tick())
