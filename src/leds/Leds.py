from typing import List

import rpi_ws281x as ws
from colour import Color

from utils.colours import off

# LED strip configuration:
LED_COUNT = 50  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!)
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53


class Leds:
    def __init__(self):
        self.strip = ws.Adafruit_NeoPixel(
            LED_COUNT,
            LED_PIN,
            LED_FREQ_HZ,
            LED_DMA,
            LED_INVERT,
            LED_BRIGHTNESS,
            LED_CHANNEL,
        )
        self.strip.begin()

    def setLeds(self, colours: List[Color]):
        for i in range(self.strip.numPixels()):

            try:
                colour = colours[i]
            except IndexError:
                colour = Color(None)

            r = round(colour.green * 255)
            g = round(colour.red * 255)
            b = round(colour.blue * 255)
            self.strip.setPixelColorRGB(i, r, g, b)
        self.strip.show()

    def clear(self):
        self.setLeds([off])
