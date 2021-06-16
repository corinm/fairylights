from typing import List

from colour import Color


class Bulb:
    def __init__(self, numberOfStates: int) -> None:
        pass

    def tick(self):
        pass

    def start(self, stateToColour: List[Color]) -> None:
        pass

    def getColour(self) -> Color:
        pass
