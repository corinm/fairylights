import multiprocessing
from time import sleep
from typing import List, Union

from transitions import Machine, State

from .patterns import FairyLightPatterns

modeStates: List[State] = [
    State(name="init"),
    State(name="cycle"),
    State(name="static"),
]

modeStatesSerialised = [(i, modeStates[i].name) for i in range(len(modeStates))]


class FairyLightModes(Machine):
    def __init__(self, leds):
        print("Starting...")
        self.leds = leds
        self.machine = Machine(
            self,
            states=modeStates,
            initial=modeStates[0],
        )
        self.machine.add_transition("start", source="init", dest="cycle")
        self.machine.add_transition("toStatic", source="cycle", dest="static")
        self.machine.add_transition("toCycle", source="static", dest="cycle")
        self.process: Union[multiprocessing.Process, None] = None
        self.patterns = FairyLightPatterns(leds)
        self.trigger("start")

    def on_enter_cycle(self):
        print("on_enter_cycle")

        # firstPatternName, _ = next(iter(self.patterns.machine.states.items()))
        # print(firstPatternName)
        # self.patterns.machine.

        self.process = multiprocessing.Process(target=self._runCycle, args=(self.leds,))
        self.process.start()

    def _runCycle(self, leds):
        patterns = FairyLightPatterns(leds)

        while True:
            print("Looping")
            patterns.next()
            sleep(15)

    def on_enter_static(self, pattern):
        print("on_enter_static")

        if self.process is not None and self.process.is_alive() is True:
            self.process.terminate()
            self.process = None

    def cycle(self):
        self.trigger("toCycle")

    def static(self, pattern: str):
        if self.state != "static":
            self.trigger("toStatic", pattern)

        self.patterns.toPattern(pattern)
