import random
from enum import Enum

from constants import MIN_TEMP_INCREMENT, MAX_TEMP_INCREMENT, MIN_TEMP_DECREMENT, MAX_TEMP_DECREMENT, OFF_TEMP, ON_TEMP


class BulbState(Enum):
    OFF = 1
    DIM = 2
    ON = 3


def randomIncrease() -> int:
    return random.randrange(MIN_TEMP_INCREMENT, MAX_TEMP_INCREMENT + 1)


def randomDecrease() -> int:
    return random.randrange(MIN_TEMP_DECREMENT, MAX_TEMP_DECREMENT + 1)


class FlickerBulb:
    def __init__(self, seed: int = None):
        self.state = BulbState.DIM
        self.temp = 0
        random.seed(seed)

    def tick(self):
        if self.state == BulbState.DIM:
            if self.temp < ON_TEMP:
                self.finishTurningOn()
            else:
                self.finishTurningOff()

        elif self.state == BulbState.ON:
            self.temp = self.temp + randomIncrease()

            if self.temp >= OFF_TEMP:
                self.turnOff()

        elif self.state == BulbState.OFF:
            self.temp = self.temp - randomDecrease()

            if self.temp <= ON_TEMP:
                self.turnOn()

    def turnOff(self):
        self.state = BulbState.DIM

    def turnOn(self):
        self.state = BulbState.DIM

    def finishTurningOff(self):
        self.state = BulbState.OFF

    def finishTurningOn(self):
        self.state = BulbState.ON
