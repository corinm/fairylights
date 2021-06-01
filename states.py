import multiprocessing
from typing import Union
from transitions import Machine, State

from flickering_fairylights import run as runFlickeringFairylights
from random_twinkling import run as runRandomTwinkling

from time import sleep


class Display:
    def show(self, title: str):
        print(title)


class Button:
    def __init__(self, callback):
        self.callback = callback

    def press(self):
        self.callback()


states = [
    State(name='Init'),
    State(name='FlickeringFairyLights'),
    State(name='RandomTwinkling'),
    # State(name='Fireflies')
]

transitions = [
    {'trigger': 'initialise', 'source': states[0], 'dest': states[1]},
    {'trigger': 'buttonPressed', 'source': states[1], 'dest': states[2]},
    {'trigger': 'buttonPressed', 'source': states[2], 'dest': states[1]},
    # {'trigger': 'buttonPressed', 'source': states[3], 'dest': states[1]},
]


class FairyLights(Machine):

    def __init__(self, display: Display):
        print('Starting...')
        self.display = display
        self.machine = Machine(self, states=states,
                               transitions=transitions, initial=states[0], after_state_change='showState')
        self.process: Union[multiprocessing.Process, None] = None
        self.trigger('initialise')

    def showState(self):
        self.display.show(f'New state: {self.state}')

    def buttonPressed(self):
        print('Button pressed')
        if self.process != None and self.process.is_alive() == True:
            self.process.terminate()
            self.process = None
        self.trigger('buttonPressed')

    def on_enter_FlickeringFairyLights(self):
        print('Flicker')
        self.process = multiprocessing.Process(target=runFlickeringFairylights)
        self.process.start()

    def on_enter_RandomTwinkling(self):
        print('Twinkle')
        self.process = multiprocessing.Process(target=runRandomTwinkling)
        self.process.start()

    # def runFireflies(self):
    #     print('Fireflies')


def main():
    display = Display()

    fl = FairyLights(display)

    button = Button(callback=fl.buttonPressed)

    sleep(5)

    button.press()
    sleep(5)
    button.press()
    sleep(5)
    button.press()


main()
