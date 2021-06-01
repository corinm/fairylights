from typing import Dict

from .Firefly import Direction, Firefly

leds = [0 for i in range(50)]
Fireflies: Dict[int, Firefly] = {}


def tick():
    # Increment any existing Fireflies
    for f in Fireflies.values():
        f.state = f.state + 1

    # Move any existing Fireflies
    for key, f in Fireflies.items():
        if f.direction == Direction.UP:
            leds[key+1] = leds[key]

        # Delete any finished Fireflies and clear led
        # Pick an empty led
        # Create firefly and store it
        pass


print(leds)
