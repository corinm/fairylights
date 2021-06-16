import os
import sys
from datetime import datetime, timedelta

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from typing import Callable, List  # noqa

from colour import Color  # noqa

from leds.Leds import Leds  # noqa

from .RandomTwinkling import RandomTwinkling  # noqa


class RandomColours:
    def __init__(
        self,
        numberOfLeds: int,
        randomColourAlgorithm: Callable[[], Color],
        secondsBetweenColourChanges=10,
        numberOfColours=2,
    ):
        self.numberOfLeds = numberOfLeds
        self.randomColourAlgorithm: Callable[[], Color] = randomColourAlgorithm
        self.secondsBetweenColourChanges = secondsBetweenColourChanges
        self.numberOfColours: int = numberOfColours

        self.resetTime()
        self._newColours()

    def tick(self) -> List[Color]:
        if self.nextChange <= datetime.now():
            self.updateColours()
            self.resetTime()

        return self.rt.tick()

    def resetTime(self):
        self.nextChange = datetime.now() + timedelta(seconds=self.secondsBetweenColourChanges)

    def updateColours(self):
        self.colours = self.colours[1:] + [self.randomColourAlgorithm()]
        self.rt.updateColours(self.colours)

    def _newColours(self):
        self.colours: List[Color] = [
            self.randomColourAlgorithm() for _ in range(self.numberOfColours)
        ]
        self.rt = RandomTwinkling(self.numberOfLeds, self.colours)
