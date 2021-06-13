from .Fireflies import Fireflies
from .patterns import flicker, staticGlow


def runStaticGlow(leds):
    ff = Fireflies(50, staticGlow)

    while True:
        leds.setLeds(ff.tick())


def runFlicker(leds):
    ff = Fireflies(50, flicker)

    while True:
        leds.setLeds(ff.tick())
