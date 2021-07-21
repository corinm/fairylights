from time import time
from typing import List

from colour import Color

from utils.Bulb import Bulb
from utils.gradients import createGradientFromAndToBlack
from utils.ShuffledBulbs import ShuffledBulbs

from .TwinkleBulb import TwinkleBulb

STEPS_FROM_OFF_TO_ON = 60
NUMBER_OF_STATES = STEPS_FROM_OFF_TO_ON * 2 - 1


def allOff(colours: List[Color]) -> bool:
    return all(c == Color(None) for c in colours)


class RandomTwinkling:
    def __init__(self, numberOfBulbs: int, colours: List[Color]):
        self.updateColours(colours)
        self.currentColourIndex: int = 0
        bulbs: List[Bulb] = [TwinkleBulb(NUMBER_OF_STATES) for _ in range(numberOfBulbs)]
        self.shuffledBulbs = ShuffledBulbs(bulbs)
        self._stopping = False
        self._ticksUntilCheck = 15
        self._count = 0

    def tick(self) -> List[Color]:
        if not self._stopping and self._count >= 4:
            self._count = 0
            self._nextTwinkle()

        self._count += 1

        colours: List[Color] = [bulb.getColour() for bulb in self.shuffledBulbs.getBulbs()]

        if self._stopping:
            self._ticksUntilCheck -= 1

        if self._stopping and self._ticksUntilCheck == 0 and allOff(colours):
            self._stopping = False

        if self._stopping and self._ticksUntilCheck == 0:
            self._ticksUntilCheck = 15

        [bulb.tick() for bulb in self.shuffledBulbs.getBulbs()]

        return colours

    def updateColours(self, colours: List[Color]):
        t1 = time()
        self.numberOfColours = len(colours)

        print(self.numberOfColours, colours)

        self.stateToColourByColour: List[List[Color]] = []

        for i in range(self.numberOfColours):
            stateToColour = createGradientFromAndToBlack(colours[i].hex, STEPS_FROM_OFF_TO_ON)
            self.stateToColourByColour.append(stateToColour)

        self.currentColourIndex = 0
        print(time() - t1)

    def stop(self):
        self._stopping = True

    def isStopping(self) -> bool:
        return self._stopping

    def _nextTwinkle(self):
        bulb = self.shuffledBulbs.getNextBulb()

        # Only start a new twinkle if we're not mid-twinkle from a previous shuffle
        if bulb.isReady():
            colour: Color = self.stateToColourByColour[self.currentColourIndex]
            bulb.start(colour)
            self._incrementColour()

        return self.shuffledBulbs.getBulbs()

    def _incrementColour(self):
        self.currentColourIndex += 1

        if self.currentColourIndex >= self.numberOfColours:
            self.currentColourIndex = 0
