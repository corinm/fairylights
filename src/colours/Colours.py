from abc import ABC, abstractmethod
from typing import List, Callable

from colour import  Color

class Colours(ABC):
    @abstractmethod
    def getColours(self) -> List[Color]:
        pass


class ColoursFromList(Colours):
    def __init__(self, colours):
        self._colours = colours

    def getColours(self) -> List[Color]:
        return self._colours


class ColoursFromAlgorithm(Colours):
    def __init__(self, nextColour: Callable[[], Color], numberOfColours: int):
        self._nextColour = nextColour
        self._firstCall = True
        self._colours: List[Color] = [self._nextColour() for _ in range(numberOfColours)]

    def getColours(self) -> List[Color]:
        if self._firstCall:
            self._firstCall = False
            return self._colours

        self._colours.pop(0)
        self._colours.append(self._nextColour())

        return self._colours


class ColoursFromListOfPalettes(Colours):
    def __init__(self, palettes: List[List[Color]]):
        self._index = 0
        self._palettes = palettes
        self._numberOfPalettes = len(palettes)

        self._colours: List[Color] = self._palettes[self._index]

    def getColours(self) -> List[Color]:
        self._colours = self._palettes[self._index]

        self._index += 1

        if self._index >= self._numberOfPalettes:
            self._index = 0

        return self._colours
