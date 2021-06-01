from typing import List
from colour import Color

import random_twinkling.helpers as helpers

off = Color()


class RandomTwinkling:
    def __init__(self, numberOfBulbs: int, colour: Color):
        self.numberOfBulbs: int = numberOfBulbs
        self.colour = colour
        self.counter: int = 0

        self.stateToColour: List[Color] = list(off.range_to(colour, 4))

        self.shuffledBulbIndexes: List[int] = []
        self.shuffle()

        self.bulbs: List[int] = [0 for _ in range(numberOfBulbs)]

    def tick(self) -> List[Color]:
        # TODO Only do this sometimes, not every tick?
        self.nextTwinkle()

        colours: List[Color] = [self.stateToColour[state]
                                for state in self.bulbs]

        self.updateBulbs()

        return colours

    def shuffle(self):
        self.shuffledBulbIndexes = helpers.createShuffledList(
            self.numberOfBulbs)

    def nextTwinkle(self):
        if (self.counter == len(self.shuffledBulbIndexes)):
            self.shuffle()
            self.counter = 0

        bulb = self.shuffledBulbIndexes[self.counter]
        self.counter += 1

        self.bulbs[bulb] = 1

        return self.bulbs

    def updateBulbs(self):
        print(self.bulbs)
        for i in range(len(self.bulbs)):
            if self.bulbs[i] == 0:
                pass
            elif self.bulbs[i] >= 3:
                self.bulbs[i] = 0
            else:
                self.bulbs[i] += 1
