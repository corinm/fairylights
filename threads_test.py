from transitions import Machine, State
from time import sleep
import multiprocessing


def runA():
    while True:
        print('Loop a')
        sleep(2)


def runB():
    while True:
        print('Loop b')
        sleep(2)


def runC():
    while True:
        print('Loop c')
        sleep(2)


class TestFsm():
    states = [
        State(name='init'),
        State(name='a', on_enter=['runA']),
        State(name='b', on_enter=['runB']),
        State(name='c', on_enter=['runC']),
    ]

    transitions = [
        {'trigger': 'initialise', 'source': states[0], 'dest': states[1]},
        {'trigger': 'buttonPressed', 'source': states[1], 'dest': states[2]},
        {'trigger': 'buttonPressed', 'source': states[2], 'dest': states[3]},
        {'trigger': 'buttonPressed', 'source': states[3], 'dest': states[1]},
    ]

    def __init__(self):
        print('Starting...')
        self.machine = Machine(self, states=self.states,
                               transitions=self.transitions, initial=self.states[0], after_state_change='printState')
        self.transition = False
        self.initialise()

    def printState(self):
        print("Now in state: ", self.state)

    def runA(self):
        print('Running a')
        self.p1 = multiprocessing.Process(target=runA)
        self.p1.start()

    def runB(self):
        print('Running b')
        self.p2 = multiprocessing.Process(target=runB)
        self.p2.start()

    def runC(self):
        print('Running c')
        self.p3 = multiprocessing.Process(target=runC)
        self.p3.start()

    def buttonPressed(self):
        print("Button pressed")
        self.p1.terminate()
        self.p2.terminate()
        self.p3.terminate()
        self.trigger('buttonPressed')


class Button:
    def __init__(self, callback):
        self.callback = callback

    def press(self):
        self.callback()


test = TestFsm()
button = Button(test.buttonPressed)
sleep(5)
button.press()
sleep(5)
button.press()
sleep(5)
button.press()
