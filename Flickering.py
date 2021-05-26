from FlickerBulb import FlickerBulb
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

flickerBulbs = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
assert len(flickerBulbs) == 10


def tick() -> list:
    [flickerBulb.tick() for flickerBulb in flickerBulbs]
    flickerBulbsOn = list(map(lambda b: b.isOn, flickerBulbs))
    leds = generateFullListOfColours(flickerBulbsOn)
    return leds


def generateFullListOfColours(flickerBulbsOn: list):
    numberOn = flickerBulbsOn.count(True)
    on = ledColours.flickerColours[numberOn]

    bulbs = [
        on if flickerBulbsOn[0] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbsOn[1] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbsOn[2] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbsOn[3] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbsOn[4] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbsOn[5] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbsOn[6] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbsOn[7] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbsOn[8] == True else ledColours.off,
        on, on, on, on,
        on if flickerBulbsOn[9] == True else ledColours.off,
        on, on, on, on,
    ]

    assert len(bulbs) == 50

    return bulbs


tick()
