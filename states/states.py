from transitions import Machine, State

from flickering_fairylights import FlickeringFairyLights
from random_twinkling.RandomTwinkling import RandomTwinkling

states = [
    State(name='Init', on_enter=['initialise']),
    State(name='FlickeringFairyLights', on_enter=['runFlickeringFairyLights']),
    State(name='RandomTwinkling', on_enter=['runRandomTwinkling']),
    State(name='Fireflies', on_enter=['runFireflies'])]

transitions = [
    ['initialise', states[0], states[1]],
    {'trigger': 'buttonPressed', 'source': states[1], 'dest': states[2]},
    {'trigger': 'buttonPressed', 'source': states[2], 'dest': states[3]},
    {'trigger': 'buttonPressed', 'source': states[3], 'dest': states[1]},
]


class FairyLights(object):
    def __init__(self, button, display):
        self.button = button
        self.display = display
        self.machine = Machine(self, states=states,
                               transitions=transitions, initial=states[0], after_state_change='showState')
        self.to_FlickeringFairyLights()

    def showState(self):
        print('SHOW_STATE')
        self.display(f'New state: {self.state}')

    def runFlickeringFairyLights(self):
        print('Flicker')
        ff = FlickeringFairyLights()

        while True:
            ff.tick()

    def runRandomTwinkling(self):
        print('Twinkle')
        rt = RandomTwinkling()

        while True:
            rt.tick()

    def runFireflies(self):
        print('*** 3')


def main(button, display):
    print('Starting...')
    fl = FairyLights(button, display)
    fl.initialise()
    fl.buttonPressed()
    fl.buttonPressed()
    fl.buttonPressed()
