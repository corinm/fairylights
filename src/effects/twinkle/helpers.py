import math
import random
from typing import List

from colour import Color


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


def calculateLuminance(timeNow: float, timeToPeak: float, maxLuminance: float):
    luminance = 0

    if timeNow < timeToPeak * 2:
        if timeNow <= timeToPeak:
            luminance = (timeNow * 100 / timeToPeak) * maxLuminance / 100
        else:
            luminance = (
                ((timeToPeak - (timeNow - timeToPeak)) * 100 / timeToPeak) * maxLuminance / 100
            )

    return luminance


# def createGradientFromBlack(colour: Color, steps: int) -> List[Color]:
#     r,g,b = int(colour.hex_l[1:3],16), int(colour.hex_l[3:5], 16), int(colour.hex_l[5:7], 16)
#     rs = [round((i / (steps - 1)) * r) for i in range(steps)]
#     gs = [round((i / (steps - 1)) * g) for i in range(steps)]
#     bs = [round((i / (steps - 1)) * b) for i in range(steps)]
#     colours = [Color(red=rs[i]/255,green=gs[i]/255,blue=bs[i]/255) for i in range(steps)]
#     print(colour.hex_l, rs, gs, bs, colours)
#     return colours


# def calculateColourFromLuminance(colour: Color, luminance: float) -> Color:
#     r,g,b = int(colour.hex_l[1:3],16), int(colour.hex_l[3:5], 16), int(colour.hex_l[5:7], 16)
#     r = round(r * luminance)
#     g = round(g * luminance)
#     b = round(b * luminance)
#     r = r if luminance > 0.04 else 0
#     g = g if luminance > 0.04 else 0
#     b = b if luminance > 0.04 else 0
#     return Color(red=r/255, green=g/255, blue=b/255)


GAMMA_CORRECTION = 2.8


def correctForGamma(luminance: float, maxLuminance: float) -> float:
    return pow(luminance / maxLuminance, GAMMA_CORRECTION) * maxLuminance