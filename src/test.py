from fireflies import run
from leds.Leds import Leds

try:
    leds = Leds()
    run(leds)

except KeyboardInterrupt:
    # Cleanup
    print("Done")
