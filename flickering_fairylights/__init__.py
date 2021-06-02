from .FlickeringFairyLights import FlickeringFairyLights

from time import sleep


def run(leds):
    ff = FlickeringFairyLights()

    while True:
        leds.setLeds(ff.tick())
