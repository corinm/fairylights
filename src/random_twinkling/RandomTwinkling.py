from time import time
from typing import Dict, List

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

        self.memo: Dict[Color, List[Color]] = {}
        self.updateColours(colours)

        self.colourIndex: int = 0

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
            stateToColour = self._memoisedCreateStateToColour(colours[i])
            self.stateToColourByColour.append(stateToColour)

        self.colourIndex = 0
        print(time() - t1)

    def _memoisedCreateStateToColour(self, colour: Color) -> List[Color]:
        if self.memo.get(colour.hex) is not None:
            return self.memo[colour.hex]
        else:
            upAndDown: List[Color] = createGradientFromAndToBlack(
                colour, STEPS_FROM_OFF_TO_ON
            )
            self.memo[colour.hex] = upAndDown
            return upAndDown

    def _incrementColour(self):
        self.colourIndex += 1

        if self.colourIndex >= self.numberOfColours:
            self.colourIndex = 0

    def _shuffle(self):
        self.shuffledBulbIndexes = helpers.createShuffledList(self.numberOfBulbs)

    def _nextTwinkle(self):
        if self.counter == len(self.shuffledBulbIndexes):
            self._shuffle()
            self.counter = 0

        bulbIndex: int = self.shuffledBulbIndexes[self.counter]
        bulb: TwinkleBulb = self.bulbs[bulbIndex]
        self.counter += 1

        # Only start a new twinkle if we're not mid-twinkle from a previous shuffle
        if bulb.isReady():
            colour: Color = self.stateToColourByColour[self.colourIndex]
            bulb.start(colour)
            self._incrementColour()

        return self.bulbs

    def _updateBulbStates(self):
        for bulb in self.bulbs:
            bulb.tick()
