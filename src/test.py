from colour import Color

from leds.Leds import Leds

try:
    pink = Color(rgb=(91 / 255, 0 / 255, 45 / 255))
    pink2 = Color(rgb=(96 / 255, 38 / 255, 67 / 255))
    pink3 = Color(rgb=(93 / 255, 19 / 255, 56 / 255))
    blue = Color(rgb=(0 / 255, 53 / 255, 127 / 255))
    blue2 = Color(rgb=(0 / 255, 73 / 255, 127 / 255))
    orange = Color(rgb=(199 * 0.8 / 255, 90 * 0.8 / 255, 0 * 0.8 / 255))
    green = Color(rgb=(54 * 0.4 / 255, 139 / 255, 27 * 0.4 / 255))
    red = Color(rgb=(184 * 0.7 / 255, 44 * 0.4 / 255, 8 * 0.4 / 255))

    leds = Leds()
    colours = [pink3, blue, orange, green, blue2, red, Color()]
    leds.setLeds([colours[i % len(colours)] for i in range(50)])

    print([colour.red + colour.green + colour.blue for colour in colours])


except KeyboardInterrupt:
    # Cleanup
    print("Done")
