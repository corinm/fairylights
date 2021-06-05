from enum import Enum
from random import randrange
from typing import Dict, List

from colour import Color

from utils.gradients import createGradientFromBlack, createGradientToBlack

# yellowGreen1 = Color(rgb=(241 / 255, 250 / 255, 13 / 255))
bright = Color(rgb=(96 / 255, 100 / 255, 5 / 255))
dark = Color(rgb=(87 / 255, 96 / 255, 13 / 255))

STEPS = 10


class FireflyColour(Enum):
    BRIGHT = 1
    DARKER = 2


up1 = createGradientFromBlack(bright, STEPS)
down1 = createGradientToBlack(bright, STEPS)
gradient1: List[Color] = up1 + down1[1:]

up2 = createGradientFromBlack(bright, STEPS)
down2 = createGradientToBlack(bright, STEPS)
gradient2: List[Color] = up2 + down2[1:]

GRADIENT_LENGTH = STEPS * 2 - 1

black = Color(None)

gradients: Dict[FireflyColour, List[Color]] = {
    FireflyColour.BRIGHT: gradient1,
    FireflyColour.DARKER: gradient2,
}


class Firefly:
    def __init__(self, position: int):
        self.position: int = position
        self.state: int = 0
        self.colour: FireflyColour = (
            FireflyColour.BRIGHT if randrange(0, 2) == 0 else FireflyColour.DARKER
        )
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

        elif self.state >= GRADIENT_LENGTH - 1:
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
            colours[firefly.position] = gradients[firefly.colour][firefly.state]

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
