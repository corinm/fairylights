from time import time
from typing import List

from colour import Color

from utils.Bulb import Bulb
from utils.ShuffledBulbs import ShuffledBulbs
from colours.Colours import Colours

from .TwinkleBulb import TwinkleBulb
from .. import Effect


UNIQUE_BULBS = 25


class Twinkle(Effect):
    def __init__(
        self,
        numberOfBulbs: int,
        colours: Colours,
        timeBetweenTwinkles=0.08,
        timeToPeak=0.8,
        maxLuminance=0.2,
        secondsBetweenColourChanges=10,
    ):
        Effect.__init__(self)
        
        self.colours: Colours = colours
        self.updateColours()

        bulbs: List[Bulb] = [TwinkleBulb(timeToPeak, maxLuminance) for _ in range(UNIQUE_BULBS)]
        self.shuffledBulbs = ShuffledBulbs(bulbs)

        self._timeBetweenTwinkles = timeBetweenTwinkles

        self._numberOfBulbs = numberOfBulbs
        self.currentColourIndex: int = 0
        self._count = 0
        self._timeToNextTwinkle = self._time + self._timeBetweenTwinkles
        self.secondsBetweenColourChanges = secondsBetweenColourChanges
        self._resetNewColourTime()

    def tick(self) -> List[Color]:
        now = time()
        timeDelta = self._getTimeDelta(now)

        if not self.isStopping() and now > self._timeToNextTwinkle:
            self._nextTwinkle()
            self._timeToNextTwinkle = now + self._timeBetweenTwinkles

        if self._readyForNewColour():
            self.currentColours = self.colours.getColours()
            print(self.currentColours)
            self._resetNewColourTime()

        self._count += 1

        for bulb in self.shuffledBulbs.getBulbs():
            bulb.incrementTimeDelta(timeDelta)

        colours: List[Color] = [bulb.getColour() for bulb in self.shuffledBulbs.getBulbs()]

        super().tick(now, colours)

        return colours * int(self._numberOfBulbs / UNIQUE_BULBS)

    def _readyForNewColour(self) -> bool:
        now = time()
        return now >= self.timeForNewColour

    def updateColours(self):
        self.currentColours = self.colours.getColours()
        self.numberOfColours = len(self.currentColours)
        self.currentColourIndex = 0

    def _nextTwinkle(self):
        bulb = self.shuffledBulbs.getNextBulb()

        # Only start a new twinkle if we're not mid-twinkle from a previous shuffle
        if bulb.isReady():
            colour = Color(self.currentColours[self.currentColourIndex])
            bulb.setColourAtPeak(colour)
            self._incrementColour()

    def _incrementColour(self):
        self.currentColourIndex += 1

        if self.currentColourIndex >= self.numberOfColours:
            self.currentColourIndex = 0

    def _resetNewColourTime(self):
        self.timeForNewColour = time() + self.secondsBetweenColourChanges
