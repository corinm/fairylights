import math
from random import random, randrange
from typing import Callable, List, Tuple

from fireflies.Firefly import Firefly
from utils.colours import off


class FirefliesWaves:
    def __init__(
        self,
        numberOfLeds: int,
        algo: Callable,
        ticksActiveRange: Tuple[int, int],
        ticksBetweenWavesRange: Tuple[int, int],
    ):
        self.numberOfLeds = numberOfLeds
        self.fireflies: List[Firefly] = []
        self.ticksUntilNextWave = 0
        self.ticksSinceLastWave = 0
        self.algo = algo
        self.ticksActiveRange = ticksActiveRange
        self.ticksBetweenWavesRange = ticksBetweenWavesRange

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
        lower, upper = self.ticksBetweenWavesRange
        self.ticksUntilNextWave = randrange(lower, upper + 1)
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
                lower, upper = self.ticksActiveRange
                ticksActive = randrange(lower, upper + 1)
                self.fireflies.append(Firefly(i, self.algo, ticksActive))
