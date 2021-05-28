from colour import Color

from rainbow import angleToColour, generateColourWheel

wheel = generateColourWheel()

off = Color(rgb=(0, 0, 0))

# flicker3V = Color(rgb=(60/255, 46/255, 9/255))
# flicker2_4V = Color(rgb=(60*0.25/255, 46*0.25/255, 9*0.25/255))
flicker2_4V = Color(rgb=(100/255, 122/255, 6/255))  # Brighter
shades = list(flicker2_4V.range_to(off, 50))
flicker3V = shades[10]  # Dimmer

flickerColours = list(flicker2_4V.range_to(flicker3V, 11))


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
