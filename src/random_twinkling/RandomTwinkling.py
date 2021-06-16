from time import time
from typing import List

from colour import Color

import random_twinkling.helpers as helpers
from random_twinkling.TwinkleBulb import TwinkleBulb
from utils.gradients import createGradientFromAndToBlack

STEPS_FROM_OFF_TO_ON = 19
NUMBER_OF_STATES = STEPS_FROM_OFF_TO_ON * 2 - 1


class RandomTwinkling:
    def __init__(self, numberOfBulbs: int, colours: List[Color]):
        self.numberOfBulbs: int = numberOfBulbs
        self.counter: int = 0

        self.updateColours(colours)

        self.currentColourIndex: int = 0

        self.shuffledBulbIndexes: List[int] = []
        self._shuffle()

        self.bulbs: List[TwinkleBulb] = [
            TwinkleBulb(NUMBER_OF_STATES) for _ in range(numberOfBulbs)
        ]

    def tick(self) -> List[Color]:
        self._nextTwinkle()

        colours: List[Color] = [bulb.getColour() for bulb in self.bulbs]

        self._updateBulbStates()

        return colours

    def updateColours(self, colours: List[Color]):
        t1 = time()
        self.numberOfColours = len(colours)

        self.stateToColourByColour: List[List[Color]] = []

        for i in range(self.numberOfColours):
            stateToColour = createGradientFromAndToBlack(
                colours[i].hex, STEPS_FROM_OFF_TO_ON
            )
            self.stateToColourByColour.append(stateToColour)

        self.currentColourIndex = 0
        print(time() - t1)

    def _incrementColour(self):
        self.currentColourIndex += 1

        if self.currentColourIndex >= self.numberOfColours:
            self.currentColourIndex = 0

    def _shuffle(self):
        self.shuffledBulbIndexes = helpers.createShuffledList(self.numberOfBulbs)

    def _nextTwinkle(self):
        if self.counter == len(self.shuffledBulbIndexes):
            self._shuffle()
            self.counter = 0

        bulb = self._getNextBulb()
        self.counter += 1

        # Only start a new twinkle if we're not mid-twinkle from a previous shuffle
        if bulb.isReady():
            colour: Color = self.stateToColourByColour[self.currentColourIndex]
            bulb.start(colour)
            self._incrementColour()

        return self.bulbs

    def _getNextBulb(self) -> TwinkleBulb:
        bulbIndex: int = self.shuffledBulbIndexes[self.counter]
        bulb: TwinkleBulb = self.bulbs[bulbIndex]
        return bulb

    def _updateBulbStates(self):
        for bulb in self.bulbs:
            bulb.tick()
