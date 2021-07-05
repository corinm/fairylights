import signal
import sys

from api.api import runApiServer
from leds.Leds import Leds
from states.modes import FairyLightModes


def sigterm_handler(_signo, _stack_frame):
    sys.exit(0)


def main():
    signal.signal(signal.SIGTERM, sigterm_handler)

    leds = Leds()

    try:
        fsm = FairyLightModes(leds)
        runApiServer(fsm.cycle, fsm.static, fsm.stop)

    finally:
        leds.clear()


if __name__ == "__main__":
    main()
