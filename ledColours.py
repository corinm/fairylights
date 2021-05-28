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

flicker2_4V = Color(rgb=(69/255, 60/255, 2/255))  # Dimmer
flicker3V = Color(rgb=(96/255, 145/255, 3/255))  # Bright

flickerColours = list(flicker3V.range_to(flicker2_4V, 11))

# printColour(flickerColours[4])

# Shades of yellow/orange to white
# y0 = Color(rgb=(85/255, 170/255, 0/255))
# y1 = Color(rgb=(92/255, 157/255, 2/255))
# y2 = Color(rgb=(96/255, 145/255, 3/255))
# y3 = Color(rgb=(99/255, 134/255, 5/255))
# y4 = Color(rgb=(100/255, 122/255, 6/255))
# y5 = Color(rgb=(99/255, 111/255, 7/255))
# y6 = Color(rgb=(97/255, 100/255, 8/255))
# y7 = Color(rgb=(90/255, 86/255, 9/255))
# y8 = Color(rgb=(79/255, 71/255, 9/255))
# y9 = Color(rgb=(69/255, 57/255, 9/255))
# shades = [y0, y1, y2, y3, y4, y5, y6, y7, y8, y9]
