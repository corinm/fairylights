
class MockDisplay:
    def __init__(self):
        pass

    def renderMessage(self, message: str):
        print(f'Render: {message}')
