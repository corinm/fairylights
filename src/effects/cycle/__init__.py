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
        self._timeBetweenUpdates = 0.08
        self._timeOfNextUpdate = self._time + self._timeBetweenUpdates

    def tick(self) -> List[Color]:
        now = time()

        if now < self._timeOfNextUpdate:
            return self._currentColours

        if self.isStopping():
            for c in self._currentColours:
                l = c.luminance - 0.01
                c.set_luminance(l if l > 0 else 0)

        self._currentColours = self._currentColours[1:] + self._currentColours[0:1]

        super().tick(now, self._currentColours)
        
        self._timeOfNextUpdate = now + self._timeBetweenUpdates

        return self._currentColours
