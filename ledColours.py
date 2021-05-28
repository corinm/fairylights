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
y0 = Color(rgb=(85, 170, 0))
y1 = Color(rgb=(92, 157, 2))
y2 = Color(rgb=(96, 145, 3))
y3 = Color(rgb=(99, 134, 5))
y4 = Color(rgb=(100, 122, 6))
y5 = Color(rgb=(99, 111, 7))
y6 = Color(rgb=(97, 100, 8))
y7 = Color(rgb=(90, 86, 9))
y8 = Color(rgb=(79, 71, 9))
y9 = Color(rgb=(69, 57, 9))
shades = [y0, y1, y2, y3, y4, y5, y6, y7, y8, y9]
