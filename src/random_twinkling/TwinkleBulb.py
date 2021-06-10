from typing import List

from colour import Color

from utils.colours import off


class TwinkleBulb:
    def __init__(self, numberOfStates: int):
        self._numberOfStates: int = numberOfStates
        self._state: int = 0
        self._stateToColour: List[Color] = []

    def start(self, stateToColour: List[Color]):
        self._state = 1
        self._stateToColour = stateToColour

    def getColour(self):
        return off if self.isNotTwinkling() else self._stateToColour[self._state]

    def isNotTwinkling(self) -> bool:
        return self._state == 0

    def hasFinished(self) -> bool:
        return self._state >= self._numberOfStates - 1

    def resetState(self) -> None:
        self._state = 0

    def incrementState(self) -> None:
        self._state += 1
