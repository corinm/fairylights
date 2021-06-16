from time import time
from typing import List

from colour import Color

import random_twinkling.helpers as helpers
from random_twinkling.TwinkleBulb import TwinkleBulb
from utils.gradients import createGradientFromAndToBlack

STEPS_FROM_OFF_TO_ON = 19
NUMBER_OF_STATES = STEPS_FROM_OFF_TO_ON * 2 - 1


class ShuffledBulbs:
    def __init__(self, numberOfBulbs: int):
        self.numberOfBulbs: int = numberOfBulbs
        self.counter: int = 0
        self.shuffledBulbIndexes: List[int] = []
        self._shuffle()
        self.bulbs: List[TwinkleBulb] = [
            TwinkleBulb(NUMBER_OF_STATES) for _ in range(numberOfBulbs)
        ]

    def _shuffle(self):
        self.shuffledBulbIndexes = helpers.createShuffledList(self.numberOfBulbs)

    def getNextBulb(self) -> TwinkleBulb:
        bulbIndex: int = self.shuffledBulbIndexes[self.counter]
        bulb: TwinkleBulb = self.bulbs[bulbIndex]
        self._incrementCounter()
        return bulb

    def _incrementCounter(self):
        self.counter += 1

        if self.counter == len(self.shuffledBulbIndexes):
            self._shuffle()
            self.counter = 0

    def getBulbs(self) -> List[TwinkleBulb]:
        return self.bulbs


class RandomTwinkling:
    def __init__(self, numberOfBulbs: int, colours: List[Color]):
        self.updateColours(colours)
        self.currentColourIndex: int = 0
        self.shuffledBulbs = ShuffledBulbs(numberOfBulbs)

    def tick(self) -> List[Color]:
        self._nextTwinkle()

        colours: List[Color] = [bulb.getColour() for bulb in self.shuffledBulbs.getBulbs()]

        [bulb.tick() for bulb in self.shuffledBulbs.getBulbs()]

        return colours

    def updateColours(self, colours: List[Color]):
        t1 = time()
        self.numberOfColours = len(colours)

        self.stateToColourByColour: List[List[Color]] = []

        for i in range(self.numberOfColours):
            stateToColour = createGradientFromAndToBlack(colours[i].hex, STEPS_FROM_OFF_TO_ON)
            self.stateToColourByColour.append(stateToColour)

        self.currentColourIndex = 0
        print(time() - t1)

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
