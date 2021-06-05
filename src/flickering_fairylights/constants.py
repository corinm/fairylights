from colour import Color

MAX_TEMP_INCREMENT = 2
MIN_TEMP_INCREMENT = 1
MAX_TEMP_DECREMENT = 2
MIN_TEMP_DECREMENT = 1
OFF_TEMP = 100
ON_TEMP = 90


off = Color(rgb=(0, 0, 0))

# 72,39,1 -> 145,90,3 is quite nice
flicker2_4V = Color(rgb=(72 / 255, 32 / 255, 1 / 255))  # Dimmer
flicker3V = Color(rgb=(145 / 255, 80 / 255, 3 / 255))  # Bright

flickerColours = list(flicker3V.range_to(flicker2_4V, 11))
flickerMid = flickerColours[5]  # For "DIM" flicker bulbs

# 263a01 - 38,58,1
# 282D00 - 40,45,0
# 262801 - rgb(38,40,1)
