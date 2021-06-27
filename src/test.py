from leds.Leds import Leds
from random_twinkling import runCoolorPalettes

leds = Leds()

try:
    runCoolorPalettes(leds)

except KeyboardInterrupt:
    # Cleanup
    leds.clear()
    print("Done")
