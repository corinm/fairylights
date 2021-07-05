import multiprocessing
from time import sleep
from typing import List

from transitions import Machine, State

from .patterns import FairyLightPatterns

modeStates: List[State] = [
    State(name="stopped"),
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
        self.machine.add_transition("start", source="stopped", dest="cycle")
        self.machine.add_transition("toStatic", ["static", "cycle", "stopped"], dest="static")
        self.machine.add_transition("toCycle", source=["static", "cycle", "stopped"], dest="cycle")
        self.machine.add_transition("stop", source=["static", "cycle", "stopped"], dest="stopped")
        self.patterns = FairyLightPatterns(leds)
        self.process = None
        self.trigger("start")

    def _runCycle(self):
        while True:
            print("Looping")
            self.patterns.next()
            sleep(15)

    def on_enter_cycle(self):
        print("on_enter_cycle")
        if self.process is not None:
            self.process.terminate()
            self.process = None

        self.process = multiprocessing.Process(target=self._runCycle)
        self.process.start()

    def on_enter_static(self, pattern):
        print("on_enter_static")

        if self.process is not None:
            self.process.terminate()
            self.process = None

        self.patterns.toPattern(pattern)

    def on_enter_stopped(self):
        print("modes.son_enter_stopped")

        if self.process is not None:
            self.process.terminate()
            self.process = None

        self.patterns.stop()

    def cycle(self):
        self.trigger("toCycle")

    def static(self, pattern: str):
        self.trigger("toStatic", pattern)

    def stop(self):
        print("modes.stop")
        self.trigger("stop")
