from time import time
from typing import Dict, List

from colour import Color

import random_twinkling.helpers as helpers
from random_twinkling.TwinkleBulb import TwinkleBulb
from utils.gradients import createGradientFromBlack

STEPS_FROM_OFF_TO_ON = 19
NUMBER_OF_STATES = STEPS_FROM_OFF_TO_ON * 2 - 1


class RandomTwinkling:
    def __init__(self, numberOfBulbs: int, colours: List[Color]):
        self.numberOfBulbs: int = numberOfBulbs
        self.counter: int = 0

        self.memo: Dict[Color, List[Color]] = {}
        self.updateColours(colours)

        self.colour = 0

        self.shuffledBulbIndexes: List[int] = []
        self._shuffle()

        self.bulbs: List[TwinkleBulb] = [
            TwinkleBulb(NUMBER_OF_STATES) for _ in range(numberOfBulbs)
        ]

    def tick(self) -> List[Color]:
        self._nextTwinkle()

        colours: List[Color] = [bulb.getColour() for bulb in self.bulbs]

        self._updateBulbs()

        return colours

    def _incrementColour(self):
        self.colour += 1

        if self.colour >= self.numberOfColours:
            self.colour = 0

    def _shuffle(self):
        self.shuffledBulbIndexes = helpers.createShuffledList(self.numberOfBulbs)

    def _nextTwinkle(self):
        if self.counter == len(self.shuffledBulbIndexes):
            self._shuffle()
            self.counter = 0

        bulbIndex = self.shuffledBulbIndexes[self.counter]
        self.counter += 1

        # Only start a new twinkle if we're not mid-twinkle from a previous shuffle
        if self.bulbs[bulbIndex].isNotTwinkling():
            self.bulbs[bulbIndex].start(self.stateToColourByColour[self.colour])
            self._incrementColour()

        return self.bulbs

    def _updateBulbs(self):
        for i in range(len(self.bulbs)):
            if self.bulbs[i].isNotTwinkling():
                pass
            elif self.bulbs[i].hasFinished():
                self.bulbs[i].resetState()
            else:
                self.bulbs[i].incrementState()

    def updateColours(self, colours: List[Color]):
        t1 = time()
        self.numberOfColours = len(colours)

        self.stateToColourByColour: List[List[Color]] = []

        for i in range(self.numberOfColours):
            if self.memo.get(colours[i].hex) is not None:
                self.stateToColourByColour.append(self.memo[colours[i].hex])
            else:
                up = createGradientFromBlack(colours[i], STEPS_FROM_OFF_TO_ON)
                down = list(reversed(up))
                upAndDown: List[Color] = up + down[1:]
                self.memo[colours[i].hex] = upAndDown
                self.stateToColourByColour.append(upAndDown)

        self.colour = 0
        print(time() - t1)
