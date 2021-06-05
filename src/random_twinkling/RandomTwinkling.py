from typing import List

from colour import Color

import random_twinkling.helpers as helpers
from utils.gradients import createGradientFromBlack, createGradientToBlack

off = Color()

STEPS_FROM_OFF_TO_ON = 19
NUMBER_OF_STATES = STEPS_FROM_OFF_TO_ON * 2 - 1


class RandomTwinkling:
    def __init__(self, numberOfBulbs: int, colours: List[Color]):
        self.numberOfBulbs: int = numberOfBulbs
        self.counter: int = 0

        self.stateToColourByColour: List[List[Color]] = []

        for i in range(len(colours)):
            up = createGradientFromBlack(colours[i], STEPS_FROM_OFF_TO_ON)
            down = createGradientToBlack(colours[i], STEPS_FROM_OFF_TO_ON)
            upAndDown: List[Color] = up + down[1:]
            self.stateToColourByColour.append(upAndDown)

        # self.stateToColour: List[Color] = up + down[1:]

        self.shuffledBulbIndexes: List[int] = []
        self.shuffle()

        self.bulbs: List[int] = [0 for _ in range(numberOfBulbs)]

    def tick(self) -> List[Color]:
        # TODO Only do this sometimes, not every tick?
        self.nextTwinkle()

        colour = 0
        colours: List[Color] = [
            self.stateToColourByColour[colour][state] for state in self.bulbs
        ]

        self.updateBulbs()

        return colours

    def shuffle(self):
        self.shuffledBulbIndexes = helpers.createShuffledList(self.numberOfBulbs)

    def nextTwinkle(self):
        if self.counter == len(self.shuffledBulbIndexes):
            self.shuffle()
            self.counter = 0

        bulb = self.shuffledBulbIndexes[self.counter]
        self.counter += 1

        # Only start a new twinkle if we're not mid-twinkle from a previous shuffle
        if self.bulbs[bulb] == 0:
            self.bulbs[bulb] = 1

        return self.bulbs

    def updateBulbs(self):
        for i in range(len(self.bulbs)):
            if self.bulbs[i] == 0:
                pass
            elif self.bulbs[i] >= NUMBER_OF_STATES - 1:
                self.bulbs[i] = 0
            else:
                self.bulbs[i] += 1
