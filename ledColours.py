from colour import Color
import math

from rainbow import generateColourWheel


def printColour(colour: Color):
    print(math.floor(
        colour.red * 255), math.floor(colour.green * 255), math.floor(colour.blue * 255))


wheel = generateColourWheel()

off = Color(rgb=(0, 0, 0))

# flicker3V = Color(rgb=(60/255, 46/255, 9/255))
# flicker2_4V = Color(rgb=(60*0.25/255, 46*0.25/255, 9*0.25/255))

flicker2_4V = Color(rgb=(50/255, 70/255, 3/255))  # Dimmer
flicker3V = Color(rgb=(99/255, 134/255, 5/255))  # Bright

flickerColours = list(flicker3V.range_to(flicker2_4V, 11))

# Shades of yellow/orange to white
# 0 (85, 170, 0)
# 1 (92, 157, 2)
# 2 (96, 145, 3)
# 3 (99, 134, 5)
# 4 (100, 122, 6)
# 5 (99, 111, 7)
# 6 (97, 100, 8)
# 7 (90, 86, 9)
# 8 (79, 71, 9)
# 9 (69, 57, 9)
