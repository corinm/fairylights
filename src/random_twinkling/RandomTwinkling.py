from time import time
from typing import List

from colour import Color

from utils.Bulb import Bulb
from utils.ShuffledBulbs import ShuffledBulbs

from .TwinkleBulb import TwinkleBulb

STEPS_FROM_OFF_TO_ON = 60
NUMBER_OF_STATES = STEPS_FROM_OFF_TO_ON * 2 - 1


def allOff(colours: List[Color]) -> bool:
    return all(c == Color(None) for c in colours)


class RandomTwinkling:
    def __init__(self, numberOfBulbs: int, colours: List[Color]):
        bulbs: List[Bulb] = [TwinkleBulb() for _ in range(numberOfBulbs)]
        self.shuffledBulbs = ShuffledBulbs(bulbs)
        self.currentColourIndex: int = 0
        self.updateColours(colours)
        self._stopping = False
        self._ticksUntilCheck = 15
        self._count = 0
        self._time = time()
        self._timeToNextTwinkle = self._time + 0.2

    def tick(self) -> List[Color]:
        now = time()
        timeDelta = self._getTimeDelta(now)

        # TODO: Do this based on amount of time passed
        if not self._stopping and now > self._timeToNextTwinkle:
            self._nextTwinkle()
            self._timeToNextTwinkle = now + 0.2

        self._count += 1

        for bulb in self.shuffledBulbs.getBulbs():
            bulb.incrementTimeDelta(timeDelta)

        colours: List[Color] = [bulb.getColour() for bulb in self.shuffledBulbs.getBulbs()]

        if self._stopping:
            self._ticksUntilCheck -= 1

        if self._stopping and self._ticksUntilCheck == 0 and allOff(colours):
            self._stopping = False

        if self._stopping and self._ticksUntilCheck == 0:
            self._ticksUntilCheck = 15

        self._time = time()

        print(colours)

        return colours

    def updateColours(self, colours: List[Color]):
        self.colours: List[Color] = colours
        self.numberOfColours = len(colours)
        self.currentColourIndex = 0

    def stop(self):
        self._stopping = True

    def isStopping(self) -> bool:
        return self._stopping

    def _nextTwinkle(self):
        print("Twinkle")
        bulb = self.shuffledBulbs.getNextBulb()

        # Only start a new twinkle if we're not mid-twinkle from a previous shuffle
        print("Is ready", bulb.isReady())
        if bulb.isReady():
            colour = Color(self.colours[self.currentColourIndex])
            print("**** colour", colour)
            bulb.setColourAtPeak(colour)
            self._incrementColour()

    def _incrementColour(self):
        self.currentColourIndex += 1

        if self.currentColourIndex >= self.numberOfColours:
            self.currentColourIndex = 0

    def _getTimeDelta(self, timeNow):
        td = timeNow - self._time
        self._time = timeNow
        return td
