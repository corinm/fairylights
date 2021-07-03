from random import random

from .FlickeringFairyLights import FlickeringFairyLights


def run(leds):
    ff = FlickeringFairyLights()
    id = random()

    while True:
        print("Loop", id)
        leds.setLeds(ff.tick())
