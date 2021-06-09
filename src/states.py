import multiprocessing
from time import sleep
from typing import Union

from transitions import Machine, State

from fireflies import run as runFireflies
from flickering_fairylights import run as runFlickeringFairylights
from leds.Leds import Leds
from random_twinkling import run as runRandomTwinkling
from random_twinkling import (
    runColoursWheel,
    runRandomAnalagousColours,
    runRandomAnalagousWeightedColours,
    runRandomColours,
)
from temperature_check.mockCheckTemperature import (
    mockCheckTemperature as checkTemperature,
)


class Button:
    def __init__(self, callback):
        self.callback = callback

    def press(self):
        self.callback()


states = [
    State(name="Init"),
    State(name="FlickeringFairyLights"),
    State(name="RandomTwinklingBluePink"),
    State(name="RandomTwinklingRetro"),
    State(name="RandomTwinklingRandomColours"),
    State(name="RandomTwinklingRandomAnalagousColours"),
    State(name="RandomTwinklingRandomAnalagousWeightedColours"),
    State(name="RandomTwinklingColourWheel"),
    State(name="Fireflies"),
]

transitions = [
    {"trigger": "initialise", "source": states[0], "dest": states[1]},
    {"trigger": "next", "source": states[1], "dest": states[2]},
    {"trigger": "next", "source": states[2], "dest": states[3]},
    {"trigger": "next", "source": states[3], "dest": states[4]},
    {"trigger": "next", "source": states[4], "dest": states[5]},
    {"trigger": "next", "source": states[5], "dest": states[6]},
    {"trigger": "next", "source": states[6], "dest": states[7]},
    {"trigger": "next", "source": states[7], "dest": states[8]},
    {"trigger": "next", "source": states[8], "dest": states[1]},
]


class FairyLights(Machine):
    def __init__(self, leds):
        print("Starting...")
        self.leds = leds
        self.machine = Machine(
            self,
            states=states,
            transitions=transitions,
            initial=states[0],
        )
        self.process: Union[multiprocessing.Process, None] = None
        self.processMonitorTemperature: multiprocessing.Process = (
            multiprocessing.Process(target=self.monitorTemperature)
        )
        self.processMonitorTemperature.start()
        self.trigger("initialise")

    def monitorTemperature(self):
        while True:
            print("Checking temp", checkTemperature())
            sleep(10)

    def next(self):
        print("Button pressed")
        if self.process is not None and self.process.is_alive() is True:
            self.process.terminate()
            self.process = None
        self.trigger("next")

    def on_enter_FlickeringFairyLights(self):
        print("Flicker")
        self.process = multiprocessing.Process(
            target=runFlickeringFairylights, args=(self.leds,)
        )
        self.process.start()

    def on_enter_RandomTwinklingBluePink(self):
        print("TwinkleBluePink")
        self.process = multiprocessing.Process(
            target=runRandomTwinkling, args=(self.leds, "BLUE_PINK")
        )
        self.process.start()

    def on_enter_RandomTwinklingRetro(self):
        print("TwinkleRetro")
        self.process = multiprocessing.Process(
            target=runRandomTwinkling, args=(self.leds, "RETRO")
        )
        self.process.start()

    def on_enter_Fireflies(self):
        print("Fireflies")
        self.process = multiprocessing.Process(target=runFireflies, args=(self.leds,))
        self.process.start()

    def on_enter_RandomTwinklingRandomColours(self):
        print("RandomTwinklingRandomColours")
        self.process = multiprocessing.Process(
            target=runRandomColours, args=(self.leds,)
        )
        self.process.start()

    def on_enter_RandomTwinklingRandomAnalagousColours(self):
        print("RandomTwinklingRandomAnalagousColours")
        self.process = multiprocessing.Process(
            target=runRandomAnalagousColours, args=(self.leds,)
        )
        self.process.start()

    def on_enter_RandomTwinklingRandomAnalagousWeightedColours(self):
        print("RandomTwinklingRandomAnalagousWeightedColours")
        self.process = multiprocessing.Process(
            target=runRandomAnalagousWeightedColours, args=(self.leds,)
        )
        self.process.start()

    def on_enter_RandomTwinklingColourWheel(self):
        print("RandomTwinklingColourWheel")
        self.process = multiprocessing.Process(
            target=runColoursWheel, args=(self.leds,)
        )
        self.process.start()


def main():
    leds = Leds()

    fl = FairyLights(leds)

    button = Button(callback=fl.next)

    # sleep(10)
    button.press()
    # sleep(10)
    button.press()
    # sleep(10)
    button.press()
    # sleep(10)
    button.press()
    button.press()
    # button.press()


main()
