import multiprocessing
from enum import Enum
from typing import List, Union

from transitions import Machine, State

from fireflies import runFlicker, runStaticGlow, runStaticGlowShorter
from flickering_fairylights import run as runFlickeringFairylights
from random_twinkling import (
    runColoursWheel,
    runColoursWheelFast,
    runCoolorPalettes,
    runRandomAnalagousColours,
    runRandomAnalagousWeightedColours,
    runRandomColour137Degress,
    runRandomColours,
    runRandomComplementary,
    runRandomSplitComplementary,
    runTwinklingRetro,
)

# from random import randrange


class Pattern(Enum):
    Flickering = 1
    Twinkling_Retro = 2
    Twinkling_Random = 3
    Twinkling_Analagous = 4
    Twinkling_AnalagousWeighted = 5
    Twinkling_Complementary = 6
    Twinkling_SplitComplementary = 7
    Twinkling_137Degrees = 8
    Twinkling_ColourWheel = 9
    Twinkling_ColourWheelFast = 10
    Twinkling_CoolorPalletes = 11
    Fireflies_StaticGlowShorter = 12
    Fireflies_StaticGlow = 13
    Fireflies_StaticFlicker = 14
    Off = 99


def runOff(leds):
    print("runOff")
    leds.clear()


class StateWithRunMethod(State):
    def __init__(
        self,
        name: Pattern,
        on_enter=None,
        on_exit=None,
        ignore_invalid_triggers=None,
        run=lambda *args: None,
    ):
        super().__init__(name, on_enter, on_exit, ignore_invalid_triggers)
        self.run = run

    def serialise(self):
        return self.name


states: List[StateWithRunMethod] = [
    StateWithRunMethod(name=Pattern.Flickering, run=runFlickeringFairylights),
    StateWithRunMethod(name=Pattern.Twinkling_Retro, run=runTwinklingRetro),
    StateWithRunMethod(name=Pattern.Twinkling_Random, run=runRandomColours),
    StateWithRunMethod(name=Pattern.Twinkling_Analagous, run=runRandomAnalagousColours),
    StateWithRunMethod(
        name=Pattern.Twinkling_AnalagousWeighted, run=runRandomAnalagousWeightedColours
    ),
    StateWithRunMethod(name=Pattern.Twinkling_Complementary, run=runRandomComplementary),
    StateWithRunMethod(name=Pattern.Twinkling_SplitComplementary, run=runRandomSplitComplementary),
    StateWithRunMethod(name=Pattern.Twinkling_137Degrees, run=runRandomColour137Degress),
    StateWithRunMethod(name=Pattern.Twinkling_ColourWheel, run=runColoursWheel),
    StateWithRunMethod(name=Pattern.Twinkling_ColourWheelFast, run=runColoursWheelFast),
    StateWithRunMethod(name=Pattern.Twinkling_CoolorPalletes, run=runCoolorPalettes),
    StateWithRunMethod(name=Pattern.Fireflies_StaticGlowShorter, run=runStaticGlowShorter),
    StateWithRunMethod(name=Pattern.Fireflies_StaticGlow, run=runStaticGlow),
    StateWithRunMethod(name=Pattern.Fireflies_StaticFlicker, run=runFlicker),
    StateWithRunMethod(name=Pattern.Off, run=runOff),
]

statesSerialised = [(i, states[i].serialise()) for i in range(len(states))]


class FairyLightPatterns(Machine):
    def __init__(self, leds):
        print("Starting...")
        self.leds = leds
        self.machine = Machine(
            self,
            states=states,
            # initial=states[len(states) - 1],
            # initial=states[randrange(0, len(states))],
            initial=states[9],
        )
        print(self.machine.states)
        self.machine.add_transition(trigger="stop", source=[s.name for s in states], dest="Off")
        self.machine.add_ordered_transitions(after=self.on_enter)
        self.process: Union[multiprocessing.Process, None] = None

    def _clearProcessIfExists(self):
        if self.process is not None:
            print("TERMINATING PROCESS")
            self.process.terminate()
            self.process = None

    def _runState(self, state: Pattern):
        self._clearProcessIfExists()
        print(state.name)
        runMethod = self.machine.states[state.name].run

        if not callable(runMethod):
            print("run method not callable")
            return

        self.process = multiprocessing.Process(
            target=runMethod,
            args=(self.leds,),
        )
        self.process.daemon = True
        self.process.start()

    def next(self):
        self._clearProcessIfExists()
        self.trigger("next_state")

    def on_enter(self):
        print("Transitioned to: ", self.state)
        self._clearProcessIfExists()
        self._runState(self.state)

    def toPattern(self, stateName: Pattern):
        self._clearProcessIfExists()
        self._runState(stateName)

    def stop(self):
        print("patterns.stop")
        self.trigger("stop")
        self.leds.clear()
        print(self.state)
