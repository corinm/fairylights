from typing import List

import helpers


class RandomTwinkling:
    def __init__(self, numberOfBulbs: int):
        self.numberOfBulbs: int = numberOfBulbs
        self.counter: int = 0
        self.shuffledBulbIndexes: List[int] = []
        self.shuffle()

    def tick(self):
        if (self.counter == len(self.shuffledBulbIndexes)):
            self.shuffle()
            self.counter = 0

        # Return the next bulb and increment counter
        bulb = self.shuffledBulbIndexes[self.counter]
        self.counter += 1
        return bulb

    def shuffle(self):
        self.shuffledBulbIndexes = helpers.createShuffledList(
            self.numberOfBulbs)


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
