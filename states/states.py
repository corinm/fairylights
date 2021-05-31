from transitions import Machine, State

states = [
    State(name='Init', on_enter=['initialise']),
    State(name='FlickeringFairyLights'),
    State(name='RandomTwinkling'),
    State(name='FireFlies')]

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

    def showState(self):
        self.display(f'New state: {self.state}')


def main(button, display):
    fl = FairyLights(button, display)
    fl.initialise()
    fl.buttonPressed()


button = 'button'


class Button:
    def __init__(self, callback):
        self.callback = callback

    def press(self):
        self.callback()


def display(title: str):
    print(title)


main(button, display)
