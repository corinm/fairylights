from typing import Dict, List


class RandomTwinkling:
    def __init__(self, numberOfBulbs: int):
        self.numberOfBulbs = numberOfBulbs
        self.shuffledBulbIndexes: List[int] = []
        self.counter = 0

        # Divide bulbs into buckets of 10
        self.buckets: Dict[int, bool] = {}
        numberOfBuckets = int(numberOfBulbs / 10)
        for i in range(numberOfBuckets):
            self.buckets[i] = False

    def tick(self):
        if (self.counter == len(self.shuffledBulbIndexes)):
            self.createShuffledList()
            self.counter = 0
        pass

        # Return the next bulb and increment counter
        bulb = self.shuffledBulbIndexes[self.counter]
        self.counter += 1
        return bulb

    def createShuffledList(self):
        # Choose random bucket
        # [0,1,2,3,4] buckets - shuffle
        # pick in turn, when get to end, shuffle and repeat
        # Until all bulbs have been picked
        # Perhaps need a datra structure to represent the buckets - hashmap?
        # Otherwise it'll be hard to keep track of what's already been picked

        # Pick random bulb from bucket
        # Append bulb to list

        # From remaining buckets, repeat

        # If all buckets have been selected from, reset buckets
        pass
