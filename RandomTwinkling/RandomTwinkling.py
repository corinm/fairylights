from typing import Dict, List
from colours import Color

import helpers

stateToColour: Dict[int, Color] = {}


class RandomTwinkling:
    def __init__(self, numberOfBulbs: int):
        self.numberOfBulbs: int = numberOfBulbs
        self.counter: int = 0
        self.shuffledBulbIndexes: List[int] = []
        self.shuffle()

        self.bulbs: List[int] = [0 for i in range(numberOfBulbs)]

    def tick(self) -> List[Color]:
        # TODO Only do this sometimes, not every tick?
        self.nextTwinkle()

        colours: List[Color] = [stateToColour[state] for state in self.bulbs]

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

        return self.bulbs


rt = RandomTwinkling(50)
print(rt.counter, rt.shuffledBulbIndexes)
rt.tick()
print(rt.counter, rt.shuffledBulbIndexes)
rt.tick()
print(rt.counter, rt.shuffledBulbIndexes)
rt.tick()
print(rt.counter, rt.shuffledBulbIndexes)
rt.tick()
print(rt.counter, rt.shuffledBulbIndexes)
