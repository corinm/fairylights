import math
from typing import List
import random


def createShuffledList(numberOfBulbs):
    numberOfBuckets = math.floor(numberOfBulbs / 10)
    buckets = [i for i in range(numberOfBuckets)]
    remainingIndexes: List[int] = [i for i in range(numberOfBulbs)]
    remainingIndexesByBucket: List[List[int]] = [[]
                                                 for i in range(numberOfBuckets)]

    for n in remainingIndexes:
        bucketIndex = math.floor(n / 10)
        remainingIndexesByBucket[bucketIndex].append(n)

    shuffledBulbIndexes: List[int] = []

    while len(remainingIndexes) > 0:
        random.shuffle(buckets)

        for bucketIndex in buckets:
            remainingIndexesInBucket = remainingIndexesByBucket[bucketIndex]
            chosenIndex = remainingIndexesInBucket[random.randrange(
                0, len(remainingIndexesInBucket))]

            remainingIndexesInBucket.remove(chosenIndex)
            remainingIndexes.remove(chosenIndex)

            shuffledBulbIndexes.append(chosenIndex)

    assert len(shuffledBulbIndexes) == numberOfBulbs

    return shuffledBulbIndexes
