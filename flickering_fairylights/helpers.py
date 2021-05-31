from typing import List
import math
from colour import Color

from flickering_fairylights.FlickerBulb import BulbState
import flickering_fairylights.constants as constants


def generateFullListOfColours(flickerBulbStates: List[BulbState]):
    numberOn = flickerBulbStates.count(BulbState.ON)
    numberDim = flickerBulbStates.count(BulbState.DIM)
    total = math.floor(numberOn + (numberDim / 2))

    on = constants.flickerColours[total]

    bulbs = [
        determineBrightness(flickerBulbStates[0], on),
        on, on, on, on,
        determineBrightness(flickerBulbStates[1], on),
        on, on, on, on,
        determineBrightness(flickerBulbStates[2], on),
        on, on, on, on,
        determineBrightness(flickerBulbStates[3], on),
        on, on, on, on,
        determineBrightness(flickerBulbStates[4], on),
        on, on, on, on,
        determineBrightness(flickerBulbStates[5], on),
        on, on, on, on,
        determineBrightness(flickerBulbStates[6], on),
        on, on, on, on,
        determineBrightness(flickerBulbStates[7], on),
        on, on, on, on,
        determineBrightness(flickerBulbStates[8], on),
        on, on, on, on,
        determineBrightness(flickerBulbStates[9], on),
        on, on, on, on,
    ]

    assert len(bulbs) == 50

    return bulbs


def determineBrightness(bulbState: BulbState, on: Color):
    if bulbState == BulbState.ON:
        return on
    elif bulbState == BulbState.DIM:
        return constants.flickerMid
    else:
        return constants.off
