from threading import Thread
from typing import Callable, Union

from leds.Leds import Leds
from patterns.twinkle import Twinkle
from utils.colours import retroColours

leds = Leds()


class RunnablePattern(Thread):
    def __init__(self, leds: Leds, runnableInstance, onStop):
        Thread.__init__(self)
        self.leds: Leds = leds
        self.runnableInstance = runnableInstance
        self.onStop: Callable = onStop
        self._stopped = False
        self.daemon = True
        self.start()

    def run(self):
        while not self._stopped:
            self.leds.setLeds(self.runnableInstance.tick())
        self.onStop()

    def stop(self):
        self._stopped = True


def onStop(leds: Leds):
    def stop():
        leds.clear()

    return stop


t = Twinkle(
    50,
    [
        retroColours["pink"],
        retroColours["blue"],
        retroColours["orange"],
        retroColours["green"],
        retroColours["red"],
    ],
)


rp: Union[RunnablePattern, None] = None

try:
    rp = RunnablePattern(leds, t, onStop(leds))
    print(">>> Main thread")

finally:
    if rp is not None:
        rp.stop()
