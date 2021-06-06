import os
import sys
from datetime import datetime, timedelta
from typing import List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


from colour import Color  # noqa

from leds.Leds import Leds  # noqa
from utils.randomColour import randomColour  # noqa

from .RandomTwinkling import RandomTwinkling  # noqa


class RandomColours:
    def __init__(self, numberOfLeds: int):
        self.numberOfLeds = numberOfLeds
        self.resetTime()
        self.colours: List[Color] = [randomColour(), randomColour()]
        self.rt = RandomTwinkling(numberOfLeds, self.colours)

    def tick(self) -> List[Color]:
        if self.nextChange <= datetime.now():
            self.updateColours()
            self.resetTime()

        return self.rt.tick()

    def resetTime(self):
        self.nextChange = datetime.now() + timedelta(seconds=10)

    def updateColours(self):
        self.colours = [self.colours[1], randomColour()]
        self.rt.queueNewColours(self.colours)
