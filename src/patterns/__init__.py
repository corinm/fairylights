from enum import Enum
from typing import Callable, List, Type, Union

from transitions import Machine, State

from leds.Leds import Leds
from patterns.fireflies.FirefliesConstant import FirefliesConstant
from patterns.twinkle.Twinkle import Twinkle
from patterns.twinkle.TwinkleFromColourAlgorithm import TwinkleFromColourAlgorithm
from patterns.twinkle.TwinkleFromPalettes import TwinkleFromPalettes
from utils.colours import coolors, pleasantWhite, retroColoursList
from utils.randomColour import colourWheel, randomAnalogousWeighted
from utils.randomColour import randomColour as trulyRandom
from utils.randomColour import (
    randomColour137Degrees,
    randomColourAnalogous,
    randomComplementary,
    randomSplitComplementary,
)
from utils.StoppableThread import StoppableThread

# from colour import Color
# from patterns.fireflies import runGlowConstant
# from patterns.full_twinkle import runFullTwinkleRetro
# from patterns.glitter import runGlitterWarm
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
    FullTwinkle_Retro = 12
    FullTwinkle_ColourWheelFast = 13
    Fireflies_GlowConstant = 14
    Glitter_Warm = 15
    Glitter_Retro = 16
    Glitter_Random = 17
    Glitter_Analagous = 18
    Glitter_AnalagousWeighted = 19
    Glitter_Complementary = 20
    Glitter_SplitComplementary = 21
    Glitter_137Degrees = 22
    Glitter_ColourWheel = 23
    Glitter_ColourWheelFast = 24
    Glitter_CoolorPalletes = 25
    Off = 99


def runOff(leds, shouldStop):
    print("runOff")
    leds.clear()


class StateWithRunMethod(State):
    def __init__(
        self,
        name: Pattern,
        patternManager: Union[
            Type[Twinkle],
            Type[TwinkleFromColourAlgorithm],
            Type[TwinkleFromPalettes],
            Type[FirefliesConstant],
        ],
        args={},
    ):
        super().__init__(name, on_enter=None, on_exit=None, ignore_invalid_triggers=None)
        self._patternManager = patternManager
        self._args = args

    def run(self, leds: Leds, shouldStop: Callable[[], bool]):
        pattern = self._patternManager(50, **self._args)

        while not shouldStop():
            leds.setLeds(pattern.tick())

        pattern.stop()

        while pattern.isStopping():
            leds.setLeds(pattern.tick())

    def serialise(self):
        return self.name


class StateOff(State):
    def __init__(self, name: Pattern):
        super().__init__(name, on_enter=None, on_exit=None, ignore_invalid_triggers=None)

    def run(self, leds: Leds, shouldStop: Callable[[], bool]):
        while not shouldStop():
            pass

    def serialise(self):
        return self.name


