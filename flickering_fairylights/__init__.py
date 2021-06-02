from .FlickeringFairyLights import FlickeringFairyLights

from time import sleep


def run(leds):
    ff = FlickeringFairyLights()

    while True:
        print('ff.tick')
        leds.setLeds(ff.tick())
        sleep(1)
