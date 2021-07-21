from enum import Enum
from typing import List, Union

from transitions import Machine, State

from fireflies import runFlicker, runStaticGlow, runStaticGlowShorter  # noqa
from flickering_fairylights import run as runFlickeringFairylights  # noqa
from random_twinkling import (  # noqa
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
from utils.StoppableThread import StoppableThread

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


def runOff(leds, shouldStop):
    print("runOff")
    leds.clear()


class StateWithRunMethod(State):
    def __init__(
        self,
        name: Pattern,
        run=lambda *args: None,
    ):
        super().__init__(name, on_enter=None, on_exit=None, ignore_invalid_triggers=None)
        self.run = run

    def serialise(self):
        return self.name


states: List[StateWithRunMethod] = [
    # StateWithRunMethod(Pattern.Flickering, runFlickeringFairylights),
    StateWithRunMethod(Pattern.Twinkling_Retro, runTwinklingRetro),
    StateWithRunMethod(Pattern.Twinkling_Random, runRandomColours),
    StateWithRunMethod(Pattern.Twinkling_Analagous, runRandomAnalagousColours),
    StateWithRunMethod(Pattern.Twinkling_AnalagousWeighted, runRandomAnalagousWeightedColours),
    StateWithRunMethod(Pattern.Twinkling_Complementary, runRandomComplementary),
    StateWithRunMethod(Pattern.Twinkling_SplitComplementary, runRandomSplitComplementary),
    StateWithRunMethod(Pattern.Twinkling_137Degrees, runRandomColour137Degress),
    StateWithRunMethod(Pattern.Twinkling_ColourWheel, runColoursWheel),
    StateWithRunMethod(Pattern.Twinkling_ColourWheelFast, runColoursWheelFast),
    StateWithRunMethod(Pattern.Twinkling_CoolorPalletes, runCoolorPalettes),
    StateWithRunMethod(Pattern.Fireflies_StaticGlowShorter, runStaticGlowShorter),
    StateWithRunMethod(Pattern.Fireflies_StaticGlow, runStaticGlow),
    StateWithRunMethod(Pattern.Fireflies_StaticFlicker, runFlicker),
    StateWithRunMethod(Pattern.Off, runOff),
]

statesSerialised = [(i, states[i].serialise()) for i in range(len(states))]


class FairyLightPatterns(Machine):
    def __init__(self, leds):
        print("Starting FairyLightPatterns...")
        self.leds = leds
        self.machine = Machine(
            self,
            states=states,
            # initial=states[len(states) - 1],
            # initial=states[randrange(0, len(states))],
            initial=states[9],
        )
        self.machine.add_transition(trigger="stop", source=[s.name for s in states], dest="Off")
        self.machine.add_ordered_transitions(after=self.on_enter)
        self.thread: Union[StoppableThread, None] = None

    def _stopThread(self):
        print("CHECKING THREAD")
        print(self.thread)
        if self.thread is not None:
            print("ASKING THREAD TO STOP")
            self.thread.stop()
            print("CALLING JOIN")
            self.thread.join()
            print("JOINED")
            self.thread = None

    def _runState(self, state: Pattern):
        self._stopThread()
        print("STARTING NEW THREAD")
        runMethod = self.machine.states[state.name].run

        if not callable(runMethod):
            print("run method not callable")
            return

        self.thread = StoppableThread(target=runMethod, args=(self.leds,))
        self.thread.setDaemon(True)
        print(">> Starting thread")
        self.thread.start()
        print(">> Thread started")

    def next(self):
        self.trigger("next_state")

    def on_enter(self):
        print("Transitioned to: ", self.state)
        self._runState(self.state)

    def toPattern(self, stateName: Pattern):
        self._runState(stateName)
