from random import randrange
from typing import Callable, Tuple

from colour import Color

from fireflies.FireflyColour import FireflyColour
from utils.colours import off


def randomColour() -> FireflyColour:
    return FireflyColour.BRIGHT if randrange(0, 2) == 0 else FireflyColour.DARK


def randomDelay() -> int:
    return randrange(0, 25)


class Firefly:
    def __init__(
        self,
        position: int,
        activeAlgorithm: Callable[[int, FireflyColour, int], Callable[[], Tuple[Color, bool]]],
        ticksActive: int = 10,
        steps: int = 10,
    ):
        self.position: int = position
        colour: FireflyColour = randomColour()
        self.activeAlgorithm: Callable[[], Tuple[Color, bool]] = activeAlgorithm(
            ticksActive, colour, steps
        )

        self.delay: int = randomDelay()
        self.delayCounter: int = 0
        self.isDone: bool = False

    def tick(self) -> Color:
        if self.isWaitingToStart():
            self.delayCounter += 1
            return off
        elif self.isDone:
            return off
        else:
            (colour, isDone) = self.activeAlgorithm()
            self.isDone = isDone
            return colour

    def isWaitingToStart(self) -> bool:
        return self.delayCounter < self.delay
