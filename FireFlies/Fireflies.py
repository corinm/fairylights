from typing import Dict

from FireFlies.Firefly import Direction, Firefly

leds = [0 for i in range(50)]
fireflies: Dict[int, Firefly] = {}


def tick():
    # Increment any existing fireflies
    for f in fireflies.values():
        f.state = f.state + 1

    # Move any existing fireflies
    for key, f in fireflies.items():
        if f.direction == Direction.UP:
            leds[key+1] = leds[key]

        # Delete any finished fireflies and clear led
        # Pick an empty led
        # Create firefly and store it
        pass


print(leds)
