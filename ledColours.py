from colour import Color

from rainbow import generateColourWheel

wheel = generateColourWheel()

off = Color(rgb=(0, 0, 0))

# flicker3V = Color(rgb=(60/255, 46/255, 9/255))
# flicker2_4V = Color(rgb=(60*0.25/255, 46*0.25/255, 9*0.25/255))
flicker3V = Color(rgb=(60/255, 46/255, 9/255))  # Dimmer
flicker2_4V = Color(rgb=(60*0.25/255, 46*0.25/255, 9*0.25/255))  # Brighter

flickerColours = list(flicker2_4V.range_to(flicker3V, 11))
