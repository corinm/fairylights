from typing import List
from time import time

from colour import Color

from ..Effect import Effect
from colours.Colours import Colours


SECONDS_TO_CYCLE_ONCE = 10


class Cycle(Effect):
    def __init__(self, numberOfBulbs: int, colours: Colours):
        Effect.__init__(self)

        self._colours: Colours = colours
        self._numberOfBulbs = numberOfBulbs
        self._currentColours = self._colours.getColours(self._numberOfBulbs)

    def tick(self) -> List[Color]:
        now = time()
        timeDelta = self._getTimeDelta(now)

        # TODO: Make independent of tick rate

        self._currentColours = self._currentColours[1:] + self._currentColours[0:1]

        super().tick(now, self._currentColours)

        return self._currentColours
