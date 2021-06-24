from leds.Leds import Leds
from utils.randomColour import randomSplitComplementary

# from utils.colourWheel import COLOUR_WHEEL

leds = Leds()

try:
    f = randomSplitComplementary()
    leds.setLeds([f() for _ in range(50)])

    # print([c.luminance for c in COLOUR_WHEEL])
    # print([c.saturation for c in COLOUR_WHEEL])

    # leds.setLeds([COLOUR_WHEEL[i % 12] for i in range(50)])

except KeyboardInterrupt:
    # Cleanup
    leds.clear()
    print("Done")
