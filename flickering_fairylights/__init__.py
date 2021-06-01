from .FlickeringFairyLights import FlickeringFairyLights

from time import sleep


def run():
    ff = FlickeringFairyLights()

    while True:
        print('ff.tick')
        ff.tick()
        sleep(1)
