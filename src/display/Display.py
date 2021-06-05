import multiprocessing
from time import sleep
from typing import Union

import adafruit_ssd1306
import busio
from board import SCL, SDA
from PIL import Image, ImageDraw, ImageFont

MODE = "1"  # 1-bit colour
PIXEL_WIDTH = 128
PIXEL_HEIGHT = 32


class Display:
    def __init__(self):
        i2c = busio.I2C(SCL, SDA)
        self.display = adafruit_ssd1306.SSD1306_I2C(PIXEL_WIDTH, PIXEL_HEIGHT, i2c)
        self.clearDisplay()
        self.image = Image.new(MODE, (self.display.width, self.display.height))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.rectangle(
            (0, 0, self.display.width, self.display.height), outline=0, fill=0
        )
        padding = -2
        self.top = padding
        # bottom = self.display.height - padding
        self.x = 0
        self.font = ImageFont.load_default()

        self.process: Union[multiprocessing.Process, None] = None

    def _renderMessage(self, message: str):
        self.draw.text((self.x, self.top), message, font=self.font, fill=255)
        self.display.image(self.image)
        self.display.show()
        sleep(5)
        self.clearDisplay()

    def renderMessage(self, message: str):
        self.clearAnyPreviousMessage()

        self.process = multiprocessing.Process(
            target=self._renderMessage, args=(message,)
        )
        self.process.start()

    def clearAnyPreviousMessage(self):
        if self.process is not None and self.process.is_alive() is True:
            self.process.terminate()
            self.process = None
        self.clearDisplay()

    def clearDisplay(self):
        self.display.fill(0)
        self.display.show()
