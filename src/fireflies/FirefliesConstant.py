from random import random, randrange, shuffle
from typing import List, Set

from colour import Color

from utils.colours import off

from .Firefly import Firefly
from .patterns import staticGlow


def shouldAdd() -> bool:
    return random() < 0.2


class FirefliesConstant:
    def __init__(self):
        self.fireflies: List[Firefly] = []
        self._stopping = False

    def tick(self) -> List[Color]:
        if shouldAdd():
            self._addMoreFireflies()

        colours = [off for i in range(50)]

        for firefly in self.fireflies:
            colour = firefly.tick()
            colours[firefly.position] = colour

        self.fireflies = [f for f in self.fireflies if not f.isDone]

        return colours

    def _addMoreFireflies(self):
        takenPositions: Set[int] = set([ff.position for ff in self.fireflies])
        emptyPositions: List[int] = list(filter(lambda x: x not in takenPositions, range(50)))
        shuffle(emptyPositions)

        numberOfNewFireflies = randrange(1, 5)
        for i in range(min(numberOfNewFireflies, len(emptyPositions))):
            ticksActive = randrange(0, 5)
            steps = randrange(4, 9)
            self.fireflies.append(Firefly(emptyPositions[i], staticGlow, ticksActive, steps=steps))

    def stop(self):
        self._stopping = True

    def isStopping(self) -> bool:
        return self._stopping
