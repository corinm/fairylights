import time
from leds.Leds import Leds
from colour import Color


try:
    flicker2_4V = Color(rgb=(57/255, 87/255, 1/255))  # Dimmer
    flicker3V = Color(rgb=(96/255, 145/255, 3/255))  # Bright

    STEPS_FROM_OFF_TO_ON = 5
    off = Color()

    # 1 = GRB

    colour = Color('#0000ff')
    print(colour.red, colour.green, colour.blue)

    rangeLs = [(i / (STEPS_FROM_OFF_TO_ON - 1)) * colour.luminance
               for i in range(STEPS_FROM_OFF_TO_ON)]

    range = []
    for lum in rangeLs:
        newColour = Color(colour)
        newColour.luminance = lum
        range.append(newColour)

    print(rangeLs, range)
    leds = Leds()
    leds.setLeds(range)


except KeyboardInterrupt:
    # Cleanup
    print('Done')
