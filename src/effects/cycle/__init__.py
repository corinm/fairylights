from typing import List
from time import time

from colour import Color

from ..Effect import Effect
from colours.Colours import Colours


class Cycle(Effect):
    def __init__(self, numberOfBulbs: int, colours: Colours):
        Effect.__init__(self)

        self._colours = colours.getColours(numberOfBulbs)
        self._numberOfBulbs = numberOfBulbs
        self._currentColours = self._colours
        self._timeBetweenUpdates = 0.001
        self._timeOfNextUpdate = self._time + self._timeBetweenUpdates
        self._index = 0

    def tick(self) -> List[Color]:
        now = time()

        if self.isStopping():
            for c in self._currentColours:
                l = c.luminance - 0.01
                c.set_luminance(l if l > 0 else 0)

        if now < self._timeOfNextUpdate:
            return self._currentColours

        colours = self._colours[self._index:] + self._colours[0:self._index]
        self._index += 3
        if self._index >= self._numberOfBulbs:
            self._index -= self._numberOfBulbs

        super().tick(now, self._currentColours)

        self._timeOfNextUpdate = now + self._timeBetweenUpdates

        return colours
