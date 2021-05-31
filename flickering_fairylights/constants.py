from colour import Color

MAX_TEMP_INCREMENT = 5
MIN_TEMP_INCREMENT = 1
MAX_TEMP_DECREMENT = 3
MIN_TEMP_DECREMENT = 1
OFF_TEMP = 100
ON_TEMP = 95


off = Color(rgb=(0, 0, 0))

flicker2_4V = Color(rgb=(69/255, 40/255, 2/255))  # Dimmer
flicker3V = Color(rgb=(96/255, 145/255, 3/255))  # Bright

flickerColours = list(flicker3V.range_to(flicker2_4V, 11))
flickerMid = flickerColours[5]  # For "DIM" flicker bulbs
