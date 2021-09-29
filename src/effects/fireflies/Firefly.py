from random import randrange

from colour import Color

from utils.colours import off

from .FireflyColour import FireflyColour, colours


def randomTimeActive() -> float:
    return randrange(200, 2000) / 1000


def randomDelay() -> float:
    return randrange(0, 2000) / 1000


def randomColour() -> FireflyColour:
    return FireflyColour.BRIGHT if randrange(0, 2) == 0 else FireflyColour.DARK


class Firefly:
    def __init__(self, position: int):
        self._position = position
        self._timeActive = randomTimeActive()
        self._delayBeforeActive = randomDelay()
        self._time: float = 0
        self._isDone = False
        self._colourType: FireflyColour = randomColour()

    def incrementTimeDelta(self, timeDelta: float) -> None:
        self._time += timeDelta

        if self._time > self._delayBeforeActive + self._timeActive:
            self._isDone = True

    def getColour(self) -> Color:
        if self._time < self._delayBeforeActive:
            return off

        elif self._time > self._delayBeforeActive + self._timeActive:
            return off

        else:
            x = self._time - self._delayBeforeActive
            if x < 0.2:
                # increasing
                y = 5 * x
                c = Color(colours[self._colourType])
                c.set_luminance(y * 0.15)
                return c
            elif x > self._timeActive - 0.2:
                # decreasing
                x2 = self._timeActive - x
                y = 5 * x2
                c = Color(colours[self._colourType])
                c.set_luminance(y * 0.15)
                return c
            else:
                # on
                return colours[self._colourType]

    def getPosition(self) -> int:
        return self._position

    def _isDelayed(self, now: float) -> bool:
        return now < self._delayBeforeActive

    def isDone(self) -> bool:
        return self._isDone
