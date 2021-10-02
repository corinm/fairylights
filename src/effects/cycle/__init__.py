from typing import List, Callable

from colour import Color

from .. import Effect
from colours.Colours import Colours


class Cycle(Effect):
    def __init__(self, numberOfBulbs: int, colours: Colours):
        Effect.__init__(self)
        self._numberOfBulbs = numberOfBulbs
        self._colours = colours(numberOfBulbs=numberOfBulbs)

    def tick(self) -> List[Color]:
        now = 0
        colours = self._colours.getColours()
        super().tick(now, colours)
        return colours

# class CycleFromAlgorithm(Effect):
#     def __init__(self, numberOfBulbs: int, colourGenerator: Callable[[int], Callable[[], Color]]):
#         self._numberOfBulbs = numberOfBulbs
#         self._colourGenerator = colourGenerator
#         self._colours = self._colourGenerator(50)

#     def tick(self) -> List[Color]:
#         return self._colours
