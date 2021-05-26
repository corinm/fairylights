class Adafruit_NeoPixel(object):
    def __init__(
        self, num: int, pin: int, freq_hz=800000, dma=10, invert=False,
        brightness=255, channel=0, strip_type=ws.WS2811_STRIP_RGB
    ) -> None: ...
