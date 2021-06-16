import signal
import sys
from time import sleep

from leds.Leds import Leds
from states.states import FairyLights


def sigterm_handler(_signo, _stack_frame):
    sys.exit(0)


def main():
    signal.signal(signal.SIGTERM, sigterm_handler)

    leds = Leds()
    fsm = FairyLights(leds)

    try:
        while True:
            sleep(5 * 60)
            fsm.next()

    finally:
        leds.clear()


if __name__ == "__main__":
    main()
