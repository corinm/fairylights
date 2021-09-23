from time import time
from typing import List

from colour import Color

from utils.Bulb import Bulb
from utils.ShuffledBulbs import ShuffledBulbs

from .TwinkleBulb import TwinkleBulb


def allOff(colours: List[Color]) -> bool:
    return all(c == Color(None) for c in colours)


class Twinkle:
    def __init__(
        self,
        numberOfBulbs: int,
        colours: List[Color],
        timeBetweenTwinkles=0.08,
        timeToPeak=0.8,
        maxLuminance=0.2,
    ):
        bulbs: List[Bulb] = [TwinkleBulb(timeToPeak, maxLuminance) for _ in range(numberOfBulbs)]
        self.shuffledBulbs = ShuffledBulbs(bulbs)

        self._timeBetweenTwinkles = timeBetweenTwinkles

        self._numberOfBulbs = numberOfBulbs
        self.currentColourIndex: int = 0
        self.updateColours(colours)
        self._count = 0
        self._time = time()
        self._timeToNextTwinkle = self._time + self._timeBetweenTwinkles / self._numberOfBulbs / 50
        self._stopping = False
        self._timeToNextStoppedCheck = None

    def tick(self) -> List[Color]:
        now = time()
        timeDelta = self._getTimeDelta(now)

        if not self._stopping and now > self._timeToNextTwinkle:
            self._nextTwinkle()
            self._timeToNextTwinkle = now + self._timeBetweenTwinkles / self._numberOfBulbs / 50

        self._count += 1

        for bulb in self.shuffledBulbs.getBulbs():
            bulb.incrementTimeDelta(timeDelta)

        colours: List[Color] = [bulb.getColour() for bulb in self.shuffledBulbs.getBulbs()]

        if self._stopping:
            self._checkIfStopped(now, colours)

        self._time = time()

        return colours

    def _checkIfStopped(self, now: float, colours: List[Color]):
        if self._timeToNextStoppedCheck is not None and now >= self._timeToNextStoppedCheck:
            if allOff(colours):
                self._stopping = False

    def updateColours(self, colours: List[Color]):
        self.colours: List[Color] = colours
        self.numberOfColours = len(colours)
        self.currentColourIndex = 0

    def stop(self):
        self._stopping = True
        self._timeToNextStoppedCheck = time() + 0.2

    def isStopping(self) -> bool:
        return self._stopping

    def _nextTwinkle(self):
        bulb = self.shuffledBulbs.getNextBulb()

        # Only start a new twinkle if we're not mid-twinkle from a previous shuffle
        if bulb.isReady():
            colour = Color(self.colours[self.currentColourIndex])
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
