import math
import random
from typing import List


def createShuffledList(numberOfBulbs: int) -> List[int]:
    numberOfBuckets: int = math.floor(numberOfBulbs / 10)
    buckets: List[int] = [i for i in range(numberOfBuckets)]
    remainingIndexes: List[int] = [i for i in range(numberOfBulbs)]
    remainingIndexesByBucket: List[List[int]] = [[] for i in range(numberOfBuckets)]

    for n in remainingIndexes:
        bucketIndex: int = math.floor(n / 10)
        remainingIndexesByBucket[bucketIndex].append(n)

    shuffledBulbIndexes: List[int] = []

    while len(remainingIndexes) > 0:
        random.shuffle(buckets)

        for bucketIndex in buckets:
            remainingIndexesInBucket: List[int] = remainingIndexesByBucket[bucketIndex]
            chosenIndex: int = remainingIndexesInBucket[
                random.randrange(0, len(remainingIndexesInBucket))
            ]

            remainingIndexesInBucket.remove(chosenIndex)
            remainingIndexes.remove(chosenIndex)

            shuffledBulbIndexes.append(chosenIndex)

    assert len(shuffledBulbIndexes) == numberOfBulbs

    return shuffledBulbIndexes
