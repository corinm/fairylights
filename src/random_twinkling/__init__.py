import os
import sys
from typing import Dict, List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


from colour import Color  # noqa

from leds.Leds import Leds  # noqa

from .RandomTwinkling import RandomTwinkling  # noqa

blue80s = Color(rgb=(11 / 255, 77 / 255, 57 / 255))
pink80s = Color(rgb=(57 / 255, 11 / 255, 77 / 255))

# Retro Noma Pickwick fairy lights
pink = Color(rgb=(127 / 255, 0 / 255, 64 / 255))
blue = Color(rgb=(0 / 255, 21 / 255, 127 / 255))
orange = Color(rgb=(120 / 255, 68 / 255, 17 / 255))
green = Color(rgb=(57 / 255, 92 / 255, 46 / 255))

styles: Dict[str, List[Color]] = {
    "BLUE_PINK": [blue80s, pink80s],
    "RETRO": [pink, blue, orange, green],
}


def run(leds: Leds, style: str):
    rt = RandomTwinkling(50, styles[style])

    while True:
        leds.setLeds(rt.tick())
