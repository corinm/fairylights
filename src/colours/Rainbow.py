from typing import List

from colour import Color

from .Colours import Colours
from utils.rainbow import rainbow

class Rainbow(Colours):
    def __init__(self, numberOfBulbs: int):
        self._colours = rainbow(numberOfBulbs)

    def getColours(self) -> List[Color]:
        return self._colours
