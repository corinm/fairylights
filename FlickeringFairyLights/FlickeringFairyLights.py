import math
from typing import List
from colour import Color

from FlickerBulb import BulbState, FlickerBulb
import constants

"""
This module simulates a set of flickering fairy lights described here: https://youtu.be/zeOw5MZWq24?t=268
Every 5th bulb is a flickering one which shorts out when it reaches a certain temperature
When a bulb shorts it turns off, which increases the voltage going to the remaining bulbs
This create the effect of 1 in 5 bulbs flickering on and off
And all the bulbs changing brightness depending on how many bulbs are of or off at a time

In the video he notes that the voltage will vary from 2.4V to 3V depending on how many bulbs are lit
However, I'm simulating that by simply counting the number of FlickerBulbs that are on
and setting all "on" bulbs to a colour within an 11-colour gradient based on that number (0 - 10)
where 0 = brightest and 10 = dimmest
"""


class FlickeringFairyLights:
    def __init__(self):
        f1 = FlickerBulb()
        f2 = FlickerBulb()
        f3 = FlickerBulb()
        f4 = FlickerBulb()
        f5 = FlickerBulb()
        f6 = FlickerBulb()
        f7 = FlickerBulb()
        f8 = FlickerBulb()
        f9 = FlickerBulb()
        f10 = FlickerBulb()

        self.flickerBulbs = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
        assert len(self.flickerBulbs) == 10

    def tick(self) -> List[Color]:
        [flickerBulb.tick() for flickerBulb in self.flickerBulbs]
        flickerBulbStates: list[BulbState] = list(
            map(lambda b: b.state, self.flickerBulbs))
        leds = generateFullListOfColours(flickerBulbStates)
        return leds


def generateFullListOfColours(flickerBulbStates: list(BulbState)):
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
