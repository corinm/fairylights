from typing import List

import random_twinkling.helpers as helpers

from .Bulb import Bulb


class ShuffledBulbs:
    def __init__(self, bulbs: List[Bulb]):
        self.bulbs = bulbs
        self.numberOfBulbs: int = len(bulbs)
        self.counter: int = 0
        self.shuffledBulbIndexes: List[int] = []
        self._shuffle()

    def _shuffle(self):
        self.shuffledBulbIndexes = helpers.createShuffledList(self.numberOfBulbs)

    def getNextBulb(self) -> Bulb:
        bulbIndex: int = self.shuffledBulbIndexes[self.counter]
        bulb: Bulb = self.bulbs[bulbIndex]
        self._incrementCounter()
        return bulb

    def _incrementCounter(self):
        self.counter += 1

        if self.counter == len(self.shuffledBulbIndexes):
            self._shuffle()
            self.counter = 0

    def getBulbs(self) -> List[Bulb]:
        return self.bulbs
