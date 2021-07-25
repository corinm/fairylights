from random import randrange
from typing import List

from colour import Color

from utils.colours import off


class GlitterBulb:
    def __init__(self, colour: Color):
        self._colour: Color = colour
        self._pattern: List[int] = [randrange(0, 2) for _ in range(50)]
        self._counter: int = 0

    def tick(self) -> Color:
        isOn = self._pattern[self._counter]

        self._incrementCounter()

        return self._colour if isOn else off

    def _incrementCounter(self):
        self._counter += 1
        if self._counter >= 50:
            self._counter = 0


class Glitter:
    def __init__(self, numberOfBulbs: int, colours: List[Color]):
        self._bulbs: List[GlitterBulb] = [
            GlitterBulb(colours[i % len(colours)]) for i in range(numberOfBulbs)
        ]
        self._counter = 0
        self._updateColours()

    def tick(self) -> List[Color]:
        if self._skipTick():
            self._incrementCounter()
            return self._colours
        else:
            self._incrementCounter()
            self._updateColours()
            return self._colours

    def _skipTick(self):
        return self._counter % 4 != 0

    def _updateColours(self):
        self._colours: List[Color] = [bulb.tick() for bulb in self._bulbs]

    def _incrementCounter(self):
        self._counter += 1
        if self._counter >= 1000:
            self._counter = 0
