import multiprocessing
from time import sleep
from typing import Union

from transitions import Machine, State

from display.MockDisplay import MockDisplay
from fireflies import run as runFireflies
from flickering_fairylights import run as runFlickeringFairylights
from leds.Leds import Leds
from random_twinkling import run as runRandomTwinkling
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
    State(name="Fireflies"),
]

transitions = [
    {"trigger": "initialise", "source": states[0], "dest": states[1]},
    {"trigger": "buttonPressed", "source": states[1], "dest": states[2]},
    {"trigger": "buttonPressed", "source": states[2], "dest": states[3]},
    {"trigger": "buttonPressed", "source": states[3], "dest": states[4]},
    {"trigger": "buttonPressed", "source": states[4], "dest": states[1]},
]


class FairyLights(Machine):
    def __init__(self, leds, display):
        print("Starting...")
        self.leds = leds
        self.display = display
        self.machine = Machine(
            self,
            states=states,
            transitions=transitions,
            initial=states[0],
            after_state_change="showState",
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

    def showState(self):
        self.display.renderMessage(f"> {self.state}")

    def buttonPressed(self):
        print("Button pressed")
        if self.process is not None and self.process.is_alive() is True:
            self.process.terminate()
            self.process = None
        self.trigger("buttonPressed")

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


def main():
    display = MockDisplay()
    leds = Leds()

    fl = FairyLights(leds, display)

    button = Button(callback=fl.buttonPressed)

    sleep(0)
    button.press()
    sleep(0)
    button.press()
    sleep(0)
    button.press()
    # sleep(5)
    # button.press()


main()
