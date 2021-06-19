from random import randrange, shuffle
from typing import List, Set

from colour import Color

from utils.colours import off

from .Firefly import Firefly
from .patterns import staticGlow


class FirefliesConstant:
    def __init__(self):
        self.fireflies: List[Firefly] = []

    def tick(self) -> List[Color]:
        takenPositions: Set[int] = set([ff.position for ff in self.fireflies])
        emptyPositions: List[int] = list(filter(lambda x: x not in takenPositions, range(50)))
        shuffle(emptyPositions)

        numberOfNewFireflies = randrange(0, 8)
        for i in range(min(numberOfNewFireflies, len(emptyPositions))):
            ticksActive = randrange(0, 10)
            self.fireflies.append(Firefly(emptyPositions[i], staticGlow, ticksActive))

        colours = [off for i in range(50)]

        for firefly in self.fireflies:
            colour = firefly.tick()
            colours[firefly.position] = colour

        self.fireflies = [f for f in self.fireflies if not f.isDone]

        return colours
