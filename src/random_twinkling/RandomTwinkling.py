from typing import List

from colour import Color

import random_twinkling.helpers as helpers
from utils.colours import off
from utils.gradients import createGradientFromBlack, createGradientToBlack

STEPS_FROM_OFF_TO_ON = 19
NUMBER_OF_STATES = STEPS_FROM_OFF_TO_ON * 2 - 1


class Bulb:
    def __init__(self):
        self.state = 0
        self.stateToColour: List[Color] = []

    def start(self, stateToColour: List[Color]):
        self.state = 1
        self.stateToColour = stateToColour

    def getColour(self):
        if len(self.stateToColour) == 0:
            return off
        else:
            return self.stateToColour[self.state]


class RandomTwinkling:
    def __init__(self, numberOfBulbs: int, colours: List[Color]):
        self.numberOfBulbs: int = numberOfBulbs
        self.counter: int = 0
        self.updateColours(colours)

        self.colour = 0

        self.shuffledBulbIndexes: List[int] = []
        self._shuffle()

        self.bulbs: List[Bulb] = [Bulb() for _ in range(numberOfBulbs)]

    def tick(self) -> List[Color]:
        # TODO Only do this sometimes, not every tick?
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
        if self.bulbs[bulbIndex].state == 0:
            self.bulbs[bulbIndex].start(self.stateToColourByColour[self.colour])
            self._incrementColour()

        return self.bulbs

    def _updateBulbs(self):
        for i in range(len(self.bulbs)):
            if self.bulbs[i].state == 0:
                pass
            elif self.bulbs[i].state >= NUMBER_OF_STATES - 1:
                self.bulbs[i].state = 0
            else:
                self.bulbs[i].state += 1

    def updateColours(self, colours: List[Color]):
        self.numberOfColours = len(colours)

        self.stateToColourByColour: List[List[Color]] = []

        for i in range(self.numberOfColours):
            up = createGradientFromBlack(colours[i], STEPS_FROM_OFF_TO_ON)
            down = createGradientToBlack(colours[i], STEPS_FROM_OFF_TO_ON)
            upAndDown: List[Color] = up + down[1:]
            self.stateToColourByColour.append(upAndDown)
