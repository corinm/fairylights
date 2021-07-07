from time import sleep, time
from typing import Callable, List, Union

from transitions import Machine, State

from utils.StoppableThread import StoppableThread

from .patterns import FairyLightPatterns, Pattern

modeStates: List[State] = [
    State(name="stopped"),
    State(name="cycle"),
    State(name="static"),
]

modeStatesSerialised = [(i, modeStates[i].name) for i in range(len(modeStates))]


class FairyLightModes(Machine):
    def __init__(self, leds):
        print("Starting FairyLightModes...")
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
        self.thread: Union[StoppableThread, None] = None
        self.trigger("start")

    def _runCycle(self, shouldStop: Callable[[], bool]):
        t = time() + 15
        while not shouldStop():
            if time() > t:
                t = time() + 15
                self.patterns.next()
            else:
                sleep(2)

    def on_enter_cycle(self):
        print("on_enter_cycle")
        if self.thread is not None:
            self.thread.stop()
            self.thread.join()
            self.thread = None

        self.thread = StoppableThread(target=self._runCycle, args=())
        self.thread.setDaemon(True)
        self.thread.start()
        print("cycle thread started")

    def on_enter_static(self, pattern: Pattern):
        print("on_enter_static")

        if self.thread is not None:
            print("Stopping modes cycle thread")
            self.thread.stop()
            self.thread.join()
            self.thread = None

        self.patterns.toPattern(pattern)

    def on_enter_stopped(self):
        print("modes.son_enter_stopped")

        if self.thread is not None:
            self.thread.stop()
            self.thread.join()
            self.thread = None

        self.patterns.stop()

    def cycle(self):
        self.trigger("toCycle")

    def static(self, pattern: Pattern):
        self.trigger("toStatic", pattern)

    def stop(self):
        print("modes.stop")
        self.trigger("stop")
