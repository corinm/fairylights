from leds.Leds import Leds
from random_twinkling.RandomTwinkling import RandomTwinkling
from utils.colours import coolors

leds = Leds()

try:
    counter = 0
    index = 0
    rt = RandomTwinkling(50, coolors[index])

    while True:
        if counter >= 200:
            counter = 0
            index += 1
            print("Update")
            rt.updateColours(coolors[index])

        leds.setLeds(rt.tick())
        counter += 1


except KeyboardInterrupt:
    # Cleanup
    leds.clear()
    print("Done")
