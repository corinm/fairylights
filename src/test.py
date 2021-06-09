from leds.Leds import Leds
from utils.randomColour import randomAnalogousWeighted

try:
    leds = Leds()

    func = randomAnalogousWeighted()

    # while True:
    colours = [func() for _ in range(50)]
    leds.setLeds(colours)

except KeyboardInterrupt:
    # Cleanup
    print("Done")
