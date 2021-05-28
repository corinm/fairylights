import math
from typing import List
from colour import Color

from FlickerBulb import BulbState, FlickerBulb
import ledColours

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

    on = ledColours.flickerColours[total]

    bulbs = [
        on if flickerBulbStates[0] == BulbState.ON else ledColours.off,
        on, on, on, on,
        on if flickerBulbStates[1] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbStates[2] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbStates[3] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbStates[4] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbStates[5] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbStates[6] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbStates[7] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbStates[8] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbStates[9] == True else ledColours.off,
        on, on, on, on,
    ]

    assert len(bulbs) == 50

    return bulbs
