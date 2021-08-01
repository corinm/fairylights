from random import random, randrange, shuffle
from time import time
from typing import List, Set

from colour import Color

from utils.colours import off

from .Firefly import Firefly


def shouldAdd() -> bool:
    return random() < 0.05


class FirefliesConstant:
    def __init__(self, numberOfBulbs: int, *args, **kwargs):
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

        if len(self.fireflies) == 0:
            self._stopping = False

        return colours

    def _addMoreFireflies(self):
        takenPositions: Set[int] = set([ff.getPosition() for ff in self.fireflies])
        emptyPositions: List[int] = list(filter(lambda x: x not in takenPositions, range(50)))
        shuffle(emptyPositions)

        numberOfNewFireflies = randrange(1, 5)
        for i in range(min(numberOfNewFireflies, len(emptyPositions))):
            self.fireflies.append(Firefly(emptyPositions[i]))

    def stop(self):
        self._stopping = True

    def isStopping(self) -> bool:
        return self._stopping

    def _getTimeDelta(self, timeNow):
        td = timeNow - self._time
        self._time = timeNow
        return td
