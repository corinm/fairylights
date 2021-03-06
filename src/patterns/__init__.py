from enum import Enum, auto
from typing import Callable, List, Type, Union

from transitions import Machine, State

from leds.Leds import Leds
from colours import warmWhite, yellow, iceWhite, retro, trulyRandom, analogousRandom, analogousWeightedRandom, complementaryRandom, splitComplementaryRandom, every137Degrees, colourWheel, coolorPalettes, neon, rainbow, eighties, northernLights
from effects import Twinkle, FirefliesConstant, Cycle
from utils.StoppableThread import StoppableThread

# from random import randrange


class Pattern(Enum):
    Flickering = auto()


    Twinkle_Warm = auto()
    Twinkle_Yellow = auto()
    Twinkle_Ice = auto()
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
    Twinkle_80s = auto()
    Twinkle_NorthernLights = auto()

    FullTwinkle_Retro = auto()
    FullTwinkle_ColourWheelFast = auto()
    FullTwinkle_80s = auto()
    FullTwinkle_NorthernLights = auto()

    Fireflies_GlowConstant = auto()

    Glitter_Warm = auto()
    Glitter_Ice = auto()
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
    Glitter_Neon = auto()
    Glitter_80s = auto()
    Glitter_NorthernLights = auto()

    Cycle_Rainbow = auto()

    Off = auto()


