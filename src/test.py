from colour import Color

from glitter.Glitter import Glitter
from leds.Leds import Leds

try:
    leds = Leds()

    blue1 = Color("blue")
    blue1.luminance = 0.1
    blue1.saturation = 0.4

    blue2 = Color("blue")
    blue2.luminance = 0.05
    blue2.saturation = 0.6

    g = Glitter(50, [blue1, blue2])

    while True:
        leds.setLeds(g.tick())

except KeyboardInterrupt:
    # Cleanup
    print("Done")
