from colour import Color

from leds.Leds import Leds

black = Color(None)
blue = Color(rgb=(0, 0, 50 / 255))
red = Color(rgb=(50 / 255, 0, 0))

red6 = [red for _ in range(7)]
blue6 = [blue for _ in range(7)]
off6 = [black for _ in range(7)]
bar = [black for _ in range(8)]

# 101--101
l1 = red6 + off6 + red6 + bar + blue6 + off6 + blue6

# 010--010
l2 = off6 + red6 + off6 + bar + off6 + blue6 + off6


order = [
    l1,
    l1,
    l1,
    l1,
    l2,
    l2,
    l2,
    l2,
]

try:
    leds = Leds()

    counter = 0
    while True:
        colours = order[counter % len(order)]
        leds.setLeds(colours)
        counter += 1

except KeyboardInterrupt:
    # Cleanup
    print("Done")