class StateWithRunMethod(State):
    def __init__(
        self,
        name: Pattern,
        patternManager: Union[
            Type[Twinkle],
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
    StateWithRunMethod(Pattern.Twinkle_Warm, Twinkle, dict(colours=warmWhite)),
    StateWithRunMethod(Pattern.Twinkle_Yellow, Twinkle, dict(colours=yellow)),
    StateWithRunMethod(Pattern.Twinkle_Ice, Twinkle, dict(colours=iceWhite)),
    StateWithRunMethod(Pattern.Twinkle_Retro, Twinkle, dict(colours=retro)),
    StateWithRunMethod(
        Pattern.Twinkle_Random, Twinkle, dict(colours=trulyRandom)
    ),
    StateWithRunMethod(
        Pattern.Twinkle_Analagous,
        Twinkle,
        dict(
            colours=analogousRandom,
            secondsBetweenColourChanges=5,
        ),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_AnalagousWeighted,
        Twinkle,
        dict(colours=analogousWeightedRandom),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_Complementary,
        Twinkle,
        dict(colours=complementaryRandom),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_SplitComplementary,
        Twinkle,
        dict(colours=splitComplementaryRandom),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_137Degrees,
        Twinkle,
        dict(
            colours=every137Degrees, secondsBetweenColourChanges=5
        ),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_ColourWheel,
        Twinkle,
        dict(
            colours=colourWheel,
            secondsBetweenColourChanges=4,
        ),
    ),
    StateWithRunMethod(
        Pattern.Twinkle_ColourWheelFast,
        Twinkle,
        dict(
            colours=colourWheel,
            secondsBetweenColourChanges=1,
        ),
    ),
    StateWithRunMethod(Pattern.Twinkle_CoolorPalletes, Twinkle, dict(colours=coolorPalettes)),
    StateWithRunMethod(Pattern.Twinkle_Neon, Twinkle, dict(colours=neon)),
    StateWithRunMethod(Pattern.Twinkle_80s, Twinkle, dict(colours=eighties)),
    StateWithRunMethod(Pattern.Twinkle_NorthernLights, Twinkle, dict(colours=northernLights, secondsBetweenColourChanges=2)),

    # Full twinkle
    StateWithRunMethod(
        Pattern.FullTwinkle_Retro, Twinkle, dict(colours=retro, timeBetweenTwinkles=0.01)
    ),
    StateWithRunMethod(
        Pattern.FullTwinkle_ColourWheelFast,
        Twinkle,
        dict(
            colours=colourWheel,
            secondsBetweenColourChanges=1,
            timeBetweenTwinkles=0.01,
        ),
    ),
    StateWithRunMethod(
        Pattern.FullTwinkle_80s,
        Twinkle,
        dict(
            colours=eighties,
            secondsBetweenColourChanges=1,
            timeBetweenTwinkles=0.01,
        ),
    ),
    StateWithRunMethod(Pattern.FullTwinkle_NorthernLights, Twinkle, dict(colours=northernLights, secondsBetweenColourChanges=2)),
    
    # Fireflies
    StateWithRunMethod(Pattern.Fireflies_GlowConstant, FirefliesConstant, dict()),

    # Glitter
    StateWithRunMethod(
        Pattern.Glitter_Warm,
        Twinkle,
        dict(colours=warmWhite, **GLITTER_CONFIG),
    ),
    StateWithRunMethod(
        Pattern.Glitter_Ice,
        Twinkle,
        dict(colours=iceWhite, **GLITTER_CONFIG),
    ),
    StateWithRunMethod(
        Pattern.Glitter_Retro,
        Twinkle,
        dict(colours=retro, **GLITTER_CONFIG),
    ),
    StateWithRunMethod(
        Pattern.Glitter_Random,
        Twinkle,
        dict(colours=trulyRandom, **GLITTER_CONFIG),
    ),
    StateWithRunMethod(
        Pattern.Glitter_Analagous,
        Twinkle,
        dict(
            colours=analogousRandom,
            secondsBetweenColourChanges=5,
            **GLITTER_CONFIG
        ),
    ),
    StateWithRunMethod(
        Pattern.Glitter_AnalagousWeighted,
        Twinkle,
        dict(colours=analogousWeightedRandom, **GLITTER_CONFIG),
    ),
    StateWithRunMethod(
        Pattern.Glitter_Complementary,
        Twinkle,
        dict(colours=complementaryRandom, **GLITTER_CONFIG),
    ),
    StateWithRunMethod(
        Pattern.Glitter_SplitComplementary,
        Twinkle,
        dict(colours=splitComplementaryRandom, **GLITTER_CONFIG),
    ),
    StateWithRunMethod(
        Pattern.Glitter_137Degrees,
        Twinkle,
        dict(
            colours=every137Degrees,
            secondsBetweenColourChanges=5,
            **GLITTER_CONFIG
        ),
    ),
    StateWithRunMethod(
        Pattern.Glitter_ColourWheel,
        Twinkle,
        dict(
            colours=colourWheel,
            secondsBetweenColourChanges=4,
            **GLITTER_CONFIG
        ),
    ),
    StateWithRunMethod(
        Pattern.Glitter_ColourWheelFast,
        Twinkle,
        dict(
            colours=colourWheel,
            secondsBetweenColourChanges=1,
            **GLITTER_CONFIG
        ),
    ),
    StateWithRunMethod(
        Pattern.Glitter_CoolorPalletes,
        Twinkle,
        dict(colours=coolorPalettes, **GLITTER_CONFIG),
    ),
    StateWithRunMethod(
        Pattern.Glitter_Neon,
        Twinkle,
        dict(colours=neon, **GLITTER_CONFIG),
    ),
    StateWithRunMethod(
        Pattern.Glitter_80s,
        Twinkle,
        dict(colours=eighties, **GLITTER_CONFIG),
    ),
    StateWithRunMethod(Pattern.Glitter_NorthernLights, Twinkle, dict(colours=northernLights, secondsBetweenColourChanges=2, **GLITTER_CONFIG)),

    # Cycle
    StateWithRunMethod(Pattern.Cycle_Rainbow, Cycle, dict(colours=rainbow)),
    
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
            initial=states[len(states) - 1],
            # initial=states[randrange(0, len(states))],
            # initial=states[31],
        )
        self.machine.add_transition(trigger="stop", source=[s.name for s in states], dest="Off")
        self.machine.add_ordered_transitions(before=self.on_exit, after=self.on_enter)
        self.thread: Union[StoppableThread, None] = None

    def _stopThread(self):
        if self.thread is not None:
            print("???????  Asking thread to stop")
            self.thread.stop()
            self.thread.join()
            print("???????  Thread joined")
            self.thread = None

    def stop(self):
        self._stopThread()

    def _runState(self, state: Pattern):
        runMethod = self.machine.states[state.name].run

        if not callable(runMethod):
            raise ValueError("run method not callable")

        self.thread = StoppableThread(target=runMethod, args=(self.leds,))
        self.thread.setDaemon(True)
        print("???? Starting thread")
        self.thread.start()
        print("???? Thread started")

    def next(self):
        self.trigger("next_state")

    def on_enter(self):
        print("??????  Entering:", self.state)
        self._runState(self.state)

    def on_exit(self):
        print("??????  Leaving: ", self.state)
        self._stopThread()

    def toPattern(self, stateName: Pattern):
        self._runState(stateName)

    def getCurrentPattern(self):
        return self.state.name
