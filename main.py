import rpi_ws281x as ws

from FlickeringFairyLights import FlickeringFairyLights

# LED strip configuration:
LED_COUNT = 16      # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (18 uses PWM!)
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = ws.Adafruit_NeoPixel(
    LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

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

except KeyboardInterrupt:
    # Cleanup
    print('Done')
