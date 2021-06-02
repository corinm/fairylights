from colour import Color

MAX_TEMP_INCREMENT = 2
MIN_TEMP_INCREMENT = 1
MAX_TEMP_DECREMENT = 2
MIN_TEMP_DECREMENT = 1
OFF_TEMP = 100
ON_TEMP = 90


off = Color(rgb=(0, 0, 0))

flicker2_4V = Color('#263a01')  # Dimmer
flicker3V = Color('#609103')  # Bright

flickerColours = list(flicker3V.range_to(flicker2_4V, 11))
flickerMid = flickerColours[5]  # For "DIM" flicker bulbs
