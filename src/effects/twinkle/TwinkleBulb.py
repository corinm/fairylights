from colour import Color

from utils.Bulb import Bulb
from utils.colours import off

from .helpers import calculateLuminance, correctForGamma


class TwinkleBulb(Bulb):
    def __init__(self, timeToPeak: float, maxLuminance: float, minLuminance: float):
        self._timeToPeak = timeToPeak
        self._maxLuminance = maxLuminance
        self._minLuminance = minLuminance
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

        self._time += timeDelta

        if self._time > self._timeToPeak * 2:
            self._isActive = False

        luminance = calculateLuminance(self._time, self._timeToPeak, self._maxLuminance, self._minLuminance)
        corrected = correctForGamma(luminance, self._maxLuminance)
        self._colour.set_luminance(corrected)

    def getColour(self):
        return self._colour

    def isReady(self):
        return not self._isActive
