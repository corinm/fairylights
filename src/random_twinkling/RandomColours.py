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
        randomColourAlgorithmGenerator: Callable[[int], Callable[[], Color]],
        secondsBetweenPaletteChanges=30,
        secondsBetweenColourChanges=10,
        numberOfColours=2,
    ):
        self.numberOfLeds: int = numberOfLeds
        self.randomColourAlgorithmGenerator: Callable[
            [int], Callable[[], Color]
        ] = randomColourAlgorithmGenerator
        self.randomColourAlgorithm: Callable[[], Color] = randomColourAlgorithmGenerator(
            numberOfColours
        )
        self.secondsBetweenPaletteChanges: int = secondsBetweenPaletteChanges
        self.secondsBetweenColourChanges: int = secondsBetweenColourChanges
        self.numberOfColours: int = numberOfColours

        self.colours: List[Color] = [
            self.randomColourAlgorithm() for _ in range(self.numberOfColours)
        ]
        self.rt = RandomTwinkling(self.numberOfLeds, self.colours)

        self._resetNewPaletteTime()
        self._resetNewColourTime()

    def tick(self) -> List[Color]:
        if self._readyForNewPalette():
            self._newPalette()

        elif self._readyForNewColour():
            self._newColour()

        return self.rt.tick()

    def _newPalette(self):
        self.randomColourAlgorithm = self.randomColourAlgorithmGenerator(self.numberOfColours)
        self.colours: List[Color] = [
            self.randomColourAlgorithm() for _ in range(self.numberOfColours)
        ]
        print("New palette:", [c.hex for c in self.colours])
        self.rt = RandomTwinkling(self.numberOfLeds, self.colours)
        self._resetNewPaletteTime()

    def _readyForNewColour(self) -> bool:
        return self.timeForNewColour <= datetime.now()

    def _readyForNewPalette(self) -> bool:
        return self.timeForNewPalette <= datetime.now()

    def _newColour(self):
        self.colours = self.colours[1:] + [self.randomColourAlgorithm()]
        print("New colour:", self.colours[len(self.colours) - 1].hex)
        self.rt.updateColours(self.colours)
        self._resetNewColourTime()

    def _resetNewPaletteTime(self):
        self.timeForNewPalette = datetime.now() + timedelta(
            seconds=self.secondsBetweenPaletteChanges
        )

    def _resetNewColourTime(self):
        self.timeForNewColour = datetime.now() + timedelta(seconds=self.secondsBetweenColourChanges)
