from enum import Enum
from typing import List, Union

from transitions import Machine, State

from fireflies import runFlicker, runStaticGlow, runStaticGlowShorter  # noqa
from flickering_fairylights import run as runFlickeringFairylights  # noqa
from twinkle import (  # noqa
    runColoursWheel,
    runColoursWheelFast,
    runCoolorPalettes,
    runRandomAnalagousColours,
    runRandomAnalagousWeightedColours,
    runRandomColour137Degress,
    runRandomColours,
    runRandomComplementary,
    runRandomSplitComplementary,
    runTwinkleRetro,
)
from utils.StoppableThread import StoppableThread

# from random import randrange


class Pattern(Enum):
    Flickering = 1
    Twinkle_Retro = 2
    Twinkle_Random = 3
    Twinkle_Analagous = 4
    Twinkle_AnalagousWeighted = 5
    Twinkle_Complementary = 6
    Twinkle_SplitComplementary = 7
    Twinkle_137Degrees = 8
    Twinkle_ColourWheel = 9
    Twinkle_ColourWheelFast = 10
    Twinkle_CoolorPalletes = 11
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
    StateWithRunMethod(Pattern.Twinkle_Retro, runTwinkleRetro),
    StateWithRunMethod(Pattern.Twinkle_Random, runRandomColours),
    StateWithRunMethod(Pattern.Twinkle_Analagous, runRandomAnalagousColours),
    StateWithRunMethod(Pattern.Twinkle_AnalagousWeighted, runRandomAnalagousWeightedColours),
    StateWithRunMethod(Pattern.Twinkle_Complementary, runRandomComplementary),
    StateWithRunMethod(Pattern.Twinkle_SplitComplementary, runRandomSplitComplementary),
    StateWithRunMethod(Pattern.Twinkle_137Degrees, runRandomColour137Degress),
    StateWithRunMethod(Pattern.Twinkle_ColourWheel, runColoursWheel),
    StateWithRunMethod(Pattern.Twinkle_ColourWheelFast, runColoursWheelFast),
    StateWithRunMethod(Pattern.Twinkle_CoolorPalletes, runCoolorPalettes),
    # StateWithRunMethod(Pattern.Fireflies_StaticGlowShorter, runStaticGlowShorter),
    # StateWithRunMethod(Pattern.Fireflies_StaticGlow, runStaticGlow),
    # StateWithRunMethod(Pattern.Fireflies_StaticFlicker, runFlicker),
    # StateWithRunMethod(Pattern.Flickering, runFlickeringFairylights),
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
            initial=states[len(states) - 1],
            # initial=states[randrange(0, len(states))],
            # initial=states[10],
        )
        self.machine.add_transition(trigger="stop", source=[s.name for s in states], dest="Off")
        self.machine.add_ordered_transitions(before=self.on_exit, after=self.on_enter)
        self.thread: Union[StoppableThread, None] = None

    def _stopThread(self):
        if self.thread is not None:
            print("🗑️  Asking thread to stop")
            self.thread.stop()
            self.thread.join()
            print("🗑️  Thread joined")
            self.thread = None

    def stop(self):
        self._stopThread()

    def _runState(self, state: Pattern):
        runMethod = self.machine.states[state.name].run

        if not callable(runMethod):
            raise ValueError("run method not callable")

        self.thread = StoppableThread(target=runMethod, args=(self.leds,))
        self.thread.setDaemon(True)
        print("🏁 Starting thread")
        self.thread.start()
        print("🏁 Thread started")

    def next(self):
        self.trigger("next_state")

    def on_enter(self):
        print("⏭️  Entering:", self.state)
        self._runState(self.state)

    def on_exit(self):
        print("⏭️  Leaving: ", self.state)
        self._stopThread()

    def toPattern(self, stateName: Pattern):
        self._runState(stateName)
