import threading

# Source: https://riptutorial.com/python/example/31665/stoppable-thread-with-a-while-loop


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self.target = kwargs.get("target")
        self.args = kwargs.get("args")
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def join(self, *args, **kwargs):
        self.stop()
        super(StoppableThread, self).join(*args, **kwargs)

    def run(self):
        self.target(*self.args, shouldStop=self._stop_event.is_set)
