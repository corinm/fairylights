import os
import sys
from datetime import datetime, timedelta
from typing import List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


from colour import Color  # noqa

from leds.Leds import Leds  # noqa

from .RandomTwinkling import RandomTwinkling  # noqa


class RandomColours(RandomTwinkling):
    def __init__(self, numberOfLeds: int):
        super().__init__(numberOfLeds, [])
        self.numberOfLeds = numberOfLeds
        self.resetTime()

    def tick(self) -> List[Color]:
        if self.nextChange <= datetime.now():
            self.updateColours()
            self.resetTime()

        return [Color() for _ in range(self.numberOfLeds)]

    def resetTime(self):
        self.nextChange = datetime.now() + timedelta(seconds=10)

    def updateColours(self):
        pass
