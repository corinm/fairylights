from typing import List

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
        self.machine.add_transition("toStatic", ["static", "cycle"], dest="static")
        self.machine.add_transition("toCycle", source="static", dest="cycle")
        self.patterns = FairyLightPatterns(leds)
        self.trigger("start")

    def on_enter_cycle(self):
        print("on_enter_cycle")
        # while True:
        #     print("Looping")
        #     self.patterns.next()
        #     sleep(15)

    def on_enter_static(self, pattern):
        print("on_enter_static")
        self.patterns.toPattern(pattern)

    def cycle(self):
        self.trigger("toCycle")

    def static(self, pattern: str):
        self.trigger("toStatic", pattern)
