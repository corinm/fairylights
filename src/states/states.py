import multiprocessing
from random import randrange
from typing import List, Union

from transitions import Machine, State

from fireflies import runFlicker, runStaticGlow, runStaticGlowShorter
from flickering_fairylights import run as runFlickeringFairylights
from random_twinkling import (
    runColoursWheel,
    runColoursWheelFast,
    runRandomAnalagousColours,
    runRandomAnalagousWeightedColours,
    runRandomColour137Degress,
    runRandomColours,
    runRandomComplimentary,
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
    StateWithRunMethod(name="Flickering", run=runFlickeringFairylights),
    StateWithRunMethod(name="Twinkling_Retro", run=runTwinklingRetro),
    StateWithRunMethod(name="Twinkling_Random", run=runRandomColours),
    StateWithRunMethod(name="Twinkling_Analagous", run=runRandomAnalagousColours),
    StateWithRunMethod(name="Twinkling_AnalagousWeighted", run=runRandomAnalagousWeightedColours),
    StateWithRunMethod(name="Twinkling_Complimentary", run=runRandomComplimentary),
    StateWithRunMethod(name="Twinkling_137Degrees", run=runRandomColour137Degress),
    StateWithRunMethod(name="Twinkling_ColourWheel", run=runColoursWheel),
    StateWithRunMethod(name="Twinkling_ColourWheelFast", run=runColoursWheelFast),
    StateWithRunMethod(name="Fireflies_StaticGlowShorter", run=runStaticGlowShorter),
    StateWithRunMethod(name="Fireflies_StaticGlow", run=runStaticGlow),
    StateWithRunMethod(name="Fireflies_StaticFlicker", run=runFlicker),
]


class FairyLights(Machine):
    def __init__(self, leds):
        print("Starting...")
        self.leds = leds
        self.machine = Machine(
            self,
            states=states,
            # initial=states[len(states) - 1],
            initial=states[randrange(0, len(states))],
        )
        self.machine.add_ordered_transitions(after=self.on_enter)
        self.process: Union[multiprocessing.Process, None] = None
        self.next()

    def next(self):
        if self.process is not None and self.process.is_alive() is True:
            self.process.terminate()
            self.process = None
        self.trigger("next_state")

    def on_enter(self):
        print("Transitioned to: ", self.state)

        runMethod = self.machine.states[self.state].run

        if not callable(runMethod):
            print("run method not callable")
            return

        self.process = multiprocessing.Process(target=runMethod, args=(self.leds,))
        self.process.start()
