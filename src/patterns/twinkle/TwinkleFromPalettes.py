import os
import sys
from datetime import datetime, timedelta

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from random import randrange  # noqa
from typing import Callable, List  # noqa

from colour import Color  # noqa

from leds.Leds import Leds  # noqa

from .Twinkle import Twinkle  # noqa


class TwinkleFromPalettes:
    def __init__(
        self,
        numberOfLeds: int,
        palettes: List[List[Color]],
        secondsBetweenPaletteChanges=30,
        timeBetweenTwinkles=0.08,
    ):
        self.numberOfLeds: int = numberOfLeds
        self.palettes: List[List[Color]] = palettes
        self.secondsBetweenPaletteChanges: int = secondsBetweenPaletteChanges

        newPaletteIndex = randrange(len(self.palettes))
        self.colours: List[Color] = self.palettes[newPaletteIndex]
        print("    New palette:", [c.hex for c in self.colours])
        self.rt = Twinkle(self.numberOfLeds, self.colours, timeBetweenTwinkles=timeBetweenTwinkles)

        self._resetNewPaletteTime()

    def tick(self) -> List[Color]:
        if self._readyForNewPalette():
            self._newPalette()

        return self.rt.tick()

    def _newPalette(self):
        newPaletteIndex = randrange(len(self.palettes))
        self.colours: List[Color] = self.palettes[newPaletteIndex]
        print("    New palette:", [c.hex for c in self.colours])
        self.rt.updateColours(self.colours)
        self._resetNewPaletteTime()

    def _readyForNewPalette(self) -> bool:
        if self.secondsBetweenPaletteChanges == 0:
            return False
        else:
            return self.timeForNewPalette <= datetime.now()

    def _resetNewPaletteTime(self):
        self.timeForNewPalette = datetime.now() + timedelta(
            seconds=self.secondsBetweenPaletteChanges
        )

    def stop(self):
        self.rt.stop()

    def isStopping(self) -> bool:
        return self.rt.isStopping()
