from time import time
from typing import List

from colour import Color


def allOff(colours: List[Color]) -> bool:
    return all(c == Color(None) for c in colours)

class Effect:
    """Effect base class which provides required behaviour for managing passage of time and stopping"""

    def __init__(self):
        self._stopping = False
        self._timeToNextStoppedCheck = None
        self._time = time()

    def tick(self, now, colours) -> None:
        if self._stopping:
            self._checkIfStopped(now, colours)

        self._time = now

    def _getTimeDelta(self, timeNow) -> int:
        return timeNow - self._time
    
    def stop(self) -> None:
        """Begins to the stopping process"""
        self._stopping = True
        self._timeToNextStoppedCheck = time() + 0.2

    def isStopping(self) -> bool:
        return self._stopping

    def _checkIfStopped(self, now: float, colours: List[Color]):
        """Marks stopping as finished if all bulbs are now off"""
        if self._timeToNextStoppedCheck is not None and now >= self._timeToNextStoppedCheck:
            if allOff(colours):
                self._stopping = False

