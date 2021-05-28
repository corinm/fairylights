from rainbow import rainbow
from time import sleep
import rpi_ws281x as ws
import math

from FlickeringFairyLights import FlickeringFairyLights
import config
import ledColours


strip = ws.Adafruit_NeoPixel(config.LED_COUNT, config.LED_PIN, config.LED_FREQ_HZ,
                             config.LED_DMA, config.LED_INVERT, config.LED_BRIGHTNESS, config.LED_CHANNEL)

strip.begin()

try:
    print("Starting...")
    flickering = FlickeringFairyLights()

    while True:
        leds = flickering.tick()

        for i in range(strip.numPixels()):
            led = leds[i]
            r = round(led.red * 255)
            g = round(led.green * 255)
            b = round(led.blue * 255)
            strip.setPixelColorRGB(i, r, g, b)
            strip.show()

    # while True:
    #     bulbs = rainbow(strip.numPixels())
    #     for i, bulb in enumerate(bulbs):
    #         strip.setPixelColorRGB(
    #             i, math.floor(bulb.red * 255), math.floor(bulb.green * 255), math.floor(bulb.blue * 255))
    #         strip.show()

    # while True:
    #     for i in range(50):
    #         c = ledColours.shades[i]
    #         strip.setPixelColorRGB(i, math.floor(
    #             c.red * 255), math.floor(c.green * 255), math.floor(c.blue * 255))
    #     strip.show()

    # counter = 6
    # while True:
    #     print(counter, '/255')
    #     for i in range(strip.numPixels()):
    #         r = counter
    #         g = counter
    #         b = counter
    #         strip.setPixelColorRGB(i, r ** 2, g ** 2, b ** 2)
    #         strip.show()

    # if ((counter + 1) ** 2 <= 255):
    #     counter = counter + 1
    # else:
    #     break

    # sleep(0.05)

except KeyboardInterrupt:
    print('Done')
