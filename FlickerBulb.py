from random import randrange

maxTempIncrement = 5
minTempIncrement = 1
maxTempDecrement = 3
minTempDecrement = 1
offTemp = 70
onTemp = 50


def randomIncrease() -> int:
    return randrange(minTempIncrement, maxTempIncrement + 1)


def randomDecrease() -> int:
    return randrange(minTempDecrement, maxTempDecrement + 1)


class FlickerBulb:
    def __init__(self):
        self.isOn = True
        self.temp = 0

    def tick(self):
        if self.isOn == True:
            self.temp = self.temp + randomIncrease()

            if self.temp >= offTemp:
                self.isOn = False

        else:
            self.temp = self.temp - randomDecrease()

            if self.temp <= onTemp:
                self.isOn = True
