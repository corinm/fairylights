import math
from typing import List

from colour import Color

from patterns.flickering_fairylights.FlickerBulb import BulbState
from utils.colours import flickerColours, flickerMid, off


def generateFullListOfColours(flickerBulbStates: List[BulbState]):
    numberOn = flickerBulbStates.count(BulbState.ON)
    numberDim = flickerBulbStates.count(BulbState.DIM)
    total = math.floor(numberOn + (numberDim / 2))

    on = flickerColours[total]

    bulbs = [
        determineBrightness(flickerBulbStates[0], on),
        on,
        on,
        on,
        on,
        determineBrightness(flickerBulbStates[1], on),
        on,
        on,
        on,
        on,
        determineBrightness(flickerBulbStates[2], on),
        on,
        on,
        on,
        on,
        determineBrightness(flickerBulbStates[3], on),
        on,
        on,
        on,
        on,
        determineBrightness(flickerBulbStates[4], on),
        on,
        on,
        on,
        on,
        determineBrightness(flickerBulbStates[5], on),
        on,
        on,
        on,
        on,
        determineBrightness(flickerBulbStates[6], on),
        on,
        on,
        on,
        on,
        determineBrightness(flickerBulbStates[7], on),
        on,
        on,
        on,
        on,
        determineBrightness(flickerBulbStates[8], on),
        on,
        on,
        on,
        on,
        determineBrightness(flickerBulbStates[9], on),
        on,
        on,
        on,
        on,
    ]

    return bulbs


def determineBrightness(bulbState: BulbState, on: Color):
    if bulbState == BulbState.ON:
        return on
    elif bulbState == BulbState.DIM:
        return flickerMid
    else:
        return off
