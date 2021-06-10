from typing import Dict

from colour import Color

"""
   Retro colours e.g. Noma Pickwick fairy lights
"""
retroColours: Dict[str, Color] = {
    "pink": Color(rgb=(93 / 255, 19 / 255, 56 / 255)),
    "blue": Color(rgb=(11 / 255, 77 / 255, 57 / 255)),
    "orange": Color(rgb=(199 * 0.8 / 255, 90 * 0.8 / 255, 0 * 0.8 / 255)),
    "green": Color(rgb=(54 * 0.4 / 255, 139 / 255, 27 * 0.4 / 255)),
    "red": Color(rgb=(184 * 0.7 / 255, 44 * 0.4 / 255, 8 * 0.4 / 255)),
}

"""
   80s colours
"""
blue80s = Color(rgb=(11 / 255, 77 / 255, 57 / 255))
pink80s = Color(rgb=(57 / 255, 11 / 255, 77 / 255))

"""
   General
"""
off = Color(None)

"""
   Fireflies
   Original: rgb=(241 / 255, 250 / 255, 13 / 255)
"""
fireflies: Dict[str, Color] = {
    "bright": Color(rgb=(96 / 255, 100 / 255, 5 / 255)),
    "darker": Color(rgb=(38 / 255, 40 / 255, 2 / 255)),
}

"""
   Flickering fairy lights
"""
# 72,39,1 -> 145,90,3 is quite nice
_flicker2_4V = Color(rgb=(72 / 255, 32 / 255, 1 / 255))  # Dimmer
_flicker3V = Color(rgb=(145 / 255, 80 / 255, 3 / 255))  # Bright

flickerColours = list(_flicker3V.range_to(_flicker2_4V, 11))
flickerMid = flickerColours[5]  # For "DIM" flicker bulbs

# 263a01 - 38,58,1
# 282D00 - 40,45,0
# 262801 - rgb(38,40,1)
