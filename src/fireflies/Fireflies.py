from random import randrange
from typing import List

from colour import Color

from utils.gradients import createGradientFromBlack, createGradientToBlack

# yellowGreen1 = Color(rgb=(241 / 255, 250 / 255, 13 / 255))
bright = Color(rgb=(96 / 255, 100 / 255, 5 / 255))
dark = Color(rgb=(40 / 255, 76 / 255, 2 / 255))

STEPS = 10

up = createGradientFromBlack(bright, STEPS)
down = createGradientToBlack(bright, STEPS)

gradient: List[Color] = up + down[1:]

black = Color(None)


class Firefly:
    def __init__(self, position: int):
        self.position: int = position
        self.state: int = 0
        self.done = False


class FireflyStaticGlow(Firefly):
    def __init__(self, position: int):
        super().__init__(position)
        self.numberOfTicksWhileBright = randrange(2, 30)
        self.waitingCount = 0
        self.delay = randrange(0, 25)
        self.delayCount = 0

    def tick(self):
        if self.delayCount < self.delay:
            self.delayCount += 1

        elif self.isBright() and self.isWaiting():
            self.waitingCount += 1

        elif self.state >= len(gradient) - 1:
            self.done = True

        else:
            self.state += 1

    def isBright(self) -> bool:
        return self.state == STEPS

    def isWaiting(self) -> bool:
        return self.waitingCount < self.numberOfTicksWhileBright


class Fireflies:
    def __init__(self, numberOfLeds: int):
        self.numberOfLeds = numberOfLeds
        self.fireflies: List[Firefly] = []
        self.ticksUntilNextWave = 0

    def tick(self):
        colours = [black for i in range(50)]

        if self.noFirefliesAndReadyForNextWave():
            self.newFirelies()

        for firefly in self.fireflies:
            firefly.tick()
            colours[firefly.position] = gradient[firefly.state]

        self.fireflies = [f for f in self.fireflies if not f.done]

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
        return len([f for f in self.fireflies if not f.done]) == 0

    def newFirelies(self):
        upper = randrange(2, 5)
        for i in range(self.numberOfLeds):
            if randrange(0, upper) == 0:
                self.fireflies.append(FireflyStaticGlow(i))


# Types
#   Briefly flickers
#   Glows for period of time then goes off
