from random import randrange
from typing import Callable, List, Tuple

from colour import Color

from fireflies.FireflyColour import FireflyColour
from fireflies.patterns import flicker, staticGlow
from utils.colours import off


def randomColour() -> FireflyColour:
    return FireflyColour.BRIGHT if randrange(0, 2) == 0 else FireflyColour.DARK


def randomDelay() -> int:
    return randrange(0, 25)


def randomTicksActive() -> int:
    return randrange(2, 30)


class Firefly:
    def __init__(
        self,
        position: int,
        activeAlgorithm: Callable[
            [int, FireflyColour], Callable[[], Tuple[Color, bool]]
        ],
    ):
        self.position: int = position
        ticksActive = randomTicksActive()
        colour: FireflyColour = randomColour()
        self.activeAlgorithm: Callable[[], Tuple[Color, bool]] = activeAlgorithm(
            ticksActive, colour
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


class Fireflies:
    def __init__(self, numberOfLeds: int):
        self.numberOfLeds = numberOfLeds
        self.fireflies: List[Firefly] = []
        self.ticksUntilNextWave = 0

    def tick(self):
        colours = [off for i in range(50)]

        if self.noFirefliesAndReadyForNextWave():
            self.newFirelies()

        for firefly in self.fireflies:
            colour = firefly.tick()
            colours[firefly.position] = colour

        self.fireflies = [f for f in self.fireflies if not f.isDone]

        if self.noActiveFireflies():
            if self.ticksUntilNextWave == 0:
                self.startNewCountdown()
            else:
                self.ticksUntilNextWave -= 1

        return colours

    def startNewCountdown(self):
        self.ticksUntilNextWave = randrange(5, 150)

    def noFirefliesAndReadyForNextWave(self) -> bool:
        return len(self.fireflies) == 0 and self.ticksUntilNextWave == 0

    def noActiveFireflies(self) -> bool:
        return len([f for f in self.fireflies if not f.isDone]) == 0

    def newFirelies(self):
        upper = randrange(2, 8 + 1)
        algo = flicker if randrange(0, 3) == 0 else staticGlow
        for i in range(self.numberOfLeds):
            if randrange(0, upper) == 0:
                self.fireflies.append(Firefly(i, algo))


# Types
#   Briefly flickers
#   Glows for period of time then goes off
