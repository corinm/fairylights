import multiprocessing
from time import sleep
from typing import List, Union

from transitions import Machine, State

from fireflies import run as runFireflies
from flickering_fairylights import run as runFlickeringFairylights
from leds.Leds import Leds
from random_twinkling import (
    runColoursWheel,
    runRandomAnalagousColours,
    runRandomAnalagousWeightedColours,
    runRandomColours,
    runTwinklingRetro,
)


class StateWithRunMethod(State):
    def __init__(
        self,
        name,
        on_enter=None,
        on_exit=None,
        ignore_invalid_triggers=None,
        run=lambda *args: None,
    ):
        super().__init__(name, on_enter, on_exit, ignore_invalid_triggers)
        self.run = run


states: List[State] = [
    StateWithRunMethod(name="FlickeringFairyLights", run=runFlickeringFairylights),
    StateWithRunMethod(name="RandomTwinklingRetro", run=runTwinklingRetro),
    StateWithRunMethod(name="RandomTwinklingRandomColours", run=runRandomColours),
    StateWithRunMethod(
        name="RandomTwinklingRandomAnalagousColours",
        run=runRandomAnalagousColours,
    ),
    StateWithRunMethod(
        name="RandomTwinklingRandomAnalagousWeightedColours",
        run=runRandomAnalagousWeightedColours,
    ),
    StateWithRunMethod(name="RandomTwinklingColourWheel", run=runColoursWheel),
    StateWithRunMethod(name="Fireflies", run=runFireflies),
]


class FairyLights(Machine):
    def __init__(self, leds):
        print("Starting...")
        self.leds = leds
        self.machine = Machine(
            self,
            states=states,
            initial=states[0],
        )
        self.machine.add_ordered_transitions(after=self.on_enter)
        self.process: Union[multiprocessing.Process, None] = None

    def next(self):
        print("About to transition")
        if self.process is not None and self.process.is_alive() is True:
            self.process.terminate()
            self.process = None
        self.trigger("next_state")

    def on_enter(self):
        print("On enter", self.state)

        runMethod = self.machine.states[self.state].run

        if not callable(runMethod):
            print("run method not callable")
            return

        self.process = multiprocessing.Process(target=runMethod, args=(self.leds,))
        self.process.start()


def main():
    leds = Leds()
    fl = FairyLights(leds)

    while True:
        fl.next()
        sleep(5)


main()
