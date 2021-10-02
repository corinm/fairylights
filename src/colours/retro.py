from colour import Color

from .Colours import ColoursFromList

PINK = Color(rgb=(93 / 255, 19 / 255, 56 / 255))
BLUE = Color(rgb=(11 / 255, 77 / 255, 57 / 255))
ORANGE = Color(rgb=(199 * 0.8 / 255, 90 * 0.8 / 255, 0 * 0.8 / 255))
GREEN = Color(rgb=(54 * 0.4 / 255, 139 / 255, 27 * 0.4 / 255))
RED = Color(rgb=(184 * 0.7 / 255, 44 * 0.4 / 255, 8 * 0.4 / 255))

retro = ColoursFromList([PINK,BLUE,ORANGE,GREEN,RED])
