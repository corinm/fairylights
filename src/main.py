import signal
import sys

from leds.Leds import Leds
from states.modes import FairyLightModes

# from api.api import runApiServer


def sigterm_handler(_signo, _stack_frame):
    sys.exit(0)


def main():
    signal.signal(signal.SIGTERM, sigterm_handler)

    leds = Leds()
    FairyLightModes(leds)

    try:
        while True:
            pass

    finally:
        leds.clear()


if __name__ == "__main__":
    main()