states: List[Union[StateWithRunMethod, StateOff]] = [
    # Twinkle
    StateWithRunMethod(Pattern.Twinkle_Retro, Twinkle, dict(colours=retroColoursList)),
    StateWithRunMethod(
        Pattern.Twinkle_Random, TwinkleFromColourAlgorithm, dict(colourGenerator=trulyRandom)
    ),
    StateWithRunMethod(
        Pattern.Twinkle_Analagous,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=randomColourAnalogous,
            secondsBetweenPaletteChanges=0,
            secondsBetweenColourChanges=5,
            numberOfColours=3,
        ),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_AnalagousWeighted,
        TwinkleFromColourAlgorithm,
        dict(colourGenerator=randomAnalogousWeighted, numberOfColours=3),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_Complementary,
        TwinkleFromColourAlgorithm,
        dict(colourGenerator=randomComplementary, numberOfColours=6),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_SplitComplementary,
        TwinkleFromColourAlgorithm,
        dict(colourGenerator=randomSplitComplementary, numberOfColours=5),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_137Degrees,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=randomColour137Degrees, secondsBetweenColourChanges=5, numberOfColours=6
        ),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_ColourWheel,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=colourWheel,
            secondsBetweenPaletteChanges=0,
            secondsBetweenColourChanges=4,
        ),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_ColourWheelFast,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=colourWheel,
            secondsBetweenPaletteChanges=0,
            secondsBetweenColourChanges=1,
        ),
    ),
    StateWithRunMethod(Pattern.Twinkle_CoolorPalletes, TwinkleFromPalettes, dict(palettes=coolors)),
    # Full twinkle
    StateWithRunMethod(
        Pattern.FullTwinkle_Retro, Twinkle, dict(colours=retroColoursList, timeBetweenTwinkles=0.01)
    ),
    StateWithRunMethod(
        Pattern.FullTwinkle_ColourWheelFast,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=colourWheel,
            secondsBetweenPaletteChanges=0,
            secondsBetweenColourChanges=1,
            timeBetweenTwinkles=0.01,
        ),
    ),
    # Fireflies
    StateWithRunMethod(Pattern.Fireflies_GlowConstant, FirefliesConstant, dict()),
    # Glitter
    StateWithRunMethod(
        Pattern.Glitter_Warm,
        Twinkle,
        dict(colours=[pleasantWhite], timeBetweenTwinkles=0.05, timeToPeak=0.3, maxLuminance=0.02),
    ),
    StateWithRunMethod(
        Pattern.Glitter_Retro,
        Twinkle,
        dict(colours=retroColoursList, timeBetweenTwinkles=0.05, timeToPeak=0.3, maxLuminance=0.02),
    ),
    StateWithRunMethod(
        Pattern.Glitter_Random,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=trulyRandom, timeBetweenTwinkles=0.05, timeToPeak=0.3, maxLuminance=0.02
        ),
    ),
    StateWithRunMethod(
        Pattern.Glitter_Analagous,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=randomColourAnalogous,
            secondsBetweenPaletteChanges=0,
            secondsBetweenColourChanges=5,
            numberOfColours=3,
            timeBetweenTwinkles=0.05,
            timeToPeak=0.3,
            maxLuminance=0.02,
        ),
    ),
    StateWithRunMethod(
        Pattern.Glitter_AnalagousWeighted,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=randomAnalogousWeighted,
            numberOfColours=3,
            timeBetweenTwinkles=0.05,
            timeToPeak=0.3,
            maxLuminance=0.02,
        ),
    ),
    StateWithRunMethod(
        Pattern.Glitter_Complementary,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=randomComplementary,
            numberOfColours=6,
            timeBetweenTwinkles=0.05,
            timeToPeak=0.3,
            maxLuminance=0.02,
        ),
    ),
    StateWithRunMethod(
        Pattern.Glitter_SplitComplementary,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=randomSplitComplementary,
            numberOfColours=5,
            timeBetweenTwinkles=0.05,
            timeToPeak=0.3,
            maxLuminance=0.02,
        ),
    ),
    StateWithRunMethod(
        Pattern.Glitter_137Degrees,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=randomColour137Degrees,
            secondsBetweenColourChanges=5,
            numberOfColours=6,
            timeBetweenTwinkles=0.05,
            timeToPeak=0.3,
            maxLuminance=0.02,
        ),
    ),
    StateWithRunMethod(
        Pattern.Glitter_ColourWheel,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=colourWheel,
            secondsBetweenPaletteChanges=0,
            secondsBetweenColourChanges=4,
            timeBetweenTwinkles=0.05,
            timeToPeak=0.3,
            maxLuminance=0.02,
        ),
    ),
    StateWithRunMethod(
        Pattern.Glitter_ColourWheelFast,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=colourWheel,
            secondsBetweenPaletteChanges=0,
            secondsBetweenColourChanges=1,
            timeBetweenTwinkles=0.05,
            timeToPeak=0.3,
            maxLuminance=0.02,
        ),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_CoolorPalletes,
        TwinkleFromPalettes,
        dict(
            palettes=coolors,
            timeBetweenTwinkles=0.05,
            timeToPeak=0.3,
            maxLuminance=0.02,
        ),
    ),
    # Off
    StateOff(Pattern.Off),
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
