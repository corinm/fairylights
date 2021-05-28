import random
from enum import Enum

maxTempIncrement = 5
minTempIncrement = 1
maxTempDecrement = 3
minTempDecrement = 1
offTemp = 100
onTemp = 95


class BulbState(Enum):
    OFF = 1
    DIM = 2
    ON = 3


def randomIncrease() -> int:
    return random.randrange(minTempIncrement, maxTempIncrement + 1)


def randomDecrease() -> int:
    return random.randrange(minTempDecrement, maxTempDecrement + 1)


class FlickerBulb:
    def __init__(self, seed: int = None):
        self.state = BulbState.DIM
        self.temp = 0
        random.seed(seed)

    def tick(self):
        if self.state == BulbState.DIM:
            if self.temp < onTemp:
                self.finishTurningOn()
            else:
                self.finishTurningOff()

        elif self.state == BulbState.ON:
            self.temp = self.temp + randomIncrease()

            if self.temp >= offTemp:
                self.turnOff()

        elif self.state == BulbState.OFF:
            self.temp = self.temp - randomDecrease()

            if self.temp <= onTemp:
                self.turnOn()

    def turnOff(self):
        self.state = BulbState.DIM

    def turnOn(self):
        self.state = BulbState.DIM

    def finishTurningOff(self):
        self.state = BulbState.OFF

    def finishTurningOn(self):
        self.state = BulbState.ON
