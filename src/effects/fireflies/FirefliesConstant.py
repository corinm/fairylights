from random import random, randrange, shuffle
from time import time
from typing import List, Set

from colour import Color

from utils.colours import off

from .Firefly import Firefly
from ..Effect import Effect


def shouldAdd() -> bool:
    return random() < 0.05


class FirefliesConstant(Effect):
    def __init__(self, numberOfBulbs: int, *args, **kwargs):
        Effect.__init__(self)

        self._numberOfBulbs = numberOfBulbs
        self.fireflies: List[Firefly] = []
        self._stopping = False
        self._time = 0

    def tick(self) -> List[Color]:
        now = time()
        timeDelta = self._getTimeDelta(now)

        if not self._stopping and shouldAdd():
            self._addMoreFireflies()

        colours = [off for i in range(self._numberOfBulbs)]

        for firefly in self.fireflies:
            firefly.incrementTimeDelta(timeDelta)
            colour = firefly.getColour()
            position = firefly.getPosition()
            colours[position] = colour

        self.fireflies = [f for f in self.fireflies if not f.isDone()]

        super().tick(now, colours)

        return colours

    def _addMoreFireflies(self):
        takenPositions: Set[int] = set([ff.getPosition() for ff in self.fireflies])
        emptyPositions: List[int] = list(filter(lambda x: x not in takenPositions, range(self._numberOfBulbs)))
        shuffle(emptyPositions)

        numberOfNewFireflies = randrange(1, 5)
        for i in range(min(numberOfNewFireflies, len(emptyPositions))):
            self.fireflies.append(Firefly(emptyPositions[i]))
