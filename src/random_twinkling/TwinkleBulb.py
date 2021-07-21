from colour import Color

from utils.Bulb import Bulb
from utils.colours import off

from .helpers import calculateLuminance

TIME_TO_PEAK = 0.8  # Seconds
MAX_LUMINANCE = 0.15


class TwinkleBulb(Bulb):
    def __init__(self):
        self._time = 0
        self._isActive = False
        self._colour = off

    def setColourAtPeak(self, colour):
        self._colourAtPeak: Color = colour
        self._colour = colour
        self._colour.set_luminance(0)
        self._isActive = True
        self._time = 0

    def incrementTimeDelta(self, timeDelta):
        if not self._isActive:
            return off

        print("Is active")

        self._time += timeDelta

        if self._time > TIME_TO_PEAK * 2:
            self._isActive = False

        luminance = calculateLuminance(self._time, TIME_TO_PEAK, MAX_LUMINANCE)
        print(self._time, luminance)
        self._colour.set_luminance(luminance)

    def getColour(self):
        return self._colour

    # def isDone(self):
    #     return not self._isActive

    def isReady(self):
        return not self._isActive

    # def __init__(self, numberOfStates: int):
    #     self._numberOfStates: int = numberOfStates
    #     self._state: int = 0
    #     self._stateToColour: List[Color] = []

    # def start(self, stateToColour: List[Color]):
    #     self._state = 1
    #     self._stateToColour = stateToColour

    # def tick(self):
    #     if self._isNotTwinkling():
    #         pass
    #     elif self._hasFinished():
    #         self._resetState()
    #     else:
    #         self._incrementState()

    # def getColour(self):
    #     return off if self._isNotTwinkling() else self._stateToColour[self._state]

    # def isReady(self):
    #     return self._isNotTwinkling()

    # def _isNotTwinkling(self) -> bool:
    #     return self._state == 0

    # def _hasFinished(self) -> bool:
    #     return self._state >= self._numberOfStates - 1

    # def _resetState(self) -> None:
    #     self._state = 0

    # def _incrementState(self) -> None:
    #     self._state += 1
