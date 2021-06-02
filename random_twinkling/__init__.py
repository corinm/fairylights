from .RandomTwinkling import RandomTwinkling

from time import sleep
from colour import Color


def run(leds):
    rt = RandomTwinkling(50, Color(color='blue'))

    while True:
        print('rt.tick')
        leds.setLeds(rt.tick())
        sleep(1)
