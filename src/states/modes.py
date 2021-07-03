from time import sleep
from typing import List

from transitions import Machine, State

from .patterns import FairyLightPatterns

states: List[State] = [
    State(name="init"),
    State(name="cycle"),
    State(name="static"),
]


class FairyLightModes(Machine):
    def __init__(self, leds):
        print("Starting...")
        self.leds = leds
        self.machine = Machine(
            self,
            states=states,
            initial=states[0],
        )
        self.machine.add_transition("start", source="init", dest="cycle")
        self.machine.add_transition("toStatic", source="cycle", dest="static")
        self.machine.add_transition("toCycle", source="static", dest="cycle")
        self.patterns = FairyLightPatterns(leds)
        self.trigger("start")

    def on_enter_cycle(self):
        print("on_enter_cycle")

        # firstPatternName, _ = next(iter(self.patterns.machine.states.items()))
        # print(firstPatternName)
        # self.patterns.machine.

        while True:
            self.patterns.next()
            sleep(15)

    def on_enter_static(self, pattern):
        print("on_enter_static")
