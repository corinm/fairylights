from colour import Color

from utils.Bulb import Bulb
from utils.colours import off

from .helpers import calculateLuminance

TIME_TO_PEAK = 0.6  # Seconds
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

        self._time += timeDelta

        if self._time > TIME_TO_PEAK * 2:
            self._isActive = False

        luminance = calculateLuminance(self._time, TIME_TO_PEAK, MAX_LUMINANCE)
        self._colour.set_luminance(luminance)

    def getColour(self):
        return self._colour

    def isReady(self):
        return not self._isActive
