from enum import Enum, auto
from typing import Callable, List, Type, Union

from transitions import Machine, State

from leds.Leds import Leds
from colours import Retro, TrulyRandom, AnalogousRandom, AnalogousWeightedRandom, ComplementaryRandom
from colours.Rainbow import Rainbow
from effects.fireflies.FirefliesConstant import FirefliesConstant
from effects.twinkle.Twinkle import Twinkle
from effects.twinkle.TwinkleFromColourAlgorithm import TwinkleFromColourAlgorithm
from effects.twinkle.TwinkleFromPalettes import TwinkleFromPalettes
from effects.cycle import Cycle
from utils.colours import coolors, pleasantWhite, neon
from utils.randomColour import colourWheel
from utils.randomColour import (
    randomColour137Degrees,
    randomSplitComplementary,
)
from  utils.rainbow import rainbow
from utils.StoppableThread import StoppableThread

# from colour import Color
# from effects.fireflies import runGlowConstant
# from effects.full_twinkle import runFullTwinkleRetro
# from effects.glitter import runGlitterWarm
# from random import randrange


class Pattern(Enum):
    Flickering = auto()
    Twinkle_Retro = auto()
    Twinkle_Random = auto()
    Twinkle_Analagous = auto()
    Twinkle_AnalagousWeighted = auto()
    Twinkle_Complementary = auto()
    Twinkle_SplitComplementary = auto()
    Twinkle_137Degrees = auto()
    Twinkle_ColourWheel = auto()
    Twinkle_ColourWheelFast = auto()
    Twinkle_CoolorPalletes = auto()
    Twinkle_Neon = auto()

    FullTwinkle_Retro = auto()
    FullTwinkle_ColourWheelFast = auto()

    Fireflies_GlowConstant = auto()

    Glitter_Warm = auto()
    Glitter_Retro = auto()
    Glitter_Random = auto()
    Glitter_Analagous = auto()
    Glitter_AnalagousWeighted = auto()
    Glitter_Complementary = auto()
    Glitter_SplitComplementary = auto()
    Glitter_137Degrees = auto()
    Glitter_ColourWheel = auto()
    Glitter_ColourWheelFast = auto()
    Glitter_CoolorPalletes = auto()

    Cycle_Retro = auto()
    Cycle_Rainbow = auto()

    Off = auto()


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
        pattern = self._patternManager(leds.getNumber(), **self._args)

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


GLITTER_CONFIG = dict(timeBetweenTwinkles=0.03, timeToPeak=0.3, maxLuminance=0.02)

states: List[Union[StateWithRunMethod, StateOff]] = [
    # Twinkle
    StateWithRunMethod(Pattern.Twinkle_Retro, Twinkle, dict(colours=Retro)),
    StateWithRunMethod(
        Pattern.Twinkle_Random, Twinkle, dict(colours=TrulyRandom)
    ),
    StateWithRunMethod(
        Pattern.Twinkle_Analagous,
        Twinkle,
        dict(
            colours=AnalogousRandom,
            secondsBetweenColourChanges=5,
        ),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_AnalagousWeighted,
        Twinkle,
        dict(colours=AnalogousWeightedRandom),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_Complementary,
        Twinkle,
        dict(colours=ComplementaryRandom),
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
    StateWithRunMethod(Pattern.Twinkle_Neon, Twinkle, dict(colours=neon)),
    # Full twinkle
    # StateWithRunMethod(
    #     Pattern.FullTwinkle_Retro, Twinkle, dict(colours=retroColoursList, timeBetweenTwinkles=0.01)
    # ),
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
        dict(colours=[pleasantWhite], **GLITTER_CONFIG),
    ),
    # StateWithRunMethod(
    #     Pattern.Glitter_Retro,
    #     Twinkle,
    #     dict(colours=retroColoursList, **GLITTER_CONFIG),
    # ),
    # StateWithRunMethod(
    #     Pattern.Glitter_Random,
    #     TwinkleFromColourAlgorithm,
    #     dict(colourGenerator=trulyRandom, **GLITTER_CONFIG),
    # ),
    # StateWithRunMethod(
    #     Pattern.Glitter_Analagous,
    #     TwinkleFromColourAlgorithm,
    #     dict(
    #         colourGenerator=randomColourAnalogous,
    #         secondsBetweenPaletteChanges=0,
    #         secondsBetweenColourChanges=5,
    #         numberOfColours=3,
    #         **GLITTER_CONFIG
    #     ),
    # ),
    # StateWithRunMethod(
    #     Pattern.Glitter_AnalagousWeighted,
    #     TwinkleFromColourAlgorithm,
    #     dict(colourGenerator=randomAnalogousWeighted, numberOfColours=3, **GLITTER_CONFIG),
    # ),
    # StateWithRunMethod(
    #     Pattern.Glitter_Complementary,
    #     TwinkleFromColourAlgorithm,
    #     dict(colourGenerator=randomComplementary, numberOfColours=6, **GLITTER_CONFIG),
    # ),
    StateWithRunMethod(
        Pattern.Glitter_SplitComplementary,
        TwinkleFromColourAlgorithm,
        dict(colourGenerator=randomSplitComplementary, numberOfColours=5, **GLITTER_CONFIG),
    ),
    StateWithRunMethod(
        Pattern.Glitter_137Degrees,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=randomColour137Degrees,
            secondsBetweenColourChanges=5,
            numberOfColours=6,
            **GLITTER_CONFIG
        ),
    ),
    StateWithRunMethod(
        Pattern.Glitter_ColourWheel,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=colourWheel,
            secondsBetweenPaletteChanges=0,
            secondsBetweenColourChanges=4,
            **GLITTER_CONFIG
        ),
    ),
    StateWithRunMethod(
        Pattern.Glitter_ColourWheelFast,
        TwinkleFromColourAlgorithm,
        dict(
            colourGenerator=colourWheel,
            secondsBetweenPaletteChanges=0,
            secondsBetweenColourChanges=1,
            **GLITTER_CONFIG
        ),
    ),
    StateWithRunMethod(
        Pattern.Glitter_CoolorPalletes,
        TwinkleFromPalettes,
        dict(palettes=coolors, **GLITTER_CONFIG),
    ),
    # Cycle
    # StateWithRunMethod(Pattern.Cycle_Retro, Cycle, dict(colours=retroColoursList)),
    StateWithRunMethod(Pattern.Cycle_Rainbow, Cycle, dict(colours=Rainbow)),
    # Off
    StateOff(Pattern.Off),
]


class FairyLightPatterns(Machine):
    def __init__(self, leds):
        print("Starting FairyLightpatterns...")
        self.leds = leds
        self.machine = Machine(
            self,
            states=states,
            # initial=states[len(states) - 1],
            # initial=states[randrange(0, len(states))],
            initial=states[3],
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

    def getCurrentPattern(self):
        return self.state.name
