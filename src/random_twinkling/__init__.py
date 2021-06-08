import os
import sys
from typing import Dict, List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


from colour import Color  # noqa

from leds.Leds import Leds  # noqa
from utils.randomColour import randomColour as trulyRandom  # noqa
from utils.randomColour import randomColourAnalogous  # noqa

from .RandomColours import RandomColours  # noqa
from .RandomTwinkling import RandomTwinkling  # noqa

blue80s = Color(rgb=(11 / 255, 77 / 255, 57 / 255))
pink80s = Color(rgb=(57 / 255, 11 / 255, 77 / 255))

# Retro Noma Pickwick fairy lights
pink = Color(rgb=(93 / 255, 19 / 255, 56 / 255))
blue = Color(rgb=(0 / 255, 73 / 255, 127 / 255))
orange = Color(rgb=(199 * 0.8 / 255, 90 * 0.8 / 255, 0 * 0.8 / 255))
green = Color(rgb=(54 * 0.4 / 255, 139 / 255, 27 * 0.4 / 255))
red = Color(rgb=(184 * 0.7 / 255, 44 * 0.4 / 255, 8 * 0.4 / 255))

styles: Dict[str, List[Color]] = {
    "BLUE_PINK": [blue80s, pink80s],
    "RETRO": [pink, blue80s, orange, green, red],
}


def run(leds: Leds, style: str):
    rt = RandomTwinkling(50, styles[style])

    while True:
        leds.setLeds(rt.tick())


def runRandomColours(leds: Leds):
    rc = RandomColours(50, trulyRandom)

    while True:
        leds.setLeds(rc.tick())


def runRandomAnalagousColours(leds: Leds):
    func = randomColourAnalogous()
    rac = RandomColours(50, func)

    while True:
        leds.setLeds(rac.tick())
