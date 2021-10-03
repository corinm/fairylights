import math
import random
from typing import List


# TODO: Remove this magic number
NUMBER_OF_BULBS_IN_A_BUCKET = 5


def createShuffledList(numberOfBulbs: int) -> List[int]:
    numberOfBuckets: int = math.floor(numberOfBulbs / NUMBER_OF_BULBS_IN_A_BUCKET)
    buckets: List[int] = [i for i in range(numberOfBuckets)]
    remainingIndexes: List[int] = [i for i in range(numberOfBulbs)]
    remainingIndexesByBucket: List[List[int]] = [[] for i in range(numberOfBuckets)]

    for n in remainingIndexes:
        bucketIndex: int = math.floor(n / NUMBER_OF_BULBS_IN_A_BUCKET)
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


def calculateLuminance(timeNow: float, timeToPeak: float, maxLuminance: float, minLuminance: float = 0):
    luminance = 0

    if timeNow < timeToPeak * 2:
        if timeNow <= timeToPeak:
            startTime = 0
            oldRange = timeToPeak - 0
            newRange = (maxLuminance * 100 - minLuminance * 100) / 100
            luminance = (((timeNow - startTime) * newRange) / oldRange) + minLuminance
            print(minLuminance, maxLuminance)
            print(timeNow, startTime, newRange, oldRange)
            print((((timeNow * 100 - startTime * 100) * newRange) / oldRange / 100))
            # luminance = (timeNow / timeToPeak) * maxLuminance + minLuminance
            # luminance = (timeNow * 100 / timeToPeak) * maxLuminance / 100
        else:
            luminance = (
                ((timeToPeak - (timeNow - timeToPeak)) * 100 / timeToPeak) * maxLuminance / 100
            )

    return luminance


GAMMA_CORRECTION = 2.8


def correctForGamma(luminance: float, maxLuminance: float) -> float:
    return pow(luminance / maxLuminance, GAMMA_CORRECTION) * maxLuminance