from typing import List

from colour import Color

from utils.Bulb import Bulb
from utils.colours import off


class TwinkleBulb(Bulb):
    def __init__(self, numberOfStates: int):
        self._numberOfStates: int = numberOfStates
        self._state: int = 0
        self._stateToColour: List[Color] = []

    def start(self, stateToColour: List[Color]):
        self._state = 1
        self._stateToColour = stateToColour

    def tick(self):
        if self._isNotTwinkling():
            pass
        elif self._hasFinished():
            self._resetState()
        else:
            self._incrementState()

    def getColour(self):
        return off if self._isNotTwinkling() else self._stateToColour[self._state]

    def isReady(self):
        return self._isNotTwinkling()

    def _isNotTwinkling(self) -> bool:
        return self._state == 0

    def _hasFinished(self) -> bool:
        return self._state >= self._numberOfStates - 1

    def _resetState(self) -> None:
        self._state = 0

    def _incrementState(self) -> None:
        self._state += 1
