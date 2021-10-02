from typing import List

from colour import Color

from .. import Effect
from colours.Colours import Colours


class Cycle(Effect):
    def __init__(self, numberOfBulbs: int, colours: Colours):
        Effect.__init__(self)

        self._colours: Colours = colours
        self._numberOfBulbs = numberOfBulbs

    def tick(self) -> List[Color]:
        now = 0
        colours = self._colours.getColours()
        super().tick(now, colours)
        return colours
