from .FirefliesConstant import FirefliesConstant
from .FirefliesWaves import FirefliesWaves
from .patterns import flicker, staticGlow


def runStaticGlow(leds):
    ff = FirefliesWaves(50, staticGlow, ticksActiveRange=(2, 30), ticksBetweenWavesRange=(5, 150))

    while True:
        leds.setLeds(ff.tick())


def runStaticGlowShorter(leds):
    ff = FirefliesConstant()

    while True:
        leds.setLeds(ff.tick())


def runFlicker(leds):
    ff = FirefliesWaves(50, flicker, ticksActiveRange=(2, 30), ticksBetweenWavesRange=(5, 150))

    while True:
        leds.setLeds(ff.tick())
