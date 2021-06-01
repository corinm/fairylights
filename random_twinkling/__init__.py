from .RandomTwinkling import RandomTwinkling

from time import sleep
from colour import Color


def run():
    rt = RandomTwinkling(50, Color(color='blue'))

    while True:
        print('rt.tick')
        rt.tick()
        sleep(1)
