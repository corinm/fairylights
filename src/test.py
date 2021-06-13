from fireflies import runStaticGlow as run
from leds.Leds import Leds

leds = Leds()

try:
    run(leds)

except KeyboardInterrupt:
    # Cleanup
    leds.clear()
    print("Done")
