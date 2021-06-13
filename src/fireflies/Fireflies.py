import math
from random import random, randrange
from typing import Callable, List, Tuple

from colour import Color

from fireflies.FireflyColour import FireflyColour
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
    def __init__(self, numberOfLeds: int, algo):
        self.numberOfLeds = numberOfLeds
        self.fireflies: List[Firefly] = []
        self.ticksUntilNextWave = 0
        self.ticksSinceLastWave = 0
        self.algo = algo

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
        self.ticksSinceLastWave = self.ticksUntilNextWave

    def noFirefliesAndReadyForNextWave(self) -> bool:
        return len(self.fireflies) == 0 and self.ticksUntilNextWave == 0

    def noActiveFireflies(self) -> bool:
        return len([f for f in self.fireflies if not f.isDone]) == 0

    def newFirelies(self):
        # Half the time it's just a small number
        if random() <= 0.5:
            for i in range(self.numberOfLeds):
                if random() <= 0.1:
                    self.fireflies.append(Firefly(i, self.algo))
            return

        # Decide what % of fireflies will light up
        #   Longer time since last wave -> more fireflies
        timeModifier = math.floor(self.ticksSinceLastWave / 4)
        lower = 10 + timeModifier
        upper = 30 + timeModifier
        print(self.ticksSinceLastWave, lower, upper)
        percentage = randrange(lower, upper) / 100

        # Once % determined, use this to create fireflies
        for i in range(self.numberOfLeds):
            if random() <= percentage:
                self.fireflies.append(Firefly(i, self.algo))


# Types
#   Briefly flickers
#   Glows for period of time then goes off
